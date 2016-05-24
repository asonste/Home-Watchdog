#/usr/bin/python
"""
asonste 24/May.2016
For finding local ip, and IP without tha last IP segment.
"""
import commands
from conf import *
from send_gmail import *

def localip():
   locIP = commands.getoutput("/sbin/ifconfig").split("\n")[1].split()[1][5:]
   write_config('defult','locIP',locIP) #write new IP to .conf file
   return locIP #commands.getoutput("/sbin/ifconfig").split("\n")[1].split()[1][5:] 

def ip_short(ip):
   ipparts = ip.split('.')
   ip_short=""
   del ipparts[3]
   count = -1
   for f in ipparts:
      count = count +1
      ip_short = '.'.join(ipparts)
   return ip_short

def check_locip():
    lastIP = config.get('defult','locIP')# Get last IP from .conf file     
    currentIP = localip()
    if lastIP != currentIP: # If true, IP have changed
       write_config('defult','locIP',currentIP) #write new IP to .conf file
       #Send a gmail
       s = ("Local IP changed from " + str(lastIP) + " to " + str(currentIP)) #Email Subject
       b = "" # Email Body
       send_gmail(s,b) #Use function from anoter file.
       return "Local IP Changed. Gmail sent"
    else:
       return "IP is the same"

#--- For testing ------------- 
if __name__ == "__main__":
   print "Local ip: "+ str(localip())
   print "Short IP: "+ str(ip_short(localip()))
   print check_locip()
