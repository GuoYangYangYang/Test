#!usr/bin/python
# -*- coding:UTF-8 -*-

# Python Test 010
"""
暂停一秒输出，并格式化当前时间
"""

# 方法一

import time
for i in range(1, 11):
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    time.sleep(1)

# 方法二

import datetime
for i in range(1, 11):
    TIME = datetime.datetime.now()
    print(TIME.strftime('%Y-%m-%d %H:%M:%S'))
    time.sleep(1)
