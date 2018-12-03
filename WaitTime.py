# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 22:17:26 2018

@author: asingh368
"""
import time
import webbrowser

total_breaks =1 
break_count = 0 

print("This program has started "+time.ctime())
#for i in range(3):
while(break_count < total_breaks):
    time.sleep(2)
    webbrowser.open("https://www.youtube.com/watch?v=3--bmwOhGHU")
    break_count = break_count + 1 

