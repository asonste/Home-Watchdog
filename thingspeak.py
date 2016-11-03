#!/usr/bin/python
"""
asonste 03/Nov.2016
For posting values to thingspeak.
Latast change: Adapted for searching for sens*.txt files, for new values, then post to thingspeak.
It has been tested with three sensors, 
but it should work with the maximum number of sensors that thingspeak will handle
"""
import sys
import urllib2
from conf import *
import time
from readfile import *
from writefile import *
#time.sleep(50) # Wait until sensors are read
key =  config.get('thingspeak','thingspeak_key') # Get thingspeak key from .conf file
import glob

def make_post_string(vals,sens_numbers):
# Combine information in to a common string, for posting all values at the same time.
# Thingspeak is limited to one post every 20 second, so it is better to post many values at the same time 
   count = 0
   poststring = []
   for s in vals:
      if vals[count]!= None:
         #print 'Adding to string...'
         poststring.append('&field%s=%s'%(sens_numbers[count],vals[count]))
      count = count + 1
   return ''.join(poststring)

def thingspeak(key,poststring):
# For doing the Thingspeak post
   baseURL = ('https://api.thingspeak.com/update?api_key=%s'%key)
   f = urllib2.urlopen(baseURL + "%s"%poststring)
   print f.read()
   f.close()

def currentvals(no):
# Get the measured value from the sensor text file
   txtfile_path = ('%s/%s.txt'%(base_dir,no))
   varslist = readvars(txtfile_path)
   singlevars = varslist[0]
   singlevars2=singlevars.split(',')
   a = singlevars2[0] # Value
   b = singlevars2[1] # Status
   #c = singlevars2[2]# Time of measurement. Add a time check/verification later? 
   if b == 'newtemp': # Check if the value in the text file is new
      writefile('no_value,no_value',txtfile_path) # Reset value and status after it is read 
      return a

#while 1 == 1: # For running as a loop
if 1 ==1: # For funning one time
   vals = []
   sens_numbers = []
   sensorfiles = glob.glob('%s/sens*.txt'%base_dir) # List all sens*.txt files in the base dir
   count = 0
   for i in sensorfiles:
      sens = sensorfiles[count]
      sensparts = sens.split('.')                        # split the .txt form the end
      sensparts2 = sensparts[0].split('/')               # Split in dir.
      sensname_pos = len(sensparts2)-1                   # Position of sensor name. One pos from the end
      sensor_number = sensparts2[sensname_pos].split('sens') # Split to get the sensor number
      sens_numbers.append(sensor_number[1])              # Make a list of sensor numbers
      vals.append(currentvals(sensparts2[sensname_pos])) # Make a list of values
      count = count + 1
   post_string = make_post_string(vals,sens_numbers)
   #if __name__ == '__main__':
   print "Values: " + str(vals)      # For debugging
     # print "Statuses: "+ str(stat) # For debugging
   print post_string
      #print "Post string length:" + str(len(post_string))
   if len(post_string) != 0: # Only post if there is something to post
      thingspeak(key,post_string)
