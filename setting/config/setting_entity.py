#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/29
# @Author  : AngesZhu
# @File    : setting_entity.py
# @Desc    : 系统配置对象
import os
from pydantic import BaseModel, BaseSettings


class MysqlModel(BaseModel):
    USERNAME: str
    PASSWORD: str
    HOST: str
    PORT: int
    DATABASE: str


class RedisModel(BaseModel):
    HOST: str
    PASSWORD: str
    DB: int
    PORT: int
    TIMEOUT: int


class ProjectModel(BaseModel):
    PORT: int
    BASE_PATH: str


class SwaggerModel(BaseModel):
    SHOW: bool
    TITLE: str
    VERSION: str
    DESCRIPTION: str
    DOCS_URL: str
    REDOC_URL: str


class AccessModel(BaseModel):
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    ALGORITHM: str
    SECRET_KEY: str


class RPCModel(BaseModel):
    TITLE: str
    VERSION: str
    DESCRIPTION: str


class DatabaseModel(BaseModel):
    MYSQL: MysqlModel
    REDIS: RedisModel


class SettingModel(BaseSettings):

    PROJECT: ProjectModel
    # APP: List
    SWAGGER: SwaggerModel
    ACCESS: AccessModel
    DATABASE: DatabaseModel
    RPC: RPCModel
    # token过期时间 15天
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    # 生成token的加密算法
    ALGORITHM: str
    # 生产环境保管好 SECRET_KEY
    SECRET_KEY: str

    # 项目根路径
    BASE_PATH: str = os.path.dirname(os.path.dirname(os.path.dirname((os.path.abspath(__file__)))))