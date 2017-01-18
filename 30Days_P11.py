# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 23:15:16 2017

@author: pavantej
"""

#!/bin/python3

import sys


n = int(input().strip())

bin_n = bin(n)[2:]

count = 0
cnt_l = []

for i in bin_n:
    if int(i) == 1:
        count += 1
    else:
        cnt_l.append(count)
        count = 0

cnt_l.append(count)
print (max(cnt_l))
         
