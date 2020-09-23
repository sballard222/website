# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 08:16:23 2020

@author: Administrator
"""

import json
import pandas as pd

# Read the data from file
# We now have a Python dictionary
#with open('messages.json') as f:
    #data_listofdict = json.load(f)
    
# We can do the same thing with pandas
data_df = pd.read_json('C:\Users\Administrator\OneDrive - University of Miami\Desktop\air_sea_sam_20200120_part_1\messages.json', orient='records')

# We can write a dictionary to JSON like so
# Use 'indent' and 'sort_keys' to make the JSON
# file look nice
with open('new_data.json', 'w+') as json_file:
    json.dump(data_listofdict, json_file, indent=4, sort_keys=True)

# And again the same thing with pandas
export = data_df.to_json('new_data.json', orient='records')