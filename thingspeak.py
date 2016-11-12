#!/usr/bin/python
"""
asonste 12/Nov.2016
For posting values to thingspeak.
Latast change: split post section and make post string section in to separate files
"""
import urllib2
from conf import *
thingspeak_key =  config.get('thingspeak','thingspeak_key') # Get thingspeak key from .conf file

def thingspeak(key,poststring):
# For doing the Thingspeak post
   baseURL = ('https://api.thingspeak.com/update?api_key=%s'%key)
   f = urllib2.urlopen(baseURL + "%s"%poststring)
   print f.read()
   f.close()
