#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/29
# @Author  : AngesZhu
# @File    : redis_utils.py
# @Desc    : redis操作封装
from redis import Redis, AuthenticationError
import sys
from setting import settings
from setting.config import RedisModel
from setting.logger_config import logger


class RedisCli:

    def __init__(self, *, host: str, port: int, password: str, db: int, socket_timeout: int = 5):
        self._redis_client = None
        self.host = host
        self.port = port
        self.password = password
        self.db = db
        self.socket_timeout = socket_timeout

    def init_redis_connect(self) -> None:
        """
        初始化连接
        :return:
        """
        try:
            logger.info("初始化redis连接")
            self._redis_client = Redis(
                host=self.host,
                port=self.port,
                password=self.password,
                db=self.db,
                socket_timeout=self.socket_timeout,
                decode_responses=True  # 解码
            )
            if not self._redis_client.ping():
                logger.info("连接redis超时")
                sys.exit()
        except (AuthenticationError, Exception) as e:
            logger.info(f"连接redis异常 {e}")
            sys.exit()

    def __getattr__(self, name):
        return getattr(self._redis_client, name)

    def __getitem__(self, name):
        return self._redis_client[name]

    def __setitem__(self, name, value):
        self._redis_client[name] = value

    def __delitem__(self, name):
        del self._redis_client[name]


REDIS = RedisModel.copy(settings.DATABASE.REDIS)


redis_client: Redis = RedisCli(
    host=REDIS.HOST,
    port=REDIS.PORT,
    password=REDIS.PASSWORD,
    db=REDIS.DB,
    socket_timeout=REDIS.TIMEOUT
)

__all__ = ["redis_client"]
