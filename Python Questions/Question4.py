#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 22:40:50 2019

@author: bg
"""

def is_leap_year(a_year):
   if a_year % 400 == 0:
       return True
   if a_year % 100 == 0:
       return False
   if a_year % 4 == 0:
       return True
   else:
       return False
        
    
print(is_leap_year(2020))

