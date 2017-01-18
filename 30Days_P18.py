# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 00:49:50 2017

@author: pavantej
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class solution:
    def display(self,head):
        current = head
        while current:
            print (current.data, end = '')
            current = current.next
    def insert(self,head,data):
        if (head == None):
            head = Node(data)
        elif (head.next == None):
            head.next = Node(data)
        else:
            self.insert(head.next,data)
        return head
        
mylist = solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head,data)
mylist.display(head)