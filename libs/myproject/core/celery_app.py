# -*- coding:utf-8 -*-
"""celery后台任务配置
"""
from celery import Celery

cel = Celery('tasks',
             broker=BROKER,  # 消息代理用 RabbitMQ
             backend=BACKEND,  # 存储结果用redis
             # 包含以下多项任务文件，去相应的py文件中找任务，对多个任务做分类
             include=['tasks.extract_task',
                      'tasks.notify_task',
                      'tasks.vector_stores_task',
                      ]
             )
# 自动发现任务
# myproject.autodiscover_tasks(['fdb.tasks'])
# 时区
cel.conf.timezone = 'Asia/Shanghai'
# 是否使用UTC
cel.conf.enable_utc = False
cel.conf.broker_connection_retry_on_startup = True # 是否重试连接

# 启动命令 celery -A tasks worker -l info -P eventlet
