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
        
    def show_info(self):
        print("Last Name - "+self.last_name)
        print("Eye Color - "+self.eye_color)
        
#billy_cyrus = Parent("Cyrus", "Blue")

#print(billy_cyrus.last_name)
        
class Child(Parent):
    
    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child Constructor called")
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys
        
    def show_info(self):
        print("Last Name - "+self.last_name)
        print("Eye Color - "+self.eye_color)
        print("number of toys - "+str(self.number_of_toys))
        
        
miley_cyrus = Child("Cyrus", "Blue", 5)
#print(miley_cyrus.last_name)
miley_cyrus.show_info()
#print(miley_cyrus.number_of_toys)