# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 23:19:17 2017

@author: pavantej
"""

#!/bin/python3

import sys


S = input().strip()

i = 0
try:
    i = int(S)
    print (i)
except ValueError:
    print ('Bad String')
    
