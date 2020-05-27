#!/usr/bin/python

import sys

previous = None
sum = 0
counter = 0 

for line in sys.stdin:
    key, value = line.split( '\t' ) # split sorted input into keys, values
    value = value.rstrip('\n') # strip any "new line" indicators
    key = key.rstrip('\n')
    
    if key != previous: # if year (key) is different than last, create new entry
        if previous is not None:
            # find average for previous year, sum/counter
            print("Year: " + previous + '\t' + "Average: " + str( sum/counter ))
        # advance key, reset sum and counter
        previous = key
        sum = 0
        counter = 0 
    
    # if same year, increase sum and counter
    sum = sum + float( value )
    counter += 1

#print average closing price for each year
print("Year: " + previous + '\t' + "Average: " + str( sum/counter ))
