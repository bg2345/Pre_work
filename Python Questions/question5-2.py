#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 23:38:38 2019

@author: bg
"""

def is_consecutive(a_list):
    i = 0
    size_of_list = len(a_list)
    while (i < size_of_list):
        if (a_list[i] + 1 == a_list[i + 1]):
            return True
        else:
            return False
        i = i + 1
        
print(is_consecutive([2,3,4,5,6,7,8]))