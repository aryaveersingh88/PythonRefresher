# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 01:34:44 2018

@author: asingh368
"""

class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent Class Constructor called")
        self.last_name = last_name
        self.eye_color = eye_color
        
billy_cyrus = Parent("Cyrus", "Blue")

print(billy_cyrus.last_name)