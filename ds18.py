#/usr/bin/python
"""
asonste 12/Nov.2016
Features:
- Read ID and temp of all connected DS18B20
- Check if the detected sensors are defined in config file
  - if not, add the sensor as a new section
  - Add the ID and deafult options as defines in 'DeafultSens' section
Latest change: Completely changed check and write to config part
"""
from list_ds18 import *
from read_single import *
from conf import *
from log import *
IDs = get_IDs()      # Get ID of all connected senors
print IDs
count = 0
for id in IDs:       # Loop through sensor IDs
   i = IDs[count]
   temp = gettemp(i) #Get temp of each one
   print "ID: %s Temp: %s"%(i,temp)
   count = count +1

sections = config.sections() # Get all sections
count = 0
sens = 0
new_ids = []
section_ids = []
for i in sections:
   if 'sens' in sections[count]: # Find sensor sections
      sens = sens + 1 # Count the nomber of sensors defined
      # Make a list of all IDs defined in config file
      section_ids.append(config.get(sections[count],'id'))
   count = count + 1
count = 0

# Get deafult options to apply to any new sensors
valid_options = options('DeafultSens')

SensDeafults = []
optioncount = 0
for option in valid_options: # Get deafult values to apply to any new sensors
   SensDeafults.append(config.get('DeafultSens',valid_options[optioncount]))
   optioncount = optioncount + 1
optioncount = 0

for i in IDs:
   # Check if the any of the detected IDs are not defined in conf file
   if not IDs[count] in section_ids:
      sens = sens + 1 # The new sensors number
      str_sens = ('sens%s'%sens) # The new sensors section (main identifier)
      text = ("Add sens no %s ID: %s"%(str_sens, IDs[count]))
      print text
      log(text)
      check_section(str_sens)   # Start by adding the section
      optioncount = 0
      for option in valid_options:
         check_option(str_sens,valid_options[optioncount]) # Add all the options
         if optioncount == 0:   # Add speciffic name
            write_config(str_sens,valid_options[optioncount],str_sens)
         elif optioncount == 1: # Add speciffic ID
           write_config(str_sens,valid_options[optioncount],IDs[count])
         else:                  # Add deafult values for everything else
            write_config(str_sens,valid_options[optioncount],SensDeafults[optioncount])
         optioncount = optioncount + 1
   count = count + 1

