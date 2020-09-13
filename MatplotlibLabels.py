#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 17:35:04 2020

@author: emmanuelidehen
"""
import numpy as np 
import matplotlib.pyplot as plt

x = np.array ([1,2,3,4,5])
y = np.array ([6,7,8,9,10])

plt.xlabel('population')
plt.ylabel('temp')
"""
this is the only way to do multiple line 
comment is python lol ..
plt.Arrow(x, y)
"""
plt.title('population distribution')


plot = plt.scatter(x,y)
plt.show(plot)

