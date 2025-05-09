# -*- coding:utf-8 -*-
import sys
import logging
from logging.handlers import RotatingFileHandler
from typing import Optional


def get_logger(
        name: str = "log",
        level: int = logging.DEBUG,
        logfile: str = "run.log",
        max_bytes: int = 10 * 1024 * 1024,  # 10MB
        backup_count: int = 5,
        formatter: Optional[logging.Formatter] = None,
) -> logging.Logger:
    """
    获取配置好的日志记录器

    Args:
        name: 日志记录器名称
        level: 日志级别
        logfile: 日志文件路径
        max_bytes: 单个日志文件最大字节数
        backup_count: 保留的日志文件数量
        formatter: 自定义的日志格式器
    """
    log = logging.getLogger(name)
    log.setLevel(level)
    log.propagate = False

    # 清除已有的处理器
    for handler in log.handlers[:]:
        handler.close()
        log.removeHandler(handler)

    # 使用默认格式器或自定义格式器
    if formatter is None:
        formatter = logging.Formatter(
            "[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d] - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

    # 控制台处理器
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    log.addHandler(console_handler)

    # 文件处理器(带轮转)
    file_handler = RotatingFileHandler(
        filename=logfile,
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding="utf-8"
    )
    file_handler.setFormatter(formatter)
    log.addHandler(file_handler)

    return log


# 获取默认日志记录器
logger = get_logger()
