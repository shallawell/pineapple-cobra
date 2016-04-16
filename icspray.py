#!/usr/bin/python
#
# Author: Sam Hallawell    shallawell@gmail.com
# 5 July 2014
# Version 0.1
# Name : Raspberry Pi Intercooler Spray Controller and Data Logger
# FileName : icspray.py
# 
# Requirements:
#	Python 3.3
#	Raspberry Pi (prefer Model B)
# 	BBIO Library 
# 	ADC Breakout Board 
#

from bbio import *
import sys
import time
import gpio

# define interval timers in milliseconds  1000=1sec
# How long the spray should last before checking the status again
IC_SPRAY_INTERVAL = 2000

# define global variables and active functions
#intercooler temperature configuration
GET_IC_TEMP=true
IC_TEMP_THRESHOLD=35

#Pre intercooler temperature configuration
#GET_PRE_IC_TEMP=true

#Intake TB temperature configuration
#GET_INTAKE_TB_TEMP=true
#INTB_THRESHOLD=25   #25 for 25 degrees intake temp

#Ambient temperature configuration
#GET_AMBIENT_TEMP=true

#Time configuration
GET_CURRENT_TIME=true

#TPS configuration
#GET_TPS_PERCENT=true
#TPS_THRESHOLD=80   #80 for 80 percent TPS

#Water Tank Level configuration
GET_WATER_LEVEL=true

#IC Relay configuration
GET_IC_RELAY_STATE=true
IC_RELAY_REQUIRED_VOLTAGE=12  # 12 for 12V
SPRAY_ENABLED=false  # for testing without using water


# Define sensors
GPIOx=    			# Map GPIO to IC Temp sensor
ic_sensor=GPIOx   	# Friendly name
#GPIOw=    			# Map GPIO to Pre IC Temp sensor
#pre_ic_sensor=GPIOw	# Friendly name
#GPIOy=    			# Map GPIO to Intake TB Temp sensor
#intb_sensor=GPIOy  	# Friendly name
#GPIOz=				# Map GPIO to Ambient Temp sensor
#amb_sensor=GPIOz	# Friendly name
#GPIOv=				# Map GPIO to IC Relay sensor
#ic_relay_sensor=GPIOv# Friendly name
#GPIOt=				# Map GPIO to TPS sensor
#tps_sensor=GPIOt	# Friendly name


## Example code   http://hipstercircuits.com/thermistor-temperature-reading-with-beaglebone/
#  Good Math Examples for converting thermistor resistance and voltage to degrees
#def readThermistor():
#    # Get the ADC values:
#    adc_val = analogRead(therm1)
#    # And convert to voltages:
#    voltage1 = inVolts(adc_val)
#    print "AIN6 ADC value: %i, voltage: %fv" % (adc_val, voltage1)
#    delay(IC_SPRAY_INTERVAL)
#--END Example




def get_ic():
#	"Returns the voltage from GPIOx to represent temperature"
	ic_volts = analogRead(ic_sensor)
#	# And convert to voltages:
    voltage1 = inVolts(adc_val)
    print "AIN6 ADC value: %i, voltage: %fv" % (adc_val, voltage1)
    delay(500)
#	"Convert volts to degrees C"
	ic_temp = inVolts(ic_volts)
	round(ic_temp, 1)
	return ic_temp

def get_pre_ic():
#	"Returns the voltage from GPIOw to represent temperature"
	pre_ic_volts = analogRead(pre_ic_sensor)
#	"Convert volts to degrees C"
	pre_ic_temp = pre_ic_volts * VOLTS_TO_TEMP_MULTIPLER
	round(pre_ic_temp, 1)
	return pre_ic_temp	
		
def get_intake_tb():
#	"Returns the voltage from GPIOx to represent temperature"
	intb_volts = analogRead(intb_sensor)
#	"Convert volts to degrees C"
	intb_temp = intb_volts * VOLTS_TO_TEMP_MULTIPLER
	round(intb_temp, 1)
	return intb_temp

