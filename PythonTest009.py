#!usr/bin/python
# -*- coding:UTF-8 -*-

# Python Test 009
"""
暂停一秒输出
"""

# 方法一

import time

myD = {1: 'a', 2: 'b'}
for key, value in dict.items(myD):
    print(key, value)
    time.sleep(1)  # 暂停一秒，python中单位为秒

# 方法二

l = [1, 2, 3, 4]
for i in range(len(l)):
    print(l[i])
    time.sleep(1)
