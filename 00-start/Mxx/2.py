#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 22:07:46 2023

@author: mengxiaoqian
"""

# 2.定义三个变量，交换它们的值并打印所有可能性

A = 1
B = 2
C = 3
print ("Before exchange: ", A,B,C)
D = A
A = B
B = C
C = D
print("After exchange: ", A,B,C)
