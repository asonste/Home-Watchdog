#!/usr/bin/python
"""
asonste 12/Nov.2016
For posting reading values from sens.txt files and
creating post string for emoncms and thingspeak.
Latast change: split thingspeak post to separate file, add emoncms
"""
import glob
from readfile import *
from writefile import *
from emoncms import *
from thingspeak import *

def make_thingspeak_post_string(vals,sens_numbers):
# Combine information in to a common string, for posting all values at the same time.
# Thingspeak is limited to one post every 20 second, so it is better to post many values at the same time 
   count = 0
   poststring = []
   for s in vals:
      if vals[count]!= None:
         poststring.append('&field%s=%s'%(sens_numbers[count],vals[count]))
      count = count + 1
   return ''.join(poststring)

def make_emoncms_post_string(vals,sens_numbers):
# Combine information in to a common string, for posting all values at the same tim$
   count = 0
   poststring = []
   for s in vals:
      if vals[count]!= None:
         if count != 0:
            poststring.append(',')
         poststring.append('sens%s:%s'%(sens_numbers[count],vals[count]))
      count = count + 1
   return ''.join(poststring)

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
if 1 ==1:      # For funning one time
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
   thingspeak_post_string = make_thingspeak_post_string(vals,sens_numbers)
   emoncms_post_string = make_emoncms_post_string(vals,sens_numbers)
   #if __name__ == '__main__':
   print "Values: " + str(vals)                         # For debugging
   if len(thingspeak_post_string) != 0:                 # Only post if there is something to post
      thingspeak(thingspeak_key,thingspeak_post_string) # Post to thingspeak 
      emoncms(emoncms_key,emoncms_post_string)          # Post to emoncms
