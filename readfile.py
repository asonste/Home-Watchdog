#!/usr/bin/python
"""
asonste 09/jan.2016
For reading all lines in file1 in to a list
It takes one parameter: readvars(filepath)
"""
def readvars(filepath): # For reading all lines in file1 in to a list
    file = open(filepath,'r')
    read_it1 = file.read()
    myline1 = []
    for line1 in read_it1.splitlines():
       myline1.append(line1)
       file.close()
    return myline1[:]

#--- For testing -------------
if __name__ == "__main__":
   print "Testing..."
   filepath = "/home/pi/watchdog/Log.txt"
   print readvars(filepath)
