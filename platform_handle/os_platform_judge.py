# encoding=utf-8
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/9 0:30
# @Author  : Pan9ya0
# @Email   : su33e7@gmail.com
# @File    : os_platform_judge.py

import platform


class os_info:
    def __init__(self):
        self.python_version = platform.python_version()
        self.arch = platform.architecture()
        self.platform = platform.platform()
        self.python_compiler_info = platform.python_compiler()
        self.platform_version = platform.version()
        self.os_alias = platform.system()

    def sys_info(self):
        sys_str = self.os_alias

        if sys_str == "Windows":
            print("Call Windows API to Security analysis")
        elif sys_str == "Linux":
            print("Call Linux API/Tolls to Security analysis")
        else:
            print(sys_str)
            print("Other System tasks")
# test = os()
# test.sys_info()
