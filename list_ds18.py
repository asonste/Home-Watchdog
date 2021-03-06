#/usr/bin/python
"""
asonste 31/Oct.2016
For listing IDs of the ds18b20 sensors connected to the Raspberry Pi
Latest change: Added while loop for easy faut finding wiring issues.
"""
import os
import time
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
base_dir = '/sys/bus/w1/devices/'

def get_IDs():
   path, dirs, files = os.walk(base_dir).next()
   dir_count = len(dirs)-1
   count = -1
   all_ID = []
   for f in dirs:
     count = count + 1
     name = dirs[count]
     pos = name.find('28-')
     if pos != -1:
       all_ID.append(name)
   return all_ID

#--- For testing -------------
if __name__ == '__main__':
   IDs = get_IDs()
   print "Number of sensors: " + str(len(IDs))
   print IDs
   while len(IDs) < 1:
      print IDs
      time.sleep(3)
