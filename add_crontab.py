#!/usr/bin/env python
"""
asonste 13/Nov.2016
For adding crontab that wil run every minute
"""
import os
from conf import *

user = config.get('defult','user')         # Get user from conf file
base_dir = config.get('defult','base_dir') # Get base directory from conf file

def add_crontab(program,base_dir,file,sens,user):
   # for adding crontab that wil run every minute
   ncrontab = ("* * * * * %s %s/%s %s"%(program,base_dir,file,sens))
   print ncrontab
   cmd = ("crontab -u %s -l | grep -q '%s'  && echo 'entry exists' || crontab -u %s -l | { cat; echo '%s > /dev/null 2>&1';} | crontab -u %s -"%(user,sens,user,ncrontab,user))
   os.system(cmd)

if __name__ == "__main__":
   program = 'python'
   #sens = 'sens1'
   #file = 'pi_ds18_mqtt.py'
   #add_crontab(program,base_dir,file,sens,user)

