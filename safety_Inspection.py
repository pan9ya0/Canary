# encoding=utf-8
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/8 14:05
# @Author  : Pan9ya0
# @Email   : su33e7@gmail.com
# @File    : safety_Inspection.py

from ctypes import *

class safeDetect:

    def __init__(self,path_to_file,confidentiality_level):
        self.path = path_to_file
        self.confidentiality = confidentiality_level

    def scan(self):
        try:
            if self.confidentiality:
                self.local_security_detect()
            else:
                self.exposure_scan()
        except Exception as e:
            print(e.with_traceback())

    def local_security_detect(self):
        self.avlscan()

    def exposure_scan(self):

    def avlscan(self):
        def