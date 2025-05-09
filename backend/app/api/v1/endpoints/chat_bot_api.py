from fastapi import APIRouter, Depends, Request

from core.deps import chat_bot_service
from core.logger import logger
from api.v1.schemas.chat_bot_schema import CreateChatBotRequest

router = APIRouter()


@router.post("/chat_bot/create",
             summary="创建聊天机器人接口",
             description="创建聊天机器人接口",
             dependencies=[Depends(chat_bot_service)], )
async def create_chat_bot(request: CreateChatBotRequest):
    """创建聊天机器人"""
    pass
