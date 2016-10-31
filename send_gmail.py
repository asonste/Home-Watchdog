#!/usr/bin/python
"""
asonste 29/Oct-2016
Sends a gmail to a predefined email address
The definition "send_gmail" takes subject and body as arguments. 
Remember to define your username, password and email address in .conf file
Latest change: Modified so that allow gmail will be checked before pingweb is run.
"""
from conf import *
from aliveping import *
USERNAME = config.get('email','USERNAME')# Get username from .conf file
PASSWORD = config.get('email','PASSWORD')# Get password from .conf file
address = config.get('email','address')# Get address from .conf file
allow_send_gmails = config.get('email','allow_send_gmails')
no_of_gmails = config.get('email','no_of_gmails_sent')
from log import * # log.py needs to be in the same directory. Uncomment to disable logging. 
import smtplib
from email.mime.text import MIMEText
count = 0
#-----------------------------------------------------	
def send_gmail(subject, body,address=address):
    if allow_send_gmails == "1":
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
          count = int(no_of_gmails) + 1
          write_config('email','no_of_gmails_sent',str(count))
       elif pingweb() == "0": 
          text = ("No network connection. Failed to send mail to: %s, subject: %s, body: %s" %(address,subject,body))
          log(text) # Uncomment to disable logging
       else:
          text = ("Mails disabled. Failed to send mail to: %s, subject: %s, body: %s" %(address,subject,body))
          log(text)
#-----------------------------------------------------
# For testing
if __name__ == '__main__':
  print "Testing..."
  subject = "This is the email subject"
  body = "This is the email body"
  send_gmail(subject,body)
