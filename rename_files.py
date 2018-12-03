# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 22:37:12 2018

@author: asingh368
"""
import os 

def rename_files():
    #(1) get the filenames from a given folder
    
    file_list = os.listdir(r"C:\Users\asingh368\Desktop\Learning\Python Refresher\prank")
    #print(file_list)
    saved_path = os.getcwd()
    print(saved_path)
    os.chdir(r"C:\Users\asingh368\Desktop\Learning\Python Refresher\prank")
    print(os.getcwd())
    #(2) Change the name of each file 
    table = str.maketrans(dict.fromkeys('0123456789'))
    for file_name in file_list:
        os.rename(file_name, file_name.translate(table))
        
        
    os.chdir(r'C:\Users\asingh368\Desktop\Learning\Python Refresher')
    print(os.getcwd())
    
    return # 


rename_files()