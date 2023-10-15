#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 23:20:19 2023

@author: mengxiaoqian
"""

# 7.编写一个程序，转换人名币和美元，结果保留两位小数
#print("%.2f" % a) #%代表格式化输出，.2代表小数点后保留两位，f代表数据类型是浮点型
R = 50
D = 20
Dollar = R * 7.30
Rmb = D / 7.30
print (f"{Dollar:.2f} {Rmb:.2f}")
