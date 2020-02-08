# encoding=utf-8
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/8 13:29
# @Author  : Pan9ya0
# @Email   : su33e7@gmail.com
# @File    : main.py

"""
This is Cananry framework's main file
"""
from platform_handle import os_platform_judge


class anlysisFile:
    def __init__(self):

        # 设置文件密级,决定在安全scan中是否进行泄露式文件扫描
        self.secret = None

    def select_os_platform(self):
        """
        获得当前OS及env信息，对系统支持的安全分析API/Tools进行调用
        :return: os信息，可用API信息，可用Tools信息
        """
        info = os_platform_judge.os_info()
        info.sys_info()
