# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 23:12:48 2017

@author: pavantej
"""

N = int(input())

for i in range(N):
    S = input()
    print (S[0:len(S):2] , S[1:len(S):2])