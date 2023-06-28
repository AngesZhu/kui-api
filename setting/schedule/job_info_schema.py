#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/22 10:19
# @Author  : AngesZhu
# @File    : job_info_schema.py
# @Desc    :
from pydantic import BaseModel
from typing import Optional


class JobInfo(BaseModel):
    method: str
    path: str
    id: str
    type: str
    param: Optional[str]
    headers: Optional[str]
