#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 22:27:30 2019

@author: bg
"""

def max_num_in_list(a_list):
    max_num = 0
    for i in a_list:
        if i > max_num:
            max_num = i
    print(max_num)
    
max_num_in_list([1,3,4,222,6,3,77,3,55])