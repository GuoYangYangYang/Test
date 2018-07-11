#!usr/bin/python
# -*- coding:UTF-8 -*-

# Python Test 013
"""
题目：打印出所有的"水仙花数"，
所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
例如：153是一个"水仙花数"，
因为153=1的三次方＋5的三次方＋3的三次方。
程序分析：利用for循环控制100-999个数，
每个数分解出个位，十位，百位。
"""

# 方法一

i, j, k = 0, 0, 0
for n in range(100, 1000):
    i = int(n / 100)
    j = int(n / 10 % 10)
    k = int(n % 10)
    if n == (i ** 3 + j ** 3 + k ** 3):
        print(n)

# 方法二

for x in range(1, 10):
    for y in range(0, 10):
        for z in range(0, 10):
            s1 = x * 100 + y * 10 + z
            s2 = pow(x, 3) + pow(y, 3) + pow (z, 3)
            if s1 == s2:
                print(s1)

# 方法三

for i in range(100, 1000):
    h = i // 100
    t = (i - 100 * h) // 10
    s = i - 100 * h - 10 * t
    if i == h ** 3 + t ** 3 + s ** 3:
        print(i)

# 方法四

l = [x ** 3 + y ** 3 + z ** 3
     for x in range(0, 10)
     for y in range(0, 10)
     for z in range(0, 10)
     if str(x) + str(y) + str(z) == str(x ** 3 + y ** 3 + z ** 3)]
print(l)

# 方法五

for n in range(100, 1000):
    m = n
    sumValue = 0
    while m > 0:
        m, r = divmod(m, 10)
        sumValue += r ** 3
    if n == sumValue:
        print(n)

# 方法六


def ppdi():
    # 生成器函数ppdi，可生成十进制自然数中的所有水仙花数，共有88个
    n = 3
    while 1:
        l = (i for i in range(10 ** (n - 1), 10 ** n)
             if sum([int(str(i)[j]) ** n for j in range(n)]) == i)
        yield l
        n += 1


def f(max):
    # 最大的水仙花数由39位
    for i in ppdi():
        for j in i:
            if j < 10 ** max:
                print(j)
            else:
                break
        if j > 10 ** max:
            break


f(3)
