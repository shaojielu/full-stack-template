# -*- coding:utf-8 -*-
"""统一的后台系统日志处理
"""
import logging
import sys
from pathlib import Path

# 定义项目名（根据实际情况设置）
PROJECT_NAME = "full-stack-template"

# 获取项目根目录（根据你的项目结构调整）
PROJECT_ROOT = Path(__file__).parent

# 自定义 LogRecord 工厂函数
old_factory = logging.getLogRecordFactory()


def record_factory(*args, **kwargs):
    record = old_factory(*args, **kwargs)
    # 设置项目名
    record.project_name = PROJECT_NAME
    # 获取文件路径
    pathname = Path(record.pathname)
    try:
        # 获取相对于项目根目录的相对路径
        relative_path = pathname.relative_to(PROJECT_ROOT)
        # 提取包名（目录结构，去掉文件名）
        package_parts = relative_path.parts[:-1]  # 去除文件名
        record.package_name = '.'.join(package_parts) if package_parts else ''
    except ValueError:
        # 如果无法获取相对路径，设置包名为空
        record.package_name = ''
    return record


logging.setLogRecordFactory(record_factory)


# 自定义过滤器，只允许特定级别的日志通过
class LevelFilter(logging.Filter):
    def __init__(self, level):
        super().__init__()
        self.level = level

    def filter(self, record):
        return record.levelno == self.level


def _reset_logger(log):
    # 关闭并移除现有的处理器
    for handler in log.handlers[:]:
        handler.close()
        log.removeHandler(handler)
    log.handlers = []
    log.propagate = False

    # 创建统一的格式器，包含项目名和包名
    formatter = logging.Formatter(
        "[%(levelname)s][%(asctime)s][%(project_name)s][%(package_name)s][%(filename)s:%(lineno)d] - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # 控制台处理器
    console_handle = logging.StreamHandler(sys.stdout)
    console_handle.setFormatter(formatter)
    console_handle.setLevel(logging.DEBUG)

    # 创建文件处理器和过滤器

    # Info级别日志处理器
    info_file = Path.cwd() / "info.log"
    info_handle = logging.FileHandler(info_file, encoding="utf-8")
    info_handle.setFormatter(formatter)
    info_handle.setLevel(logging.DEBUG)
    info_handle.addFilter(LevelFilter(logging.INFO))

    # Error级别日志处理器
    error_file = Path.cwd() / "error.log"
    error_handle = logging.FileHandler(error_file, encoding="utf-8")
    error_handle.setFormatter(formatter)
    error_handle.setLevel(logging.DEBUG)
    error_handle.addFilter(LevelFilter(logging.ERROR))

    # Debug级别日志处理器
    debug_file = Path.cwd() / "debug.log"
    debug_handle = logging.FileHandler(debug_file, encoding="utf-8")
    debug_handle.setFormatter(formatter)
    debug_handle.setLevel(logging.DEBUG)
    debug_handle.addFilter(LevelFilter(logging.DEBUG))

    # 将处理器添加到日志器
    log.addHandler(console_handle)
    log.addHandler(info_handle)
    log.addHandler(error_handle)
    log.addHandler(debug_handle)
    log.setLevel(logging.DEBUG)


def _get_logger():
    # 使用模块的 __name__ 作为日志器名称
    log = logging.getLogger(__name__)
    _reset_logger(log)
    return log


# 初始化日志器
logger = _get_logger()

if __name__ == "__main__":
    logger.debug("这是一个调试日志")
    logger.info("这是一个信息日志")
    logger.error("这是一个错误日志")
