import logging
import os
from logging import handlers

def init_logging():
    # 1. 创建一个日志器 如果不写日志器的名称，那么会使用默认的日志器root
    logger = logging.getLogger()
    # 2. 设置日志的等级：控制打印日志的级别，使用logging打印日志时，
    # 如果日志级别低于设置的级别，那么不会打印
    logger.setLevel(logging.INFO)
    # 3. 设置处理器
    sf = logging.StreamHandler()
    logname = os.path.dirname(os.path.abspath(__file__)) + "/log/ego.log"
    fh = logging.handlers.TimedRotatingFileHandler(logname, when='M', interval=1, backupCount=7, encoding='utf-8')
    # 4. 设置格式化器 指打印日志时的格式内容（日志器名称、打印日志的函数名称、模块名称、代码行数、日志消息等内容）
    fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
    formmater = logging.Formatter(fmt)
    # 5. 将格式化器添加到处理器当中
    sf.setFormatter(formmater)
    fh.setFormatter(formmater)
    # 6. 将处理器添加到日志器中
    logger.addHandler(sf)
    logger.addHandler(fh)
