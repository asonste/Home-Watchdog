#!/usr/bin/python
"""
asonste 16/Aug.2016
Script to be impoted to every other script that is
accessing .conf file
Latest changes: Changed check_option to automatically add option if it does not exist.
"""
import ConfigParser
import os
config = ConfigParser.ConfigParser(allow_no_value = True)
base_dir = ("/home/pi/Home-Watchdog")# < SET YOUR BASE PATH HERE
conf_path = ('%s/usr.conf'%base_dir) # User config file)
config.read(conf_path)
def write_config(section,subsection,value):
   cfgfile = open(conf_path,'w')
   config.set(section,subsection,value)
   config.write(cfgfile)
   cfgfile.close()

def check_section(section):
   if not config.has_section(section):                                
       config.add_section(section)
       cfgfile = open(conf_path,'w')
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
      config.set(section,option,"")
      cfgfile = open(conf_path,'w')
      config.write(cfgfile)
      cfgfile.close()
      return "added option"

def options(section):
    options = config.options(section)
    return options

if dir != check_option('defult','base_dir'):
   write_config('defult','base_dir',base_dir) # writes default path

#-----------------------------------------------------
# For testing
if __name__ == "__main__":
   #sections = config.sections()
   #print ("Config sections: " + str(sections))
   #check_section('test3')
   #options(sections[0])
   count = 0
   #for f in sections:
    # options(sections[count])
     #count = count + 1   
   #print check_option('special','new')
   #print check_option("8.8.8.8", "datetim")
