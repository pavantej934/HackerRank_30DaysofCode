# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 23:13:26 2017

@author: pavantej
"""

#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

print (' '.join(map(str,arr[::-1])))
    
