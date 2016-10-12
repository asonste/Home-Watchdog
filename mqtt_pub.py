#!/usr/bin/python
"""
asonste 12/Oct.2016
mqtt publish utilities
"""
import paho.mqtt.client as mqtt
from conf import *
def pub_settings(var,HH,H,L,LL):
#Meant to be used for sending alarm limits to a sensor, when it connects.
   ip = config.get('mqtt','mqtt_broker_IP')
   mqttc = mqtt.Client("sim")
   mqttc.connect(ip, 1883, 60)
   mqttc.loop_start()
   topic = "%s_settings"%var
   settings = "%s,%s,%s,%s"%(HH,H,L,LL)
   mqttc.publish(topic,settings)
   mqttc.disconnect()

def pub(var,value):
# For publishing one or several values
   ip = config.get('mqtt','mqtt_broker_IP')
   mqttc = mqtt.Client("sim")
   mqttc.connect(ip, 1883, 60)
   mqttc.loop_start()
   topic = "%s"%var
   settings = "%s"%(value)
   #print topic
   mqttc.publish(topic,settings)
   mqttc.disconnect()

# For testing -------------------------------
if __name__ == "__main__":
#   pub_settings('sens1','32','30','7','3')
   pub('sens1','32.0')
