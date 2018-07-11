#!usr/bin/python
# -*- coding:UTF-8 -*-

# Python Test 008
"""
输出9*9乘法口诀表
"""

# 方法一

for i in range(1, 10):
    for j in range(1, i + 1):
        print("%d * %d = %d" % (i, j, i * j), end=" ")
    print()

# 方法二

i, j = 0, 0
while i < 9:
    i += 1
    while j < 9:
        j += 1
        print(j, "*", i, "=", i * j, end=" ")
        if i == j:
            j = 0
            print()
            break

# 方法三

for i in range(1, 10):
    for j in range(1, 10):
        print(j, "*", i, "=", i * j, end=" ")
        if i == j:
            print()
            break

# 方法四

for i in range(1, 10):
    for j in range(1, i + 1):
        print("{} * {} = {}".format(j, i, j * i), end=" ")
    print()

# 方法五

for i in range(1, 10):
    l = []
    for j in range(1, i + 1):
        l.append(str(j) + " * " + str(i) + " = " + str(i * j))
    print(" ".join(l))

