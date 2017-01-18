# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 23:10:16 2017

@author: pavantej
"""

meal_cost = float(input())
tip_percent = int(input())
tax_percent = int(input())

total_cost =  meal_cost + (tip_percent*meal_cost/100) + (tax_percent*meal_cost/100)
total_cost = round(total_cost)
    
print ('The total meal cost is ' + str(total_cost) + ' dollars.')
