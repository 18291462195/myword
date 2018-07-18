#!/user/bin/env python
#!-*-coding:utf-8 -*-
#!@Author : gexianyu

t='5k-12k'
s = t.replace('k','').split('-')
avg = (int(s[0])+int(s[1]))/2
print(avg)

