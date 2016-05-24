#!/usr/bin/python
"""
asonste 01/Feb.2016
Script to be impoted to every other script that is
accessing .conf file
Lastest changes: Minor changes to  "options" and "check_option" return value.
"""
import ConfigParser
import os
config = ConfigParser.ConfigParser(allow_no_value = True)
dir = os.getcwd() # Current directory
dir2 = ('%s/usr.conf'%dir) # User config file
config.read(dir2)
def write_config(section,subsection,value):
   cfgfile = open(dir2,'w')
   config.set(section,subsection,value)
   config.write(cfgfile)
   cfgfile.close()

def check_section(section):
   if not config.has_section(section):                                
       config.add_section(section)
       cfgfile = open(dir2,'w')
       config.write(cfgfile)
       cfgfile.close()
       return "added section"
   elif config.has_section(section):
       return "section exists"
   else:
       return "Error"

def check_option(section,option):
   if config.has_option(section,option):
      return config.get(section,option)
   else:
      return "option does not exist"

def options(section):
    options = config.options(section)
    return options

if dir != check_option('defult','base_dir'):
   write_config('defult','base_dir',dir) # writes default path

#-----------------------------------------------------
# For testing
if __name__ == "__main__":
   sections = config.sections()
   print ("Config sections: " + str(sections))
   check_section('test3')
   #options(sections[0])
   count = 0
   for f in sections:
     options(sections[count])
     count = count + 1   
   print check_option('special','new')
