#!usr/bin/python
# -*- coding:UTF-8 -*-

# Python Test 011
"""
古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，
小兔子长到第三个月后每个月又生一对兔子，
假如兔子都不死，问每个月的兔子总数为多少？
程序分析：兔子的规律为数列1,1,2,3,5,8,13,21....
"""

# 方法一

f1, f2 = 1, 1
for i in range(1, 22):
    print('%12ld % 12ld' % (f1, f2), end=' ')
    if (i % 3) == 0:
        print()
    f1 = f1 + f2
    f2 = f1 + f2

# 方法二
# 用递归方法非常慢


def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(36))

# 方法三


def rabbit1(time, n):
    if time < 1:
        return 0
    elif time == 1:
        num = 1
    elif time < n:
        num = 1
    else:
        num = rabbit1(time - 1, n) + rabbit1(time - (n - 1), n)
    return num


print(rabbit1(36, 3))

# 方法四


def rabbit2(num):
    f1 = 1
    f2 = 1
    if num == 1 or num == 2:
        return 1
    else:
        for i in range(num - 1):
            f1, f2 = f2, f1 + f2
    return f1


print(rabbit2(36))

# 方法五


def rabbit3(n):
    count = [1, 0, 0]
    for i in range(1, n):
        count[2] = count[2] + count[1]
        count[1] = count[0]
        count[0] = count[2]
    return count[0] + count[1] + count[2]


print(rabbit3(36))

# 方法六


def rabbit4(num):
    i = 1
    a, b = 1, 1
    while i <= num:
        yield a
        i += 1
        a, b = b, a + b


list = [x for x in rabbit4(36)]
print(list)

# 方法七

Rabbits = {'rabbits': 0}
home = [{'rabbits': 1}]
month = 5
time = 1

while time < month:
    for j in home:
        if j['rabbits'] >= 2:
            home.append(Rabbits.copy())
        else:
            j['rabbits'] += 1
    time += 1

print(len(home))

# 方法八

a, b = 1, 1
for i in range(1, 35, 2):
    a += b
    b += a
print(b)

# 方法九


def rabbit9(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    rabbits = [1, 1]
    for i in range(2, n):
        rabbits.append(rabbits[-1] + rabbits[-2])
    return rabbits


print(rabbit9(18))

# 方法十

all_rabbit = []


class Rabbit():
    def __init__(self, birthday):
        self.birthday = birthday
        all_rabbit.append(self)

    def makechild(self, month):
        if month - self.birthday >= 2:
            Rabbit(month)


Rabbit(1)
for i in range(1, 22):
    [j.makechild(i) for j in all_rabbit[:]]
    print(len(all_rabbit), end=' ')
