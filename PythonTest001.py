#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Python Test 001
# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

# 方法一
n = 0
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if (i != j) and (i != k) and (j != k):
                n += 1
print(n)

# 方法二
