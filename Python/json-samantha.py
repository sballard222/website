# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 09:04:53 2020

@author: sballard
"""

import csv, json, sys
#if you are not using utf-8 files, remove the next line
#sys.setdefaultencoding("UTF-8") #set the encode to utf8
#check if you pass the input file and output file
#if sys.argv[1] is not None and sys.argv[2] is not None:
fileInput = r"C:\Users\sballard\OneDrive - University of Miami\Desktop\air.sea.sam_20200120_part_1\messages.json"
fileOutput = r"C:\Users\sballard\OneDrive - University of Miami\Desktop\messages.csv"
inputFile = open(fileInput) #open json file
outputFile = open(fileOutput, 'w') #load csv file
data = json.load(inputFile) #load json content
inputFile.close() #close the input file
output = csv.writer(outputFile) #create a csv.write
output.writerow(data[0].keys())  # header row
for row in data:
    output.writerow(row.values()) #values row