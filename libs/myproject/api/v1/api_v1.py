# -*- coding:utf-8 -*-
from fastapi import APIRouter
from api.v1.routes import chat_bot

router = APIRouter()

router.include_router(chat_bot.router, prefix="/chat", tags=["对话"])

