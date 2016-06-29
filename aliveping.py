#/usr/bin/python
""" 
asonste 29/June-2016 Misc IP Ping utilities.
Latest changes: made separate section in .conf file for networking
""" 
from locip import *
from conf import * 
from log import *
import os, time 
def pingrange(sub,Range,start): 
# Pinging adresses on a net, based on known subnet, range and start address. Returns found IPs
    IPs = []
    for f in range(Range):
       current = str(f+start)
       IP = ("%s.%s"%(sub,current))
       os.system("echo %s"%(IP))
       test = os.system("ping %s -c 1 -W 1"%(IP)) # -c count -W timeout
       if test == 0:
          #print "found IP"
          IPs.append(str(IP))
    return IPs

def pingweb():
#Pinging a known web address, to check if there is internet conectivity.
    test = os.system("ping 8.8.8.8 -c 1 -W 1") # -c count -W timeout. 8.8.8.8 is google dns server.
    if test == 0:
       return "1"
    else:
       return "0"

def runpingweb(): # Function to be called on from crontab
    result = pingweb()
    inetstat = config.get('networking', 'inet_con_stat') #Stored inet connection status
    #print inetstat
    if result == "0":
       count = 0
       for f in range(5):
          result = pingweb()
          if result == "0":
             count = count +1
             time.sleep(5)
       if count == 5:
          text = "No connection to inet"
          return text
          log(text)
          write_config('networking', 'inet_con_stat', 'disconnected')
    elif inetstat == "disconnected":
       write_config('networking', 'inet_con_stat', 'connected')
       text = "inet connection restored" 
       log(text)   
#-----------------------------------------------------
# For testing
if __name__ == "__main__":
   print "RUNNING EXAMPLE"
   Range = 10
   start = 1
   #sub = ip_short(localip())
 #  print "Subnet: " + str(sub)
   #print "Found IP`s: " + str(pingrange(sub,Range,start))
#   print(pingweb())
   runpingweb()
