#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 19:32:11 2020

@author: emmanuelidehen
"""

from collections import Counter 



x = [64630, 11735, 14216, 99233, 14470, 4978, 73429, 38120, 51135, 67060]
m = len(x) 
  
get_sum = sum(x) 
mean = get_sum / m 

n = len(x) 
x.sort() 
  
if n % 2 == 0: 
    median1 = x[n//2] 
    median2 = x[n//2 - 1] 
    median = (median1 + median2)/2
else: 
    median = x[n//2]

def mode():
    for i in x:
        if (i+1 == i):
            return x
        else:
            return x[0]

print(str(mean))
print(str(median))
print(mode())
