#!/usr/bin/python
"""
Writes a list to lines in a file. One list parameter is one line.
Remember to define file path. Note, file will be overwritten!
"""
def writevar(content,filepath):
    lineno = -1
    file1 = open(filepath,'w')
    for line in content:
       lineno = lineno + 1
       file1.write(content[lineno] + "\n")
    file1.close()

def writefile(content,filepath):
   file1 = open(filepath,'w')
   file1.write(content)
   file1.close()

#--- For testing -------------
if __name__ == "__main__":
   print "RUNNING EXAMPLE"
   content = ['1','2','3','4']
   filepath = '/home/pi/watchdog/Log.txt' # Define your file path here. Note, file will be overwritten!
   writevar(content,filepath)
