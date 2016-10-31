#!/usr/bin/python
"""
asonste 31.Oct.2016
For backing up all files in the base directory to a zip file.
Latest changes: Changed to include a copy of crontab, alias, fstab, rsync to another diractory 
"""
import os, time
from conf import *
from log import *
source = [config.get('defult','base_dir')]# Get defult base path from .conf file
target_dir = str(config.get('defult','backup_dir')) # Get backup directory from .conf file
today = target_dir + time.strftime('%Y%m%d')
# The current time is the name of the zip archive
now = time.strftime('%H%M%S')
print"Copy crontab..."
cp_crontabCMD = ('crontab -l > %s/crontab.txt'%source[0])
os.system(cp_crontabCMD)
print "Copy alias..."
alias_cmd = ('alias >> alias.txt')
os.system(alias_cmd)
print "Copy fstab..."
os.system('cat /etc/fstab >> fstab.txt') 
def zip_backup(comment):
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

#-----------------------------------------------------
if __name__ == '__main__':
   # Comment from the user to include in the name of the zip file
   comment = raw_input('Enter a comment --> ')
   zip_backup(comment)
   time.sleep(3)
   print"Rsync..."
   rsync_cmd = "rsync -r /home/pi/Documents/Backups /mnt/freenas/Programing/Raspberry_Pi_3"
   os.system(rsync_cmd)
