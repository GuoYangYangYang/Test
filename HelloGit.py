#!usr/bin/python
# -*- coding: UTF-8 -*-

import matplotlib.pyplot as plt

class Person:
    height = 140

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.__weight = weight

    def speak(self):
        print("%s 说: 我 %d 岁，我体重为 %d Kg。身高为 %d cm" % (self.name, self.age, self.__weight, Person.height))


class Student(Person):
    grad = ''

    def __init__(self, name, age, weight, grad):
        Person.__init__(self, name, age, weight)
        self.grade = grad

    def speak(self):
        print("%s 说：我 %d 岁了，我在读 %d 年级" %(self.name, self.age, self.grade))


stu = Student('Alice', 10, 40, 3)
stu.speak()


# 定义求均值的函数


def mean(values):
    return sum(values) / float(len(values))

# 计算求方差的函数


def variance(values, mean):
    return sum([(x - mean) ** 2 for x in values])

# 计算x与y协方差的函数


def covariance(x, mean_x, y, mean_y):
    covar = 0.0
    for i in range(len(x)):
        covar += (x[i] - mean_x) * (y[i] - mean_y)
    return covar

# 开始计算均值和方差

dataset = [[1.2, 1.1], [2.4, 3.5], [4.1, 3.2], [3.4, 2.8], [5, 5.4]]
x = [row[0] for row in dataset]
y = [row[1] for row in dataset]
print(x)
print(y)
mean_x, mean_y = mean(x), mean(y)
var_x, var_y = variance(x, mean_x), variance(y, mean_y)
print('x 的统计特性：均值 = %.3f 方差 = %.3f' % (mean_x, var_x))
print('y 的统计特性：均值 = %.3f 方差 = %.3f' % (mean_y, var_y))
covar = covariance(x, mean_x, y, mean_y)
print('协方差 = ：%.3f' % (covar))