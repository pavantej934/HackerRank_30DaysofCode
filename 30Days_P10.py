# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 23:14:42 2017

@author: pavantej
"""

n = int(input())

def factorial(N):
        if N <= 1:
            f = 1
        else:
            f = N*factorial(N-1)
        return f
    
print (factorial(n))