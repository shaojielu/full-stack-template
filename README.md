# full stack template
python使用fast api +celery 做为后端加 vue前端的全栈开发项目模版

## 技术栈

### 后端

*   **语言**: Python 3.12+
*   **Web 框架**: FastAPI
*   **ORM**: SQLAlchemy 2.0+ (异步支持)
*   **数据库迁移**: Alembic
*   **包管理**: uv
*   **Web 服务器**: Uvicorn
*   **对象存储**: aioboto3 (S3 兼容), cos-python-sdk-v5 (腾讯云 COS)
*   **其他**: Pydantic, Passlib, PyJWT

### 前端

*   **框架**: Vue 3 (Composition API)
*   **UI 组件库**: Element Plus
*   **路由**: Vue Router
*   **状态管理**: Pinia
*   **HTTP 客户端**: Axios
*   **包管理**: pnpm

### 基础设施

*   **容器化**: Docker, Docker Compose
*   **数据库**: PostgreSQL
*   **缓存/消息队列**: Redis
*   **数据库管理工具**: pgAdmin
