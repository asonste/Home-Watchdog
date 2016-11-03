#!/bin/bash
# asonste 3.Nov.2016 
#For starting mqtt.py and keep it running
# Change the process and "mqtt.py" path to your needs
# Latest change:  Minor corrections
# To add to crontab, every minute:
# sudo su
# crontab -e
# * * * * * bash /home/pi/Home-Watchdog/keep_running.sh
# argument 1: base_dir
# argument 2: sensor

process="mqtt.py $2"
echo Process is: $process
echo base directory is: $1
keep_running="/usr/bin/python $1/mqtt.py $2 > /dev/null 2>&1"
if ps ax | grep -v grep | grep -v bash | grep  $2
then
    printf "Process '%s' is running.\n" "$process"
    exit
else
    printf "Starting process '%s' with command '%s'.\n" "$process" $keep_runnig
    $keep_running
fi
exit

