#!/usr/bin/python
import sys
sys.path.append('/home/pi/xively_tutorial/.envs/venv/lib/python2.7/site-packages')


database_file = "/home/pi/DS18B20/temperatures.rrd"
MIN_TEMP = -100

def read_temperature():
  # open/read/close the file with the temperature
  tfile = open("/sys/devices/w1_bus_master1/28-000005e34189/w1_slave")
  text = tfile.read()
  tfile.close()

  # split the two lines
  lines = text.split("\n")

  # make sure the crc is valid
  if lines[0].find("YES") > 0:
    # get the 9th (10th) chunk of text and lose the t= bit
    temp = float((lines[1].split(" ")[9])[2:])
    # add a decimal point
    temp /= 1000
    return temp
  return MIN_TEMP-1

current_temp = read_temperature()