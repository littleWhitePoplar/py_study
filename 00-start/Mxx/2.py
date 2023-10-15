#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 22:07:46 2023

@author: mengxiaoqian
"""

# 2.定义三个变量，交换它们的值并打印所有可能性
a = 1
b = 2
c = 3
print(a,b,c)
new_a = a
new_b = b
new_c = c
# 交换b和c
temp = new_b
new_b = new_c
new_c = temp
print(a,b,c)
