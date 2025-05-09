# -*- coding:utf-8 -*-
from backend.app.models.models import TaskResult
from backend.app.core.celery_app import celery_app
from backend.app.core.logger import logger
from celery.result import AsyncResult


def check_result(id):
    async_result = AsyncResult(id=id, app=celery_app)
    if async_result.successful():
        result = async_result.get()
        logger.info(f'{id}任务执行成功,结果为{result}')
        # 在获取成功结果后删除任务，释放资源
        async_result.forget()
        return TaskResult(status='success', result=result)

        # async.revoke(terminate=True)  # 无论现在是什么时候，都要终止
        # async.revoke(terminate=False) # 如果任务还没有开始执行呢，那么就可以终止。
    elif async_result.failed():
        logger.info(f'{id}执行失败')
        return TaskResult(status='failed', result="任务执行失败")

    elif async_result.status == 'PENDING':
        logger.info(f'{id}任务以被执行等待中')
        return TaskResult(status='pending', result="任务以被执行等待中")

    elif async_result.status == 'RETRY':
        logger.info(f'{id}任务异常后正在重试')
        return TaskResult(status='retry', result="任务异常后正在重试")

    elif async_result.status == 'STARTED':
        logger.info(f'{id}任务已经开始被执行')
        return TaskResult(status='started', result="任务已经开始被执行")
