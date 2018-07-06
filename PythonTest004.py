#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Python Test 004
"""
输入某年某月某日，判断这一天是这一年的第几天？
"""

# 方法一

year = int(input("year: "))
month = int(input("month: "))
day = int(input("day: "))
sum = 0

months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
if 0 < month <= 12:
    sum = months[month - 1]
sum += day
leap = 0
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    if month > 2:
        sum += 1
print(sum)
