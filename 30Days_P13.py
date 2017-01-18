# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 23:16:29 2017

@author: pavantej
"""

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self, firstName, lastName, idNumber)
        self.scores = scores
    def calculate(self):
        avg_score = sum(self.scores) / (len(self.scores))
        if 90 <= avg_score <= 100:
            grade = 'O'
        elif 80 <= avg_score < 90:
            grade = 'E'
        elif 70 <= avg_score < 80:
            grade = 'A'
        elif 55 <= avg_score < 70:
            grade = 'P'
        elif 40 <= avg_score < 55:
            grade = 'D'
        elif avg_score < 40:
            grade = 'T'
            
        return grade 
        
   