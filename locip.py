#/usr/bin/python
"""
asonste 29/June.2016
For finding local ip, first IP segment and first three IP segments
Will also compare IP towards conf file and triger gmail notification if IP has changed.
"""
from conf import *
from send_gmail import *

import socket, struct, fcntl, os
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockfd = sock.fileno()
SIOCGIFADDR = 0x8915

def get_ip(iface = 'eth0'):
     ifreq = struct.pack('16sH14s', iface, socket.AF_INET, '\x00'*14)
     try:
         res = fcntl.ioctl(sockfd, SIOCGIFADDR, ifreq)
     except:
         return None
     ip = struct.unpack('16sH2x4s8x', res)[2]
     return socket.inet_ntoa(ip)

def ip_specifficpart(ip,no):
   parts = ip.split('.')
   return parts[no]

def localip():
   iface = os.listdir('/sys/class/net/') # List interfaces
   count = -1
   for f in iface:
      count = count +1
      tmp = iface[count]
      IP = get_ip('%s'%tmp)
      #print type(IP)
      if type(IP) == str:
         if ip_specifficpart(IP,0) != "127":
            return IP
        # print type(IP)

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
    lastIP = config.get('networking','locIP')# Get last IP from .conf file     
    currentIP = localip()
    if lastIP != currentIP: # If true, IP have changed
       write_config('networking','locIP',currentIP) #write new IP to .conf file
       #Send a gmail
       s = ("Local IP changed from " + str(lastIP) + " to " + str(currentIP)) #Email Subject
       b = "" # Email Body
       send_gmail(s,b) #Use function from anoter file.
       return "Local IP Changed. Gmail sent"
    else:
       return "IP is the same"

#--- For testing ------------- 
if __name__ == "__main__":
   print "Specific IP part 1: "+ str(ip_specifficpart(localip(),0))
   print "Valid IP: "+ str(localip())
   print "Short IP: "+ str(ip_short(localip()))
   print check_locip()
