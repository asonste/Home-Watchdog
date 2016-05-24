#/usr/bin/python
"""
asonste 01/Feb.2016
- EARLY STAGE TESTING -
Combining multiple functions in order to print IDs and temperatures
Working on reading temp alarm limits
"""
from list_ds18 import *
from read_single import *
from conf import *
IDs = get_IDs()
count = 0
for id in IDs: # Loop through sensor IDs
   i = IDs[count]
   chk = check_section(i)
   if chk == 'added section':
      print "add"
   elif chk == 'section exists':
      print "exist"
   temp = gettemp(i)
   print "ID: %s Temp: %s"%(i,temp)
   opt = options(i)
   print opt
   count = count +1
   count2 = 0
   for f in opt: # Loop through sensor options
      print check_option(i,opt[count2])
      count2 = count2 + 1
