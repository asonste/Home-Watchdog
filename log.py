#!/usr/bin/python
"""
asonste 28/jan.2016
For loging events to a log file, and adding timestamp on the event
One mandatory parameter (text) and one optional parameter (logfilepath).
Latest changes: auto-define log file path.
"""
from conf import *
base = config.get('defult','base_dir')# Get defult logfilepath from .conf file
path = ('%s/log.txt'%(base))
from time import strftime
import time
datetime = (time.strftime("%Y-%m-%d ") + time.strftime("%H:%M:%S"))

def log(string,logfilepath=path):
   f = open(logfilepath, 'a') # a for append, w for write.
   f.write(datetime + ' {0}\n'.format(string))
   f.close() # Close the file

#--- For testing -------------
if __name__ == "__main__":
   print "Testing..."
   var = 1
   text = ('Logging test, variable: %d'%var)
   log(text)