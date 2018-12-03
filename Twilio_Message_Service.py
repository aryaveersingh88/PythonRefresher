# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 14:10:14 2018

@author: asingh368
"""

from twilio.rest import Client 

# Your Account SID and Auth token from twilio 
account_sid = "AC098abfc5f8b77ad99229fd05850852f6"
auth_token = "83bb253ab8475243e49f779ceb4b6e4c"

client = Client(account_sid, auth_token)

message = client.messages.create(
        body="Arya's first message!! Wozzaaaa", 
        to = "+12156054078",         #Phone number to which you want to send a message 
        from_ = "+16095545450")      #Your Twilio Account Number 

print(message.sid)
