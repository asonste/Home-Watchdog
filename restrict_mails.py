#!/usr/bin/python
'''
asonste 30/Sept-2016
To be run from chrontab at midtight
For preventing a huge bunch of emails
'''
from log import *
from conf import *
from send_gmail import *

def restrict():
   allow_send_gmails = config.get('email','allow_send_gmails')
   if  allow_send_gmails != "0": # Check if it is already disabled
      no_of_gmails = config.get('email','no_of_gmails_sent') # Number of emails sent
      max_no_of_mails_pr_day = config.get('email','max_no_of_mails_pr_day')# Max limit
      if int(no_of_gmails) >= int(max_no_of_mails_pr_day): # Check if the max limit has been reached
         send_gmail('Max number of gmails reached','Sending emails disabled')
         #log("Emails automaticly disabeled") # Log to logfile
         write_config('email','allow_send_gmails','0')# Disable emails

if __name__ == '__main__':
   restrict()
