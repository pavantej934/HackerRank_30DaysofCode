# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 23:15:51 2017

@author: pavantej
"""

#!/bin/python3

import sys


arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)

arr_hg_sum = []
for i in range(4):
    for j in range(4):
        arr_hg_sum.append(arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2])

print (max(arr_hg_sum))
