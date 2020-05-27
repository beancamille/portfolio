#!/usr/bin/python
# run code with linux command : python ./stock_mapper.py < stocks.csv | sort | python ./stock_reducer.py
import sys
import re

for line in sys.stdin: # for entire csv
    line = re.sub( r'^\W+|\W+$', '', line ) # find line
    words = line.split(",") # split line into words
    year = words[0][0:4] # year is first 4 digits of first item in line
    close = words[4] # closing stock price is 5th item in line
    if year.isalpha() == False:
        print(year + "\t" + close) # year is key, closing price is value
