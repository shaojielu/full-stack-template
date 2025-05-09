from pydantic import BaseModel


class CreateChatBotRequest(BaseModel):
    name: str