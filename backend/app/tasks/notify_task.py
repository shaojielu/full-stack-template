# -*- coding:utf-8 -*-
from backend.app.core.celery_app import cel
from backend.app.core.logger import logger
import requests


# 异步消息通知。最大通知10次
@cel.task(bind=True, max_retries=10)
def notify_task(self, task_id, status, result, url):
    """
    Celery 任务 - 发送 HTTP POST 请求通知外部系统，并检查响应是否为 'ok'。
    :param self: celery
    :param task_id: 任务ID
    :param status: 任务状态
    :param result: 任务结果
    :param url: 通知的 URL
    :return: None
    """
    data = {
        "task_id": task_id,
        "status": status,
        "result": result,
    }

    try:
        # 发送 HTTP POST 请求
        response = requests.post(url, json=data)
        response.raise_for_status()  # 检查 HTTP 状态码是否为 2xx

        # 判断响应内容是否为 'ok'
        if response.text.strip().lower() == 'ok':
            logger.info(f'通知成功，收到 "ok" 回复 - 任务ID: {task_id}')
            return  # 收到 'ok'，任务结束，不再重试

        # 如果不是 'ok'，记录日志并触发重试
        logger.warning(f'通知成功，但未收到 "ok" 回复 - 任务ID: {task_id}, 响应内容: {response.text}')
        raise Exception('未收到预期的 "ok" 回复')

    except requests.exceptions.RequestException as e:
        logger.error(f'通知发送失败 - 任务ID: {task_id}, 错误信息: {str(e)}')
        _retry_task(self, e)

    except Exception as e:
        logger.warning(f'任务异常：{str(e)}')
        _retry_task(self, e)


def _retry_task(self, exc):
    """
    处理任务的重试逻辑。
    :param self: 当前任务实例
    :param exc: 异常对象
    """
    retry_count = self.request.retries
    countdown = 300 * (2 ** retry_count)  # 计算重试延迟时间
    try:
        raise self.retry(exc=exc, countdown=countdown)
    except self.MaxRetriesExceededError:
        logger.error(f'通知重试已达到最大次数 - 任务ID: {self.request.id}')


def get_notify_url(task_kwargs):
    """ 获取通知 URL，若未提供则返回默认值 """
    return task_kwargs.get('notify_url', 'https://default-url.com/notify')
