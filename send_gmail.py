#!/usr/bin/python
"""
asonste 27/jan-2016
Sends a gmail to a predefined email address
The definition "send_gmail" takes subject and body as arguments. 
Remember to define your username, password and email address in .conf file
Latest change: Added online status verification
"""
from conf import *
from aliveping import *
USERNAME = config.get('defult','USERNAME')# Get username from .conf file
PASSWORD = config.get('defult','PASSWORD')# Get password from .conf file
address = config.get('defult','address')# Get address from .conf file
from log import * # log.py needs to be in the same directory. Uncomment to disable logging. 
import smtplib
from email.mime.text import MIMEText
#-----------------------------------------------------
def send_gmail(subject, body,address=address):
    if pingweb() == "1":
       msg = MIMEText(body)
       msg['Subject'] = subject
       msg['From'] = USERNAME
       msg['To'] = address
       server = smtplib.SMTP('smtp.gmail.com:587')
       server.ehlo_or_helo_if_needed()
       server.starttls()
       server.ehlo_or_helo_if_needed()
       server.login(USERNAME, PASSWORD)
       server.sendmail(USERNAME, address, msg.as_string())
       server.quit()
       #--- Logging --- 
       text = ("Sendt mail to: %s, subject: %s, body: %s" %(address,subject,body))
       log(text) # Uncomment to disable logging
    elif pingweb() == "0": 
       text = ("Failed to send mail to: %s, subject: %s, body: %s" %(address,subject,body))
       log(text) # Uncomment to disable logging
#-----------------------------------------------------
# For testing
if __name__ == '__main__':
  print "Testing..."
  subject = "This is the email subject"
  body = "This is the email body"
  send_gmail(subject,body)
