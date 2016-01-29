#!/usr/bin/env python
import sys

prev_show = None
total = 0
print_flag = 0

for line in sys.stdin:
    line       = line.strip()       #strip out carriage return
    key_value  = line.split('\t')   #split line, into key and value,

    #note: for simple debugging use print statements, ie:  
    curr_show  = key_value[0]         #key is first item in list, indexed by 0
    value_in   = key_value[1]         #value is 2nd item

    if (prev_show != curr_show):
        if (print_flag == 1):
            print( '%s\t%s' % (prev_show, total) )
            print_flag = 0
            total = 0
        if (value_in != "ABC"):
            total = int(value_in)
    else:
        if (value_in != "ABC"):
            total = int(total) + int(value_in)
    if (value_in == "ABC"):
        print_flag = 1

    prev_show = curr_show