def get_ambient():
#	"Returns the voltage from GPIOx to represent temperature"
	amb_volts = analogRead(amb_sensor)
#	"Convert volts to degrees C"
	amb_temp = amb_volts * VOLTS_TO_TEMP_MULTIPLER
	round(amb_temp, 1)
	return amb_temp

def get_current_time():
	current_time = (time.strftime("%H:%M:%S"))
	return current_time

def get_ic_relay_state():
	ic_relay_volts = analogRead(ic_relay_sensor)
	#	"test volts to read status"
	if ic_relay_volts >= IC_RELAY_REQUIRED_VOLTAGE:
		ic_relay_status = true
		print 'IC Relay is on'
	else
		ic_relay_status = false
		print 'IC Relay is off'
	return ic_relay_status
	
def ic_relay_on():
	#test if relay is already on
	ic_relay_state()
	#if relay is off, turn it on, else do nothing
	if ic_relay_status = false
		POWER ON analogRead(ic_relay_sensor)
		print 'IC Relay is now on'
	else
		print 'IC Relay is already on'
	return
	
def ic_relay_off():	
	#test if relay is already off
	ic_relay_state()
	#if relay is on, turn it off, else do nothing
	if ic_relay_status = true:
		POWER OFF ic_relay_sensor()
		print 'IC Relay is now off'
	else:
		print 'IC Relay is already off'
	return

def get_water_level():
	lvl_resistance = READ GPIOu()
	#	"test resistance to read status"
	if lvl_resistance <= 10:
		water_level = EMPTY
		print 'IC Water Level is empty'
	elif lvl_resistance = 11-100:
		water_level = LOW
		print 'IC Water Level is low'
	else lvl_resistance => 100:
		water_level = OK
		print 'IC Water Level is OK'
	return water_level	
	

def get_tps_percent():
#	"Returns the voltage from GPIOt to represent TPS%"
	tps_volts = READ tps_sensor()
#	"Convert volts to TPS%"
	if tps_volts <= 1.0:
		print 'TPS is equal to or less than 20%'
	elif tps_volts <=1.1 but => 2.0:
		print 'TPS is between 21 and 40%'
	elif tps_volts <=2.1 but => 3.0:
		print 'TPS is between 41 and 60%'
	elif tps_volts <=3.1 but => 4.0:
		print 'TPS is between 61 and 80%'
	elif tps_volts <=4.1 but => 5.0:
		print 'TPS is between 81 and 100%'
	tps_perc = tps_volts * ???
	round(tps_perc * ????, 0)
	return tps_perc	
	
def print_all():
	get_ic()
	print("The Intercooler external core temp is", ic_temp)
	get_pre_ic()
	print("The Pre-Intercooler temp is", pre_ic_temp)
	get_intake_tb()
	print("The Intake temp is", intb_temp)
	get_ambient()
	print("The Ambient temp is", amb_temp)
	get_current_time()
	print(current_time)
	ic_relay_state()
	return
	
def run_ic_spray():
	#run pre-checks
	get_ic()
	get_pre_ic()
	get_intake_tb()
	get_ambient()
	get_current_time()
	get_ic_relay_state()
	get_tps_perc()
	get_water_level()
	while True:
	get_water_level()
	if water_level = EMPTY:
		print("IC water level is too low to start spray")
		break
		elif SPRAY_ENABLED = false:
			print "SPRAY_ENABLED = false... Pump is Active is testing mode" # pump not really on
		elif water_level = [OK, LOW] and SPARY_ENABLED = true:
			if tps_perc > TPS_THRESHOLD and intb_temp > INTB_THRESHOLD :
			ic_relay_on();
			print("IC spray is ACTIVE")  # pump on for real
			sleep IC_SPRAY_INTERVAL;   # spray water for interval timer and repeat
		elif 
			ic_relay_off();
	return	
	
	
	
