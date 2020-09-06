#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 13:55:39 2020

@author: emmanuelidehen
"""

import numpy as np 
#firstfrom z = (x-u)/s we can scale our variable to be able to compare them. 
var = [2300, 1.3]#giving paramenter of weight = 2300kg and volume = 1.3 litter 
#from the previous experiment we compared volume in ccm and weight in Kg 
u = np.mean(var)
s = np.std(var)

print (u)
print (s)
