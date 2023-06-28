#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-12-25
# @Author  : AngesZhu
# @File    : response_code_utils.py
# @Desc    : 响应对象封装
from typing import Union

from kui import status
from kui.wsgi.responses import JSONResponse
from setting.common.jsonable_encoder import jsonable_encoder
from dataclasses import make_dataclass


def success_200(data: Union[list, dict, str] = None, code: int = 200, message: str = "Success", ignore: list = None) -> JSONResponse:
    return response_base(status.HTTP_200_OK, data, code, message, ignore).Success()


def error_400(data: Union[list, dict, str] = None, code: int = 400, message: str = "请求失败") -> JSONResponse:
    return response_base(status.HTTP_400_BAD_REQUEST, data, code, message).Success()


def error_403(data: Union[list, dict, str] = None, code: int = 403, message: str = "Token 认证失败") -> JSONResponse:
    return response_base(status.HTTP_403_FORBIDDEN, data, code, message).Success()


def error_500(data: Union[list, dict, str] = None, code: int = 500, message: str = "Internal Server Error") -> JSONResponse:
    return response_base(status.HTTP_500_INTERNAL_SERVER_ERROR, data, code, message).Success()


response_base = make_dataclass(
    "response_base",
    [('http_status', int, None), ('data', Union[list, dict, str], None), ('code', int, None), ('message', str, None),
     ('ignore', list, None)],
    namespace={
        "Success": lambda self: JSONResponse(
            status_code=self.http_status,
            # status_code=self.code,
            content=jsonable_encoder({'code': self.code, 'message': self.message, 'data': self.data}, ignore=self.ignore)
        ),
    }
)
