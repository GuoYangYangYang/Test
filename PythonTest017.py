#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Python Test 017
"""
输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
"""


import re

# 方法一

s = "Hello!world!12345~  24678~~~潘国阳"
letters, space, digit, others = 0, 0, 0, 0
i = 0
while i < len(s):
    c = s[i]
    i += 1
    if c.isalpha():
        letters += 1
    elif c.isspace():
        space += 1
    elif c.isdigit():
        digit += 1
    else:
        others += 1
print(letters, space, digit, others)

# 方法二

letters, space, digit, others = 0, 0, 0, 0
for c in s :
    if c.isalpha():
        letters += 1
    elif c.isspace():
        space += 1
    elif c.isdigit():
        digit += 1
    else:
        others += 1
print(letters, space, digit, others)

# 方法三

Letters, Spaces, Digits, Others = [], [], [], []
for i in iter(s):
    if i.isalpha():
        Letters.append(i)
    elif i.isspace():
        Spaces.append(i)
    elif i.isdigit():
        Digits.append(i)
    else:
        Others.append(i)
print("{} {} {} {}".format(len(Letters), len(Spaces), len(Digits), len(Others)))

# 方法四
# 正则表达式

tmpStr = s
charNum = 0
digNum = 0
spaceNum = 0
otherNum = 0
for i in range(len(tmpStr)):
    if re.match('\d', tmpStr[i]):
        digNum += 1
    elif re.match('[a-zA-Z]', tmpStr[i]):
        charNum += 1
    elif re.match('\s', tmpStr[i]):
        spaceNum += 1
    else:
        otherNum += 1
print(charNum, spaceNum, digNum, otherNum)

# 方法五

# 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
# 不能有效区分汉字。。。好像没有特定识别汉字的通用表达\s这样的#4E00～9FFFh 是中文的数字区域

char = re.findall(r'[a-zA-Z]', s)
num = re.findall(r'[0-9]', s)
blank = re.findall(r' ', s)
chi = re.findall(r'[\u4E00-\u9FFF]', s)
other = len(s)-len(char)-len(num)-len(blank)-len(chi)
print("字母：", len(char),
      "\n数字：", len(num),
      "\n空格：", len(blank),
      "\n中文：", len(chi),
      "\n其他：", other)
