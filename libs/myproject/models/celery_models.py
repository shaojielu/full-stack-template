# -*- coding:utf-8 -*-
from typing import Optional
from pydantic import BaseModel, Field


# celery任务检查返回
class TaskResult(BaseModel):
    status: str = Field(description="任务状态")
    result: Optional[object] = Field(description="任务结果")
