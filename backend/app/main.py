from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from core.config import settings
from api.v1.v1_router import v1_router


app = FastAPI(title="通用全栈开发模版后端api",
              docs_url="/docs",
              redoc_url="/redoc",
              version="0.0.1")

# 允许本地跨域请求
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1",
        f"http://127.0.0.1:{settings.fast_api_port}"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(v1_router, prefix="/v1")

if __name__ == "__main__":
    uvicorn.run("main:app",
                reload=True,
                host=settings.fast_api_host,
                port=settings.fast_api_port,
                workers=settings.fast_api_workers)
