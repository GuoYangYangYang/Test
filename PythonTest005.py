#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Python Test 005
"""
输入三个整数x,y,z，请把这三个数由小到大输出。
"""

# 方法一

l = []
for i in range(3):
    x = int(input('number'))
    l.append(x)
l.sort()
print(l)

# 方法二
# 利用冒泡排序
def Sort(list):
    n = len(list)
    for i in range(1, n):
        for j in range(1, n - i + 1):
            if list[j - 1] > list[j]:
                list[j - 1], list[j] = list[j], list[j - 1]
    for i in range(0, n):
        print(list[i], '', end='')
# 写入数据
def inputData():
    list_first = []
    while True:
        a = input("number".strip())
        if len(a) == 0:
            return list_first
        else:
            list_first.append(int(a))
# 排序
if __name__ == '__main__':
    lt = inputData()
    Sort(lt)

