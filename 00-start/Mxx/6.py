#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 23:10:20 2023

@author: mengxiaoqian
"""

# 6.打印5以内的乘法表
for a in range (1,6):
    for b in range (1,a+1):
        print(f"{a}*{b}={a*b}\t",end='')
    print()