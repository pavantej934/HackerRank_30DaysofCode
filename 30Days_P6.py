# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 23:12:37 2017

@author: pavantej
"""

#!/bin/python3

import sys


n = int(input().strip())

for i in range(1,11):
    print (str(n) + ' x ' + str(i) + ' = ' + str(n*i))
