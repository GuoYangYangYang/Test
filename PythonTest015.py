#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Python Test 015
"""
题目：利用条件运算符的嵌套来完成此题：
学习成绩>=90分的同学用A表示，60-89分之间的用B表示，
60分以下的用C表示。
程序分析：程序分析：(a>b)?a:b这是条件运算符的基本例子。
"""

# 方法一

score = 89

if score >= 90:
    grade = 'A'
elif score >= 60:
    grade = 'B'
else:
    grade = 'C'
print(grade)

# 方法二

i = score
ar = [90, 60, 0]
res = ['A', 'B', 'C']
for idx in range (0,3):
    if i >= ar[idx]:
        print(res[idx])
        break

# 方法三

print(['C', 'C', 'B', 'A'][int(score / 30)])
