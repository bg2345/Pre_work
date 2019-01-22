#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 23:06:33 2019

@author: bg
"""

def is_consecutive(a_list):
    i = 0
    for num in a_list:
        if num == a_list[i]:
            return True
        i = i + 1
    else:
            return False
    
print(is_consecutive([2,3,4,5,9,7]))