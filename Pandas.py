#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 15:04:19 2020

@author: emmanuelidehen
"""

import numpy as np, pandas as pd

data = {'color' : ['blue','green','yellow','red','white'],
'object' : ['ball','pen','pencil','paper','mug'],
'price' : [1.2,1.0,0.6,0.9,1.7]}

frame=pd.DataFrame(data)
print(frame)
frame2 = pd.DataFrame(data, columns=['object','price'])
print(frame2)
frame3 = pd.DataFrame(data, index=['one','two','three','four','five'])
print(frame3)