# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Python program to convert 
# JSON file to CSV 


import json
import csv
import sys

sys.setdefaultencoding("UTF-8")
f = open('C:\Users\Administrator\OneDrive - University of Miami\Desktop\air_sea_sam_20200120_part_1\messages.json')
data = json.load(f)
f.close()

f = open('data.csv')
csv_file = csv.writer(f)
for item in data:
    csv_file.writerow(item)

f.close()