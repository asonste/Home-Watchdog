#!/bin/bash
# For starting programs and keep them running
# Change the process and "keep_running" path to your needs
# To add to chrontab, every minute:
# sudo su
# crontab -e
# * * * * * bash /home/pi/Home-Watchdog/makerun.sh
process="mqtt.py sens1"
keep_running="sudo python /home/pi/Documents/Home-Watchdog/mqtt.py sens1"
if ps ax | grep -v grep | grep -v bash | grep --quiet $process
then
    printf "Process '%s' is running.\n" "$process"
    exit
else
    printf "Starting process '%s' with command '%s'.\n" "$process" "$keep_running"
    $keep_running
fi
exit
