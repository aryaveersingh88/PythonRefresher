# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 14:10:14 2018

@author: asingh368
"""

from twilio.rest import Client 

# Your Account SID and Auth token from twilio 
account_sid = "" #Add account SID token here 
auth_token = "" #Add authorization token here 

# Both the above account SID and Auth token available on Twilio Homepage of the application you created 

client = Client(account_sid, auth_token)

message = client.messages.create(
        body="Arya's first message!! Wozzaaaa", 
        to = "", #Add the number you want to send the text to 
        from_ = "") #Add the twilio phone number here 

print(message.sid)
