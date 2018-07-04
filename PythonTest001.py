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

list_num = [1, 2, 3 ,4]
list = [i * 100 + j * 10 + k for i in list_num for j in list_num for k in list_num \
        if (j != i and k != j and k != i)]
print(list.__len__())

# 方法三

num = [1, 2, 3, 4]
n = 0
for i in num:
    for j in num:
        for k in num:
            if (i != j) and (i != k) and (j != k):
                n += 1
print(n)

# 方法四

list_num = ['1', '2', '3', '4']
list_result = []
for i in list_num:
    for j in list_num:
        for k in list_num:
            if len(set(i + j + k)) == 3:
                list_result += [int(i + j + k)]
print(len(list_result))

# 方法五

from itertools import permutations
n = 0
for i in permutations([1, 2, 3, 4], 3):
    n += 1
print(n)

# 方法六
# 从 00 01 10 到 11 10 01
n = 0
for num in range(6, 58):
    a = num >> 4 & 3
    b = num >> 2 & 3
    c = num & 3
    if (a ^ b) and (b ^ c) and (a ^ c):
        n += 1
print(n)

# 方法七

n = 0
for i in range(1, 5):
    for j in range(1, 5):
        if j == i:
            continue
        for k in range(1, 5):
            if k == i or k == j:
                continue
            n += 1
print(n)

