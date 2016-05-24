#/usr/bin/python
"""
asonste 09/jan-2016
For reading temperature of a DS18B20 sensor, based on a known sensor id
Returns temperature in degrees celsius. Returns 99999 if there is a error
Remember to define your sensor id if you want to call the script directly 
"""
def gettemp(id):
  try:
    mytemp = ''
    filename = 'w1_slave'
    f = open('/sys/bus/w1/devices/' + id + '/' + filename, 'r')
    line = f.readline() # read 1st line
    crc = line.rsplit(' ',1)
    crc = crc[1].replace('\n', '')
    if crc=='YES':
      line = f.readline() # read 2nd line
      mytemp  = line.rsplit('t=',1)
    else:
      mytemp = 99999 # 99999 indicates a error
    f.close()
    mytemp1 =  int(mytemp[1])
    temp_c = round(float(mytemp1) / 1000.0, 2)
    temp_f = round(temp_c * 9.0 / 5.0 + 32.0, 2) # Uncomment if you want "f" / fahrenheit
    return temp_c # Change to temp_f if you want fahrenheit
  except:
    return 99999 # 99999 indicates a error

#--- For testing --------------------------
if __name__ == '__main__':
  # Script has been called directly
  id = '28-00000638a2fa'# Enter id of a DS18B20 you know is connected to the Pi
  print "Temp : " + '{:.3f}'.format(gettemp(id))
