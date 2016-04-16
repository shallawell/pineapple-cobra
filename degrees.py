#!/usr/bin/python
# Author: Sam Hallawell    shallawell@gmail.com
# 5 July 2014
# Version 0.1
# Name : Convert Degress via user input
# Script to convert fahrenheit(f) or celsius(c) 
# Filename : degrees.py



x = raw_input("would you like to convert fahrenheit(f) or celsius(c)?")
if x == "f":
    y = raw_input("what is the fahrenheit?")
    f = (int(y) - 32) * 5.0 / 9
    print f
elif x == "c":
    n = raw_input("what is the celsius?")
    z = (int(n) * 9) / 5.0 + 32
    print "and in fahrenheit, that is:"
    print z