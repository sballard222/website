# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 08:45:44 2020

@author: sballard
"""

import json
import pandas as pd
import csv
import sys
#reload(sys)
# Read the data from file
# We now have a Python dictionary,
#sys.setdefaultencoding("utf-8")
with open(r"C:\Users\sballard\OneDrive - University of Miami\Desktop\messages.json") as f:
    data  = json.load(f)
    
#data_df = pd.read_json('data', orient='records')  


keys = data[0].keys()
with open('saved_data.csv', 'wb') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(data_listofdict)
# Writing a list of dicts to CSV
#keys = data_listofdict[0].keys()
#with open("saved_data.csv", "wb") as output_file:
#    dict_writer = csv.DictWriter(output_file, keys)
#    dict_writer.writeheader()
#    dict_writer.writerows(data_listofdict)