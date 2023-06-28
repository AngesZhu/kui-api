#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/26
# @Author  : AngesZhu
# @File    : middlewares.py
# @Desc    : 数据库相关中间件封装
import functools
from kui.wsgi import Depends
from sqlalchemy.orm import Session
from setting.logger_config import logger
from setting.register import response_code
from setting.database import get_db

__all__ = ["db_affair_alone", "db_affair_multiple"]


@logger.catch()
def db_affair_alone(endpoint):
    @functools.wraps(endpoint)
    def wrapper(db: Session = Depends(get_db), *args, **kwargs):
        db.begin_nested()
        try:
            __data_temp = endpoint(db=db, *args, **kwargs)
            db.commit()
            db.flush()
            db.refresh(__data_temp)
            # return __data_temp
            return response_code.success_200(data=__data_temp)
        except Exception as ex:
            db.rollback()
            logger.error("数据库执行异常，异常回滚，{}".format(ex))
            return response_code.error_400(message="数据库异常，请稍后再试", data="数据库异常，请稍后再试")

    return wrapper


def db_affair_multiple(endpoint):
    @functools.wraps(endpoint)
    def wrapper(db: Session = Depends(get_db), *args, **kwargs):
        db.begin_nested()
        try:
            res = endpoint(db=db, *args, **kwargs)
            db.commit()
            return response_code.success_200(data=res)
        except Exception as ex:
            db.rollback()
            logger.error("数据库执行异常，异常回滚，{}".format(ex))
            return response_code.error_400(message="数据库异常，请稍后再试", data="数据库异常，请稍后再试")
    return wrapper
