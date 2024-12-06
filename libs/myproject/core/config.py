# -*- coding:utf-8 -*-
from typing import Optional, List
from dataclasses import dataclass, field
from functools import lru_cache


@dataclass
class Settings:
    """应用总配置"""
    """PostgresSQL配置"""
    pg_host: str = "127.0.0.1"
    pg_port: int = 5432
    pg_username: str = "postgres"
    pg_password: str = "postgres"

    """Redis配置"""
    redis_host: str = "127.0.0.1"
    redis_port: int = 6379
    redis_password: Optional[str] = None

    """RabbitMQ配置"""
    rabbitmq_host: str = "127.0.0.1"
    rabbitmq_port: int = 5672
    rabbitmq_username: str = "guest"
    rabbitmq_password: str = "guest"

    """celery配置"""
    celery_broker: str = f"amqp://{rabbitmq_username}:{rabbitmq_password}@{rabbitmq_host}:{rabbitmq_port}//"
    celery_backend: str = f"redis://:{redis_password}@{redis_host}:{redis_port}"
    task_serializer: str = "json"
    accept_content: List[str] = field(default_factory=lambda: ["json"])
    result_serializer: str = "json"
    timezone: str = "Asia/Shanghai"
    enable_utc: bool = True

    """fast_api配置"""
    fast_api_host: str = "0.0.0.0"
    fast_api_port: int = 8000
    fast_api_workers: int = 1


@lru_cache()
def get_settings() -> Settings:
    """获取设置单例实例"""
    return Settings()


# 获取设置单例实例
settings = get_settings()

if __name__ == "__main__":
    print(settings)
