#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/01/04
# @Author  : AngesZhu
# @File    : operation_middleware.py
# @Desc    : 操作记录中间件
import time
from kui.wsgi import request
from setting import logger


def operation_middleware(endpoint):
    def wrapper():
        # db: Session = SessionLocal()
        logger.info("请求开始：{}: {}: {}".format(request.method, request.url.scheme, request.url))
        data = {
            "ip": "{}:{}".format(request.client.host, request.client.port),
            "method": request.method,
            "path": request.url.path,
            "data": str(request.query_params) if request.method == "GET" else str(request.json),
        }
        logger.info("请求参数：{}".format(data))
        start_time = time.time()
        response = endpoint()
        end_time = time.time()
        process_time = (end_time - start_time) * 1000
        formatted_process_time = '{0:.2f}'.format(process_time)
        logger.info(
            f"请求结束: 请求处理时长: {formatted_process_time} ms, status_code: {response.status_code}, headers: {response.headers}")
        return response
    return wrapper
