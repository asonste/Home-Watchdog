#!/usr/bin/python
"""
asonste 28/June.2016
For backing up all files in the base directory to a zip file.
"""
import os, time
from conf import *
from log import *
source = [config.get('defult','base_dir')]# Get defult base path from .conf file

target_dir = str(config.get('defult','backup_dir')) # Get backup directory from .conf file
today = target_dir + time.strftime('%Y%m%d')
# The current time is the name of the zip archive
now = time.strftime('%H%M%S')
def zip_backup():
# Comment from the user to include in the name of the zip file
   comment = raw_input('Enter a comment --> ')
   if len(comment) == 0: # check if a comment was provided
        target = today + os.sep + now + '.zip'
   else:
        target = today + os.sep + now + '_' + \
        comment.replace(' ', '_') + '.zip'

# Create the subdirectory if it does not already exist
   if not os.path.exists(today):
        os.mkdir(today) # make the directory
        text1 = str(today)
        print 'Successfully created backup directory', today
        log('Successfully created backup directory %s'%(text1))

# Do the backup
   zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))

   if os.system(zip_command) == 0:
        print 'Successful backup to', target
        text2 = str(target)
        log('Successfully created backup %s'%(text2))
   else:
        print 'Backup Failed'
        log('Backup Failed')

zip_backup()
