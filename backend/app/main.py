# -*- coding:utf-8 -*-
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from api.main import api_router
from api.routes import extract, doc_parsing, chat, vectorstotes

app = FastAPI(
    title='python全栈开发后台API',
    description='',
    version='0.0.1',
    docs_url='/docs',
    redoc_url='/redocs',
)
# 允许本地跨越请求
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1",
        "http://127.0.0.1:8000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat.router, prefix='/v1/chat', tags=['聊天 /续写(该部分均支持流式返回)'])
app.include_router(extract.router, prefix='/v1/extraction', tags=['字段抽取'])
app.include_router(vectorstotes.router, prefix='/v1/vectorstore', tags=['向量数据库'])
# app.include_router(file.router, prefix='/v1/file', tags=['临时文件管理'])
app.include_router(doc_parsing.router, prefix='/v1/unstructured', tags=['非结构化文档解析'])
# app.include_router(auth.router, prefix='/v1/auth', tags=['身份认证'])
app.include_router(doc_parsing.router, prefix='/v1/other', tags=['其他'])

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True, workers=1)
