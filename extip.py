#/usr/bin/python
"""
asonste 29/June.2016
For resolving external ip. If run directly, it will
compare current ip with last ip and send mail if it changed.
Latest changes: Added check for "None" IP. Made separate section in .conf file for networking.
Future improvements: Need a timeout that will kill the script, if it takes to lont to resolve IP or send Gmail.
"""
from conf import *
from send_gmail import *
lastIP = config.get('networking','lastIP')# Get last IP from .conf file
from urllib import urlopen
import re
url='http://checkip.dyndns.org'
def extip():
    if pingweb() == "1": # check if device is online
       request = urlopen(url).read().decode('utf-8')
       outIP = re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", request)
       return str(outIP[0])
    elif pingweb() == "0": # If true, device is not online
       return lastIP
def checkip():
    currentIP = extip()
    if lastIP != currentIP and str(currentIP) != "None": # If true, IP have changed
       write_config('networking','lastIP',currentIP) #write new IP to .conf file
       #Send a gmail
       s = ("External IP changed from " + str(lastIP) + " to " + str(currentIP)) #Email Subject
       b = "" # Email Body
       send_gmail(s,b) #Use function from anoter file. 
       return "External IP Changed. Gmail sent"
    else:
       return "IP is the same"

# For testing----------------------------
if __name__ == "__main__":
   print "Testing..."
   print ("Last IP was: " + lastIP)
   currentIP = extip()
   print ("Curent IP is: " + currentIP)
   print(checkip())
