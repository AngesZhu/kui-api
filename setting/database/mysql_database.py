#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/29
# @Author  : AngesZhu
# @File    : authority_entity.py
# @Desc    : 创建数据库对象，初始化数据库
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from setting.config import MysqlModel
from setting import settings
"""
sqlalchemy操作数据库
https://docs.sqlalchemy.org/en/20/
"""

MYSQL = MysqlModel.copy(settings.DATABASE.MYSQL)
SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{MYSQL.USERNAME}:{MYSQL.PASSWORD}@{MYSQL.HOST}:{MYSQL.PORT}/{MYSQL.DATABASE}?charset=utf8mb4"
engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True, pool_recycle=3600, pool_size=200)
SessionLocal = sessionmaker(bind=engine)
DatabaseModel = declarative_base()
