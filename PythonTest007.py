#!usr/bin/python
# -*- coding:UTF-8 -*-

# Python Test 007
"""
使用列表[:]，将一个列表的数据复制到另一个列表中
注意使用[:]复制（浅拷贝）列表时b改变a不改变
而使用b = a复制（深拷贝）时传的是地址，b改变a照样改变
"""

# 方法一

a = [1, 2, 3]
b = a[:]
print(b)

# 方法二

a = [1, 2, 3]
b = a.copy()
print(b)

# 方法三

a = [1, 2, 3]
p = []
for i in range(len(a)):
    p.append(a[i])
print(p)

# 方法四

a = [1, 2, 3]
b = [i for i in a]
print(b)

# 方法五

a = [1, 2, 3]
b = list()
for i in a:
    b.append(i)
print(b)

# 方法六

a = [1, 2, 3]
b = []
b.extend(a)
print(b)
