#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Python Test 006
"""
斐波那契数列（Fibonacci sequence），又称黄金分割数列，
指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
"""

# 方法一


def fib1(n):
    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a + b
    return a


print(fib1(10))

# 方法二：利用递归


def fib2(n):
    if n == 1 or n == 2:
        return 1
    return fib2(n - 1) + fib2(n - 2)


print(fib2(10))

# 方法三


def fib3(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    fibs = [1, 1]
    for i in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs


print(fib3(10))

# 方法四

n = 10
print(int((1/(5**0.5))*(((1+(5**0.5))/2)**n - ((1-(5**0.5))/2)**n)))

# 方法五：生成器


def fib5(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1


max = 10
for n in fib5(max):
    print(n, '', end='')
print()

# 方法六


class Fibs:
    def __init__(self, n = 10):
        self.a = 0
        self.b = 1
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        self.i += 1
        if self.i > self.n:
            raise StopIteration
        return self.a


fibs = Fibs(10)
for i in fibs:
    print(i, '', end='')
print()

# 方法七

fe_list = [0, 1]
for i in range(1, 11):
    fe_list.append(sum(fe_list[(i - 1):(i + 1)]))
print(fe_list)
