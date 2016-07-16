!/usr/bin/python
"""
asonste 16/Jul.2016
Script to run on boot.
Add it to crontab:
~ sudo su
~ sudo crontab -e
add line as below. Change base directory if necessary.
@reboot /usr/bin/python /home/pi/Home-Watchdog/boot.py
Lastest changes: First issue. Logging.
"""
from log import *
from conf import *
LastAliveTime = config.get('defult','Last-Alive-Time') #Get last alive time from conf file
text = ('System stated. Last alive time %s' %(LastAliveTime))
log(text)
