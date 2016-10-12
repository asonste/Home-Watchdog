#!/usr/bin/env python
##&/ -*- coding: latin-1 -*-
##/ -*- coding: utf-8 -*-
"""
asonste 12/Oct.2016
Main script for reading MQTT values, and acting on them.
Note: script is to be run with sensor name as defined in .conf file as argument
"""
from log import log, dateandtime
from conf import *
from measure import * # Class for treating the measurement. Will determine alarms etc
from sens_settings import * # Class for sensor variables and settings
from datetime import datetime, timedelta
from writefile import *
import paho.mqtt.client as mqtt
from mqtt_pub import *
import sys
from send_gmail import *
s = str(sys.argv[1]) # Script to be run with sensor name as argument
s = sens(s) # Set s as settings class
s.update()

broker_IP = config.get('mqtt','mqtt_broker_IP')# Get username from .conf file
#------------------------------------------------
g = measure(s.HH,s.H,s.LL,s.L,1,0,s.name,0,0,0,0,50,0) #Set g as measurement class

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

#This is the Subscriber
def on_connect(client, userdata, flags, rc):
  #pub_settings(s.var,s.HH,s.H,s.L,s.LL)#Send settings to the sensor
  text = ("MQTT Connected to %s with result code %s"%(s.var,str(rc)))
  log(text)
  client.subscribe(s.var)

prevalarm = "none"
def on_message(client, userdata, msg):
  str_temp = msg.payload
  print str_temp
  if isfloat(str_temp):
     temp = float(str_temp)
     if temp != 20.44: # For some reason 20.44 chows up as first message. If statemet is for filtering it out.
        g.update(temp,1)# 1 is the bias. (Static/not used)
        writefile('%s,newtemp'%(temp),'/home/pi/Documents/Home-Watchdog/%s.txt'%s.var)
        write_config(s.var,'last-alive-time',dateandtime())
        if __name__ == "__main__":
           os.system("clear")
           print_alarms(g)
           print ("Last alive time: %s"%dateandtime())
        if "none_new" in g.alarm:
           text = "Reset alarm %s on sensor %s. Temp: %s"%(config.get(s.var,'stat'),s.name,temp)
           log(text)
           write_config(s.var,'stat','ok')
        elif "new" in g.alarm:
           if not "alarm" in config.get(s.var,'stat'):
              text = "Alarm %s on sensor %s"%(g.alarm,s.name)
              log(text)
              send_gmail(text,str(temp))
              write_config(s.var,'trigg-time',dateandtime())
              write_config(s.var,'stat','%s'%g.alarm)
  if (msg.payload == "Lims accepted"):
    text = "%s accepted the limits"%(s.var)
    log(text)

client = mqtt.Client()
client.connect(broker_IP,1883,60)
client.on_connect = on_connect
client.on_message = on_message
client.loop_forever()
