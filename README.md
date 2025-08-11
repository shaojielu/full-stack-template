# Full-Stack Template (全栈开发模板)

这是一个现代化的、开箱即用的全栈项目模板，集成了 Python (FastAPI) 后端和 Vue.js 前端。

项目通过 Docker Compose 进行容器化编排，实现了开发、测试和部署的统一管理，旨在帮助开发者快速启动新项目。

## ✨ 功能特性

- **前后端分离**: 清晰的目录结构，便于团队协作。
- **容器化**: 使用 Docker 和 Docker Compose，实现一键启动和环境一致性。
- **现代技术栈**: 后端采用 FastAPI，前端采用 Vue 3，均为当前主流的高性能框架。
- **数据库管理**: 集成 SQLAlchemy ORM 和 Alembic 数据库迁移工具。
- **异步支持**: 全面拥抱异步编程，从 Web 框架到数据库操作。
- **配置灵活**: 通过 `.env` 文件管理环境变量，轻松切换配置。
- **API 文档**: FastAPI 自动生成交互式 API 文档 (Swagger UI / ReDoc)。

## 🛠️ 技术栈

| 分类         | 技术                                                              |
|--------------|-------------------------------------------------------------------|
| **后端**     | Python 3.12+, FastAPI, SQLAlchemy, Alembic, Uvicorn, Pydantic     |
| **前端**     | Vue 3, Vite, TypeScript, Pinia, Vue Router, Axios, Element Plus   |
| **数据库**   | PostgreSQL, Redis (用于缓存和消息队列)                            |
| **对象存储**   | S3, COS                          |
| **包管理**   | `uv` (后端), `pnpm` (前端)                                        |
| **容器化**   | Docker, Docker Compose                                            |
| **测试**     | Pytest (后端), Vitest (前端单元测试), Playwright (前端 E2E 测试)   |
| **代码规范** | ESLint (前端)                                                     |

## 📂 项目结构

```
.
├── backend/         # FastAPI 后端应用
├── docs/            # 项目文档
├── frontend/        # Vue.js 前端应用
├── scripts/         # 构建或部署脚本
├── .env.example     # 根环境变量示例
└── docker-compose.yml # Docker 服务编排
```

## 🚀 快速开始 (推荐)

这是最简单的启动方式，需要你的机器上安装了 Docker 和 Docker Compose。

1.  **克隆项目**
    ```bash
    git clone https://github.com/shaojielu/full-stack-template.git
    cd full-stack-template
    ```

2.  **创建环境变量文件**
    项目依赖 `.env` 文件来配置服务。请根据 `.env.example` 创建并自定义你的配置。
    ```bash
    # 复制后端环境变量文件
    cp backend/.env.example backend/.env
    ```
    > **提示**: 请检查并按需修改 `backend/.env` 文件中的 `POSTGRES_USER`, `POSTGRES_PASSWORD`, `SECRET_KEY` 等变量。

3.  **启动服务**
    使用 Docker Compose 构建并启动所有服务（后端、前端、数据库等）。
    ```bash
    docker-compose up --build
    ```
    `-d` 参数可以在后台运行服务: `docker-compose up --build -d`

4.  **访问应用**
    服务启动成功后，你可以访问：
    - **前端页面**: [http://localhost](http://localhost) (由 Nginx 代理)
    - **后端 API 文档**: [http://localhost:8000/docs](http://localhost:8000/docs)
    - **pgAdmin (数据库管理)**: [http://localhost:8088](http://localhost:8088)

## 💻 本地开发 (不使用 Docker)

如果你想独立运行前端或后端进行开发。

### 后端 (Backend)

1.  **进入目录**
    ```bash
    cd backend
    ```
2.  **安装依赖**
    推荐使用 `uv` (它会自动创建 `.venv` 虚拟环境)。
    ```bash
    uv sync
    ```
3.  **配置环境**
    复制并修改 `.env` 文件。
    ```bash
    cp .env.example .env
    ```
4.  **应用数据库迁移**
    确保数据库服务已在运行，然后在 `.env` 中配置好数据库连接。
    ```bash
    alembic upgrade head
    ```
5.  **启动开发服务器**
    `uv` 会启动一个支持热重载的服务器。
    ```bash
    uvicorn app.api.main:app --reload --host 0.0.0.0 --port 8000
    ```

### 前端 (Frontend)

1.  **进入目录**
    ```bash
    cd frontend
    ```
2.  **安装依赖**
    推荐使用 `pnpm`。
    ```bash
    pnpm install
    ```
3.  **启动开发服务器**
    这将启动一个支持热更新的开发服务器。
    ```bash
    pnpm dev
    ```
    访问地址: [http://localhost:5173](http://localhost:5173)

## 🗃️ 数据库迁移

本项目使用 Alembic 管理数据库结构变更。

当你修改了 `backend/app/models.py` 中的模型后，需要执行以下步骤：

1.  **生成迁移脚本**
    ```bash
    # 在 backend 目录下执行
    alembic revision --autogenerate -m "你的迁移描述"
    ```
    例如: `alembic revision --autogenerate -m "add_user_age_column"`

2.  **应用迁移**
    此命令会将数据库结构更新到最新版本。
    ```bash
    # 在 backend 目录下执行
    alembic upgrade head
    ```
    > **注意**: `docker-compose up` 命令会自动执行 `alembic upgrade head`。

## 📜 可用脚本

### 后端 (`backend` 目录)
- `uvicorn app.api.main:app`: 启动服务。
- `pytest`: 运行测试。
- `alembic ...`: 数据库迁移相关命令。

### 前端 (`frontend` 目录)
- `pnpm dev`: 启动开发服务器。
- `pnpm build`: 构建生产版本。
- `pnpm test:unit`: 运行单元测试。
- `pnpm test:e2e`: 运行端到端测试。
- `pnpm lint`: 检查代码格式。