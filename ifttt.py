#!/usr/bin/python
"""
asonste 30/Aug-2016
For use with the ifttt maker chanel. Can be used to send up to three values.
The script will check the conf file if ifttt is enabled, and count how many times each event is triggered.
"""
import requests
from conf import *
from log import *
ifttt_key = config.get('ifttt','ifttt_key')# Get ifttt key from .conf file

def ifttt(event,value1="1",value2="2",value3="3",key=ifttt_key):
   values = {}
   values["value1"] = value1
   values["value2"] = value2
   values["value3"] = value3
   if config.get('ifttt','allow_ifttt') == "1": # Check if ifttt is allowed
     #Counting how many times the event has been triggered
      check_option("ifttt",event)
      if config.get('ifttt',event) == "":
         write_config('ifttt',event,"1")
      else:
         count = int(config.get('ifttt',event))
         count = count + 1
         write_config('ifttt',event,count)
      requests.post("https://maker.ifttt.com/trigger/%s/with/key/%s/"%(ifttt_event_name,key), data=values)
      log("IFTTT Triggered with event: %s, value1: %s, value2: %s ,value3: %s "%(event,value1,value2,value3))
#-----------------------------------------------------
# For testing
if __name__ == '__main__':
   print "Testing..."
   ifttt_event_name = "temp_Alert"
   #ifttt(ifttt_event_name,"one","two","three")
   ifttt(ifttt_event_name,"one")
