#!/usr/bin/env python
import sys


for line in sys.stdin:
    line       = line.strip()   #strip out carriage return
    key_value  = line.split(",")   #split line, into key and value, returns a list
    key_in     = key_value[0]   #key is first item in list
    value_in   = key_value[1]   #value is 2nd item 

    #print key_in
    if value_in == 'ABC':           
        show = key_in      
        chan = value_in
        print( '%s\t%s' % (show, chan) )  #print a string, tab, and string
    elif value_in.isdigit():   #key is only <word> so just pass it through
        print( '%s\t%s' % (key_in, value_in) )  #print a string tab and string

