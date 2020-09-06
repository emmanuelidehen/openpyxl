#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 19:32:11 2020

@author: emmanuelidehen
"""
import numpy as np 
import statistics as st

x = [64630, 11735, 14216, 99233, 14470, 4978, 73429, 38120, 51135, 67060]

print (np.mean(x))
x = np.sort(x)
print (np.median(x))
print ((st.mode(x)))

