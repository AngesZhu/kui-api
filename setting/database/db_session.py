#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/26
# @Author  : AngesZhu
# @File    : db_session.py
# @Desc    : 数据库会话对象
from typing import Generator
from setting.database import SessionLocal

__all__ = ["get_db"]


def get_db() -> Generator:
    """
    获取sqlalchemy会话对象
    :return:
    """
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
