# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 23:11:15 2017

@author: pavantej
"""

#!/bin/python3

import sys


N = int(input().strip())

if (N % 2 != 0) or (N % 2 == 0 and 6<= N <= 20):
    print ("Weird")
elif (N % 2 == 0 and (2 <= N <= 5 or N > 20)):
    print ("Not Weird")
