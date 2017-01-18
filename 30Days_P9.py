# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 23:14:09 2017

@author: pavantej
"""

n = int(input())

phone_book = {}
for i in range(n):
    key_value = (input().split())
    phone_book[key_value[0]] = key_value[1]

#print (phone_book)

while True:
    try:
        key = input()
        #print (key)
        if key in phone_book:
            #print ('true')
            print (key + '=' + phone_book[key])
        else:
            print ('Not found')
    except:
        break