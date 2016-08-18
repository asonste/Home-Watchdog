#/usr/bin/python
# -*- coding: utf-8 -*-
""" 
asonste 18/Aug-2016 Misc IP Ping utilities.
Latest changes: Changed pingweb for pinging any adress
Added pingIPs. 
Improved runpingweb with last-alive-time and logging.
""" 
from locip import *
from conf import * 
from log import *
import os, time
from datetime import datetime 

def pingrange(sub,Range,start): 
# Pinging adresses on a net, based on known subnet, range and start address. Returns found IPs
    IPs = []
    for f in range(Range):
       current = str(f+start)
       IP = ("%s.%s"%(sub,current))
       os.system("echo %s"%(IP))
       test = os.system("ping %s -c 1 -W 1"%(IP)) # -c count -W timeout
       if test == 0:
          IPs.append(str(IP))
    return IPs

webIP="8.8.8.8" # 8.8.8.8 is google dns server.
def pingweb(ip_of_Device=webIP): # If no IP is passed, 8.8.8.8 is used
# Pinging a address, to check if there is conectivity. 
	test = os.system("ping %s -c 1 -W 1"%(ip_of_Device)) # -c count -W timeout. 
	if test == 0: 
		return "1" 
	else: 
		return "0"

def pingIPs(list_of_IPs):
#  Pinging a list of IPs
	IPs = [] 
	count=-1 
	for f in list_of_IPs: 
		count = count+1 
		current = list_of_IPs[count]
                runpingweb(str(current)) 

def runpingweb(ip=webIP): # If no IP is passed, 8.8.8.8 is used
   result = pingweb(ip)
   check_section(ip) # Check if IP is in the conf file, if not, add it.
   status = check_option(ip,"status") # Add option if it does not exist
   check_option(ip,"last-alive-time") # Add option if it does not exist
   print result
   if result == "0": # No connection
       text = ("No connection to %s"%(ip))
       if status == "connected": # Only log if previous state was "Connected"
          log(text)
       write_config(ip,'status', 'disconnected')
       return text
   elif result == "1" and status == "connected": # Connection OK
       write_config(ip,"last-alive-time",dateandtime()) # Log alivetime
   elif result == "1" and status != "connected":
       write_config(ip, 'status', 'connected')
       lastAliveStr = config.get(ip,'last-alive-time')
       if lastAliveStr != "": # Time exists
          lastAlive = datetime.strptime(lastAliveStr, '%Y-%m-%d %H:%M:%S')
          nowtime = datetime.strptime(str(dateandtime()), '%Y-%m-%d %H:%M:%S')
          alivetime_diff = nowtime - lastAlive # Calculate time since last time it was alive
          text = ("Connection to %s restored after %s offline"%(ip,str(alivetime_diff)))
       elif lastAliveStr == "": # No time has been recorded
          text = ("First connection to IP %s"%(ip))
       write_config(ip,"last-alive-time",dateandtime())
       log(text)
   
#-----------------------------------------------------
# For testing
if __name__ == "__main__":
   print "RUNNING EXAMPLE"
   Range = 10
   start = 1
   #sub = ip_short(localip())
   #print "Subnet: " + str(sub)
   #print "Found IP`s: " + str(pingrange(sub,Range,start))
   #print(pingweb())
   #runpingweb()
   #pingIP()
   testIPs = ['8.8.8.8','8.8.8.9'] #List of test IPs. 8.8.8.9 should fail.
   #pingIPs(testIPs)
