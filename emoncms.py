#!/usr/bin/python
"""
asonste 12/Nov.2016
For posting values to emoncms
Run with poststing as argument.
example: sudo python emoncms.py 'ID1:10'
if you vant to post multiple values at the same time, separate with comma:
example: sudo python emoncms.py 'ID1:10,ID2:20'
"""
import sys
import urllib2
from conf import * # import user speciffic config

emoncms_key =  config.get('emoncms','emoncms_key') # Get key from conf file

def emoncms(key,poststring):
# Post values to emoncms
   baseURL = ('https://emoncms.org/input/post.json?json={%s}&apikey=%s'%(poststring,key))
   f = urllib2.urlopen(baseURL)
   print f.read() # Will print OK if ok 
   f.close()

if len(sys.argv) >= 2:            # Check if argument is given
   post_string = str(sys.argv[1]) # Script to be run with poststring as argument
   if __name__ == '__main__':
      print post_string
      print "Post string length:" + str(len(post_string))
      print emoncms(emoncms_key,post_string)

