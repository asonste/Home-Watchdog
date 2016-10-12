#!/usr/bin/python
"""
asonste 12/Oct.2016
For posting values to thingspeak.
Will check sens(x) x=1-4 text files for new values, then post to thingspeak.
Currently adapted for posting four values at the time
"""
import sys
import urllib2
from conf import *
import time
from readfile import *
from writefile import *
time.sleep(50) # Wait until sensors are read
key =  config.get('thingspeak','thingspeak_key')

def make_post_string(stat,vals):
   count = 0
   poststring = []
   for s in vals:
      print count
      print vals[count]
      if vals[count]!= None:
         print 'Adding to string...'
         poststring.append('&field%s=%s'%(count+1,vals[count]))
      count = count + 1
   return ''.join(poststring)

def thingspeak(key,poststring):
   baseURL = ('https://api.thingspeak.com/update?api_key=%s'%key)
   f = urllib2.urlopen(baseURL + "%s"%poststring)
   print f.read()
   f.close()

def currentvals(no):
   varslist = readvars('/home/pi/Documents/Home-Watchdog/%s.txt'%no)
   singlevars = varslist[0]
   singlevars2=singlevars.split(',')
   a = singlevars2[0] # Value
   b = singlevars2[1] # Status
   if b == 'newtemp': # Check if the value in the text file is new
      writefile('no_value,no_value','/home/pi/Documents/Home-Watchdog/%s.txt'%no)
      return a
#currentvals('sens2')

#while 1 == 1: # For running as a loop
if 1 ==1: # For funning one time
   vals = []
   vals.append(currentvals('sens1'))
   vals.append(currentvals('sens2'))
   vals.append(currentvals('sens3'))
   vals.append(currentvals('sens4'))
   stat = []
   stat.append(config.get('sens1','progress'))
   stat.append(config.get('sens2','progress'))
   stat.append(config.get('sens3','progress'))
   stat.append(config.get('sens4','progress'))
   #print make_post_string(stat,vals)
   post_string = make_post_string(stat,vals)
   if __name__ == '__main__':
      print "Values: " + str(vals)
     # print "Statuses: "+ str(stat)
      print post_string
      print "Post string length:" + str(len(post_string))
   if len(post_string) != 0: # Only post if there is something to post
      thingspeak(key,post_string)
