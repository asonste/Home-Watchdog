#/usr/bin/python
"""
asonste 28/June.2016
The script is called from crontab every minute
To add crontab with output to debug file:
sudo su
crontab -e
* * * * * /usr/bin/python /home/pi/Home-Watchdog/run.py >>/tmp/out.txt 2>&1
"""
from log import *
#log("Test") # For verifying that the script is beeing run from crontab.

from extip import *
checkip()    # Check if external IP has changed 

from locip import *
check_locip()# Check if local IP has changed

from aliveping import *
runpingweb() # Writes Connected / Disconnected to .conf file and logs events 
