#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/1
# @Author  : AngesZhu
# @File    : routes_utils.py
# @Desc    : 动态路由加载
import importlib.util
from kui.wsgi import Routes


def loading_routes(applications_config: dict) -> Routes:

    _return_routers = Routes()

    for application in applications_config:
        _temp_data = applications_config[application]
        _method = _temp_data["routes_method"] if _temp_data.__contains__("routes_method") else "routes"
        _path = "/{}".format(_temp_data["path"]) if _temp_data.__contains__("path") else None
        _temp_routers = None
        _middlewares = []

        if _temp_data.__contains__("middlewares"):
            if isinstance(_temp_data["middlewares"], (tuple, list, set)):
                for middleware_str in _temp_data["middlewares"]:
                    _temp = middleware_str.split(".")
                    _module_obj = importlib.import_module(_temp[0], package=__package__)
                    _middlewares.append(getattr(_module_obj, _temp[1]))
            elif isinstance(_temp_data["middlewares"], (str,)):
                _temp = _temp_data["middlewares"].split(".")
                _module_obj = importlib.import_module(_temp[0], package=__package__)
                _middlewares.append(getattr(_module_obj, _temp[1]))
            else:
                raise TypeError(f"{_temp_data['describe']}'s middlewares type exception")
        else:
            raise ValueError(f"{_temp_data['describe']} has no middlewares")

        if _temp_data.__contains__("modules"):
            _temp_routers = Routes(http_middlewares=_middlewares)
            if isinstance(_temp_data["modules"], (tuple, list, set)):
                [_temp_routers << getattr(importlib.import_module(module, package=__package__), _method) for module in
                 _temp_data["modules"]]
            elif isinstance(_temp_data["modules"], (str,)):
                _temp_routers << getattr(importlib.import_module(_temp_data["modules"], package=__package__), _method)
            else:
                raise TypeError(f"{_temp_data['describe']}'s modules type exception")
        else:
            raise ValueError(f"{_temp_data['describe']} has no modules")

        if _temp_routers:
            if _path:
                _return_routers << _path // _temp_routers
            else:
                _return_routers << _temp_routers

    return _return_routers
