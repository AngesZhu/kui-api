#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/29
# @Author  : AngesZhu
# @File    : server.py
# @Desc    : 应用启动初始化
from baize.wsgi import Subpaths
from kui.wsgi import Kui
import httpx
from rpcpy import RPC
from rpcpy.client import Client

from setting.common.ip_utils import get_host_ip
from setting import logger
from setting.router import router
from setting import settings
from setting.database import redis_client
from setting.schedule import schedule


__all__ = ["start_app"]


def kui_app() -> Kui:
    logger.info("create kui app object")
    app = Kui(
        routes=router,
    )

    logger.info("kui application create successfully")
    logger.info(f"Server address http://{get_host_ip()}:{settings.PROJECT.PORT}")
    if settings.SWAGGER.SHOW:
        logger.info(f"Api doc address http://{get_host_ip()}:{settings.PROJECT.PORT}{settings.SWAGGER.DOCS_URL}")
        logger.info(f"Api redoc address http://{get_host_ip()}:{settings.PROJECT.PORT}{settings.SWAGGER.REDOC_URL}")
    return app


def rpc_app() -> RPC:
    logger.info("create rpc app object")
    server = RPC(prefix="/rpc/", openapi={"title": settings.RPC.TITLE, "description": settings.RPC.DESCRIPTION, "version": settings.RPC.VERSION})
    client = Client(httpx.Client(), base_url=f"http://{get_host_ip()}:{settings.PROJECT.PORT}/")
    logger.info("rpc application create successfully")
    logger.info(f"rpc openapi-docs address http://{get_host_ip()}:{settings.PROJECT.PORT}{'/rpc/openapi-docs'}")

    @client.remote_call
    @server.register
    def sayhi(name: str) -> str:
        return f"hi {name}"

    return server


def start_app():

    logger.info("loading application configuration")

    logger.info("initialize connection，Redis、schedule")
    # 连接redis
    redis_client.init_redis_connect()
    # 初始化 apscheduler
    schedule.init_scheduler()

    http_app = kui_app()
    rpcpy_app = rpc_app()
    app = Subpaths(
        ("/rpc", rpcpy_app),
        ("", http_app),
    )

    logger.info("""                    
 __         .__                 .__ 
|  | ____ __|__|  _____  ______ |__|
|  |/ /  |  \  |  \__  \ \____ \|  |
|    <|  |  /  |   / __ \|  |_> >  |
|__|_ \____/|__|  (____  /   __/|__|
     \/                \/|__|       """)
    logger.info("Application started successfully")
    return app
