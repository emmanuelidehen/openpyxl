#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 14:30:47 2020

@author: emmanuelidehen
"""

import pandas as pd
import numpy as np
#We load and explore the data with the following commands:
    #place your file location here!
x = '/Users/emmanuelidehen/OneDrive - Mississippi Valley State University/Python files/melb_data.csv'
y = pd.read_csv(x) #read the data into y with .read_csv and pass file path
y.describe()  #use the .describe to print out data 

#playing with 2d arrays 

#Data types in Numpy 
#i - integer
#b - boolean
#u - unsigned integer
#f - float
#c - complex float
#m - timedelta
#M - datetime
#O - object
#S - string
#U - unicode string
#V - fixed chunk of memory for other type ( void )

array = np.array([[[0,1,2],[3,4,5]],[[6,7,8],[9,10,11]]])
for x,y in array:
   print(x)
   print(y)
   print(".............")
class addiction:
    
    x = array[0,0]
    y = array[1,0]
    z = array[0,1]
    g = array[1,1]
    
   # a = x[0] + x[1] + x[2]
    print(y)
    print("....................")
    sum = x + y
    print (sum)