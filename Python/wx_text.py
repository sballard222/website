# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 05:16:39 2020

@author: Administrator
"""

import json
import requests

#url = "https://api.forecast.io/forecast/<apikey>/<lat>,<long>"
url = "https://api.darksky.net/forecast/575931a71d12136ca98474e07508f6e7/37.8267,-122.4233"
forecast_request = requests.get(url)
query = json.loads(forecast_request.text)
#Generate your text message, remembering to keep it below 160 characters:

str_resp  = "It's %.1f C" % (query['currently']['temperature'])
str_resp += " (feels like %.1f C)." % (query['currently']['apparentTemperature'])

temp_list = [[x['temperature'], x['apparentTemperature']] for x in query['hourly']['data'][0:12]]
temp_list = sorted(temp_list, key=lambda x: x[1])

str_resp += " Low/high for next 12 hours is %.1f (%.1f) / %.1f (%.1f)." %(
		temp_list[0][0], temp_list[0][1],
		temp_list[-1][0], temp_list[-1][1],
		)

if len(str_resp + " " + query['hourly']['summary']) < 160:
	str_resp += " " + query['hourly']['summary']
#This generates messages like the following:

#It's -2.3 C (feels like -4.5 C). Low/high for next 12 hours is
#-2.3 (-4.5) / 3.6 (-0.1). Flurries tonight.
#To send this as an SMS using the voip.ms API, login and then go to their API page to generate an API password, enable the API, and enter the IP address you’ll be making requests from.

#Then, provide parameters for their rest.php endpoint:

def send_sms(dst, text):
	voip_post = {
		"api_username" : "sballard222@gmail.com",
		"api_password" : "Spalding2",
		"method" : "sendSMS",
		"did" : "<your voip.ms DID with SMS enabled>",
		"dst" : dst,
		"message" : text
	}

	base_url = "https://voip.ms/api/v1/rest.php?"
	add_ons = []

	for k in voip_post.keys():
		add_ons.append(k + "=" + voip_post[k])

	url = base_url + "&".join(add_ons)

	voip_result = requests.get(url)
	voip_result = voip_result.text
	voip_result = json.loads(voip_result)

	# optionally check voip_result fields here
#his creates a URL that will resemble

#rest.php?api_username=test@fake.com&api_password=testpostpleaseignore&method=sendSMS&...