import uuid

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.core.security import get_password_hash, verify_password
from app.models import User
from app.schemas import UserCreate, UserUpdate


class UserService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_user_by_id(self, user_id: uuid.UUID) -> User | None:
        """
        根据用户ID获取用户。
        """
        return await self.session.get(User, user_id)

    async def get_user_by_email(self, email: str) -> User | None:
        """
        根据邮箱获取用户。
        """
        query = select(User).where(User.email == email)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()

    async def create_user(self, user_create: UserCreate) -> User:
        """
        创建新用户。
        """
        if await self.get_user_by_email(user_create.email):
            raise Exception("Email already registered")
        
        hashed_password = await get_password_hash(user_create.password)
        new_user = User(
            full_name=user_create.full_name,
            email=user_create.email,
            hashed_password=hashed_password,
            is_active=True
        )
        self.session.add(new_user)
        await self.session.commit()
        await self.session.refresh(new_user)
        return new_user

    async def update_user(self, user_id: uuid.UUID, user_update: UserUpdate) -> User:
        """
        更新用户信息。
        """
        user = await self.get_user_by_id(user_id)
        if not user:
            raise Exception("User not found")
        
        update_data = user_update.model_dump(exclude_unset=True)

        if "email" in update_data and update_data["email"] != user.email:
            existing_user = await self.get_user_by_email(update_data["email"])
            if existing_user and existing_user.id != user.id:
                raise Exception("This email is already registered to another user.")
        
        for key, value in update_data.items():
            if key == "password":
                setattr(user, "hashed_password", await get_password_hash(value))
            else:
                setattr(user, key, value)
        
        await self.session.commit()
        await self.session.refresh(user)
        return user

    async def authenticate_user(self, email: str, password: str) -> User:
        """
        认证用户。
        """
        db_user = await self.get_user_by_email(email)
        
        if not db_user:
            raise Exception("Incorrect username or password")
        if not await verify_password(password, db_user.hashed_password):
            raise Exception("Incorrect username or password")
        
        return db_user
