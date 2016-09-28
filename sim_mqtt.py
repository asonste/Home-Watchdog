"""
asonste 28/Sept.2016
Will simulate a value, and send it on MQTT
"""
import paho.mqtt.client as mqtt # mosquitto.py is deprecated
import time

from usrinput import *

starttemp = int(usrinput("Enter start temp"))
dyntemp = starttemp
maxtemp = int(usrinput("Enter start maxtemp"))

mqttc = mqtt.Client("sim1")
mqttc.connect("127.0.0.1", 1883, 60)
#mqttc.subscribe("test/", 2) # Not needed unless you include a subscribe callback
mqttc.loop_start()

topic = "ha/_temperature1"

while True:
    mqttc.publish(topic,dyntemp)
    print dyntemp
    time.sleep(1)# sleep for 1 second
    if dyntemp < maxtemp:
       dyntemp = dyntemp + 1
    else:
       while dyntemp > starttemp:
          dyntemp = dyntemp - 1
          mqttc.publish(topic,dyntemp) 
          print dyntemp
          time.sleep(1)# sleep for 1 second
