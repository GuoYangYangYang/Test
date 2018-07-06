#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Python Test 003
"""
一个整数，它加上100后是一个完全平方数，
再加上168又是一个完全平方数，请问该数是多少？
"""

"""
假设该数为 x。
1、则：x + 100 = n2, x + 100 + 168 = m2
2、计算等式：m2 - n2 = (m + n)(m - n) = 168
3、设置： m + n = i，m - n = j，i * j =168，i 和 j 至少一个是偶数
4、可得： m = (i + j) / 2， n = (i - j) / 2，i 和 j 要么都是偶数，要么都是奇数。
5、从 3 和 4 推导可知道，i 与 j 均是大于等于 2 的偶数。
6、由于 i * j = 168， j>=2，则 1 < i < 168 / 2 + 1。
7、接下来将 i 的所有数字循环计算即可。
"""

# 方法一

for i in range(1, 85):
    if 168 % i == 0:
        j = 168 / i
        if i > j and (i + j) % 2 == 0 and (i - j) % 2 == 0:
            m = (i + j) / 2
            n = (i - j) / 2
            x = n * n - 100
            print(x, "", end="")
print()

# 方法二

"""
设该数为x：x + 100 = n^2, n^2 + 168 = m^2。
设m=n+k（不妨设m,n,k均为自然数）：带入m^2-n^2-168，
得k^2+2nk=168。
解得n=84/k - k/2；由于n,k均为自然数，
则nk>=1，故1<=k^2<168，故1<=k<=12。
"""

for x in range(1, 13):
    a = 84 / x - x / 2
    if int(a) == a:
        n = a ** 2 - 100
        print(n, "", end="")
print()

# 方法三

for i in range(1, 85):
    if 168 % i == 0 :
        j = 168 / i
        if i > j:
            m = (i + j) / 2
            n = (i - j) / 2
            if m * m - 268 == n * n - 100 and \
                    (n * n - 100) % 1 == 0:
                print(m * m - 268, "", end="")
print()

# 方法四

i = 1
# 先求最大范围
while ((i + 1) * (i + 1) - i * i) <= 168:
    i += 1
# 循环测试
for j in range(1, i):
    for k in range(1, i):
        if (k * k - j * j) == 168:
            print(k * k - 268, "", end="")
print()

# 方法五

print([n ** 2 - 100 for m in range(168) for n in range(m) \
       if (m + n) * (m - n) == 168])

# 方法六
"""
因为题目说明x是整数，但没有说明n和m一定大于零，
此处考虑了n和m小于零的情形
x+100=n^2;x+100+168=m^2;(注意，没有要求m,n一定大于零)
m^2-n^2=168 即 (m+n)(m-n)=168;
设 m+n=i,m-n=j,则m=(i+j)/2;n=(i-j)/2 有 i*j=168, 
因为 m,n 都是整数且 m!=n, 所以 j,i!=0, 因为i*j是正数，
故 abs(i)>=1,abs(j)>=1。所以i和j的上限可以取 168。
因此m和n的上限也是168,下限可以取-168
（注意，m,n的取值范围可以放得很大，不影响结果，
因为限制条件可以自己去约束，但所取的范围一定要比真实范围大）
"""
x = []
for m in range(-168, 169):
    for n in range(-168, 169):
        if (m + n) * (m - n) == 168:
            x.append(n ** 2 - 100)
x = set(x)
x = list(x)
print(x)
