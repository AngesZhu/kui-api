#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/29
# @Author  : AngesZhu
# @File    : ip_utils.py
# @Desc    : 获取ip地址封装
import socket


def get_host_ip():
    """
    查询本机ip地址
    :return:
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip


# if __name__ == '__main__':
#     print(get_host_ip())