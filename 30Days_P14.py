# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 23:17:07 2017

@author: pavantej
"""

#Write MyBook class
class MyBook(Book):
    def __init__(self,title,author,price):
        Book.__init__(self,title,author)
        self.price = price
    def display(self):
        print ('Title: ' + self.title)
        print ('Author: ' + self.author)
        print ('Price: ' + str(self.price))
        
