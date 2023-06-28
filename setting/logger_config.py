#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/29
# @Author  : AngesZhu
# @File    : logger_config.py
# @Desc    : 日志初始化配置
import os, time
from loguru import logger
"""
loguru好看的日志模块
更多用法以及api详见文档：https://loguru.readthedocs.io/en/stable/index.html
"""

basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

log_path = os.path.join(basedir, 'logs')

if not os.path.exists(log_path):
 os.mkdir(log_path)

api_log_path = os.path.join(log_path, '{}-{}.log'.format('api', time.strftime("%Y-%m-%d")))

format_str = '{time:YYYY-MM-DD HH:mm:ss} | {thread.name}:{thread.id} | {function}:{module}:{line} - {level} - {message}'

log_path_info = os.path.join(log_path, f'{time.strftime("%Y-%m-%d")}_info.log')
log_path_warning = os.path.join(log_path, f'{time.strftime("%Y-%m-%d")}_warning.log')
log_path_error = os.path.join(log_path, f'{time.strftime("%Y-%m-%d")}_error.log')

# 日志简单配置 文件区分不同级别的日志
logger.add(log_path_info, format=format_str, rotation="00:00", compression="zip", retention="15 days", encoding='utf-8', enqueue=True, level='INFO')
logger.add(log_path_warning, format=format_str, rotation="00:00", compression="zip", retention="15 days", encoding='utf-8', enqueue=True, level='WARNING')
logger.add(log_path_error, format=format_str, rotation="00:00", compression="zip", retention="15 days", encoding='utf-8', enqueue=True, level='ERROR')

format_str = '{time:YYYY-MM-DD HH:mm:ss} | {thread.name}:{thread.id} | {function}:{module}:{line} - {level} - {message}'

__all__ = ["logger"]
