#!/usr/bin/env python
##&/ -*- coding: latin-1 -*-
##/ -*- coding: utf-8 -*-
"""
asonste 12/Oct.2016
For reading sensor connected to pi and send value on mqtt
Note: script is to be run with sensor name as defined in .conf file as argument
"""
from datetime import datetime, timedelta
from mqtt_pub import *
import time
import sys
name = str(sys.argv[1]) # Script to be run with sensor name as argument

delay = int(name[-1])*5
time.sleep(delay)

from log import log, dateandtime
from conf import *
from read_single import *
id = config.get(name,'id')
broker_IP = config.get('mqtt','mqtt_broker_IP')# Get username from .conf file
#-------------------------------------------
def isfloat(value): # Verify that value is float
  try:
    float(value)
    return True
  except ValueError:
    return False

def on_connect():
  text = ("Pi DS18 connected to %s"%(name))
  log(text)

def on_message():
  str_temp = gettemp(id)
  if isfloat(str_temp):
     temp = float(str_temp)
     if temp != 85.0: # Some times sensor gives a incorrect reading of 85. If statemetn is for filtering it out.
        if __name__ == "__main__":
           os.system("clear")
           print temp
           pub(name,temp)

on_connect()
on_message()
