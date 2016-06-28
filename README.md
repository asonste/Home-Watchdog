# Home-Watchdog
---- This is a ongoing project ----
Main features:
- Raspberry Pi project to monitor your home
- Code language will mainly be Python
- The Raspberry Pi will send alerts by email, and  log to a log file
- It will be and be controlled by email and SSH

I will aim against making one or more files for each function, and then call the file when needed.

All user specific parameters are defined in the .conf file. Base directory for all the files are defined in the conf.py file.

Short description of the main files:
conf.py
- Handles reading / writing from the .conf file

run.py
- The script is to be run from crontab. Other scripts are run from the run.py file

log.py 
- Handles logging to the log file

send_gmail.py
- Sends gmails. Account information is collected from the .conf file

aliveping.py
- For verifying network conectivity

locip.py
- For getting the local iP of the device

extip.py
- For getting the external IP

## Functions to come ## 

1) Temperature (DS18B20)
  - Room sensor to detect fire and prevent freezing water pipes.
  - Refrigerator sensor to make sure the unit is functioning properly 

2) Noise
	- To detect fire alarm or intrusion
	
3) General power failure
  - Gracefully shut down equipment powered from UPS
  
4) Moisture
	- Detect water leak
	
5) Motion
	- To detect intrusion 

Control functions :
- Control relays connected to GPIO 
  - Heater
  - Power on / Shutdown computer equipment
