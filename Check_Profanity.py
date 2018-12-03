# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 18:03:53 2018

@author: asingh368
"""

import urllib.request
import urllib.parse

def read_text():
    quotes = open(r"C:\Users\asingh368\Desktop\Learning\Python Refresher\Profanity_Check.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)
    
def check_profanity(text_to_check):
    connection = urllib.request.urlopen("http://www.wdylike.appspot.com/?" + urllib.parse.urlencode([('q', text_to_check)]))
    #connection = urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    print(output)
    connection.close()
    
    if 'true' in str(output):
        print("Prfanity Alert!!!")
    else:
        print("This document has no curse words")
    

    
read_text()
