#/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 10:36:57 2020

@author: sballard
"""


stn = '185'
startdate = "06/11/2016 2:00"




import numpy as np
import matplotlib.pyplot as plt
from netCDF4 import Dataset
import datetime 
import urllib
import time
import calendar
import numpy.matlib

urlarc = 'http://thredds.cdip.ucsd.edu/thredds/dodsC/cdip/archive/' + stn + 'p1/' + stn + 'p1_historic.nc'

nc = Dataset(urlarc)

timevar = nc.variables['waveTime'][:]

# Find nearest value in numpy array
def find_nearest(array,value):
    idx = (np.abs(array-value)).argmin()
    return array[idx]

# Convert to unix timestamp
def getUnixTimestamp(humanTime,dateFormat):
    unixTimestamp = int(calendar.timegm(datetime.datetime.strptime(humanTime, dateFormat).timetuple()))
    return unixTimestamp

# Convert to human readable timestamp
def getHumanTimestamp(unixTimestamp, dateFormat):
    humanTimestamp = datetime.datetime.utcfromtimestamp(int(unixTimestamp)).strftime(dateFormat)
    return humanTimestamp

unixtimestamp = getUnixTimestamp(startdate, "%m/%d/%Y %H:%M")
unix_nearest = find_nearest(timevar, unixtimestamp)  # Find the closest unix timestamp
neardate = getHumanTimestamp(unix_nearest, '%Y%m%d%H%M') # Convert unix timestamp to string format to attach to URL
url = 'http://cdip.ucsd.edu/data_access/MEM_2dspectra.cdip?sp' + stn + '01' + neardate



data = urllib.request.urlopen(url)
readdata = data.read()

#readdata = str(readdata) # Read text file of recent data
datas = readdata.split() # Split text file into individual rows

##datas = readdata
#datas = readdata.split()
##Create a new array
#
#Split lines into individual objects
#Remove 'pre' characters and filter array for empty objects

datas2 = []

for item in datas:
     line = item.strip().split()
     datas2.append(line)

#datas2[0].remove()
#datas2[72].remove("/n")
datas3 = datas2[1:4608]
#datas3 = filter(None, datas3)
#Change 'datas2' list to 'Ed_array' array
#datas2 = bytes(datas2)
#Append the first colum of 'Ed_array' to the end of 'Ed_array' so that dimensions are (64L,73L), and the last column connects back to the first column. This allows the polar plot to call all 72 (5-degree bin) columns of real data when plotting the colormesh.
datas4 = numpy.matlib.repmat(datas3,64,72)
Edarray = np.array(datas3, dtype=object)
#Edarray = numpy.matlib.repmat(Edarray,64,73)
Ednew = np.append(Edarray,Edarray[:,0:1],1)

#Create Degrees ('Dmean') and Frequency ('Fq') variables to use in plotting Energy Density

#Extract Frequency variable from NetCDF, to use as 'Fq' array
#Create manually-specified Degrees ('Dmean') list, of 5-degree intervals from 0-360

# Fq = np.asarray(np.arange(0.03,0.59,0.01)) # Use this Frequency range option when calling the 'even' option for a station
Fq = nc.variables['waveFrequency']
Dmean = np.asarray(np.arange(2.5,367.5,5))

# Convert 'Dmean' from degrees to radians
rad_convert = (np.pi/270)
Dmean_rad = [d*rad_convert for d in Dmean]


Edmax = np.amax(Ednew)
Edfloat = float(Edmax)
#Plot Polar Spectrum
#Specify radial and angular axes of polar plot
#'radii' = Fq array
#'thetas' = Dmean_rad array
#Define colormesh range
#Change 'thetas' alignment so that 0 Degrees is at the top
#Apply a colormesh (contourf) of Energy Density data to polar plot
#Add colorbar and titles

fig = plt.figure(figsize=(11,11))

radii = Fq[0:35] # Only call frequency bands > 0.3 Hz
thetas = Dmean_rad[:] 


## Color-scale
contour_levels = np.arange(0.00,0.1,0.0001) # Manually set colorbar min/max values
#contour_levels = np.arange(Edfloat/1000,Edfloat/2,0.0001) # Automatically set colorbar min/max values based on 'Ed'
values  = np.array(datas3)
values = values[0:4599]
values = values.reshape(63,73)
 
 #r, theta = np.meshgrid(zeniths, dp.radians(azimuths))

ax = plt.subplot(111, polar=True)
ax.set_theta_direction(-1)
ax.set_theta_zero_location("N")
ylabels = ([20,10,6.7,5,4])
ax.set_yticklabels(ylabels)

colorax = ax.contourf(thetas, radii, values[0:35],contour_levels, cmap = 'RdPu')
#cmap('cubehelix')

## Set titles and colorbar
plt.suptitle('Wave Directional Spectrum at Station. ' + stn, fontsize=22, y=0.95, x=0.45)
plt.title(startdate, fontsize=16, y=1.11)

cbar = fig.colorbar(colorax)
cbar.set_label('Energy Density (m*m/Hz/deg)', rotation=270, fontsize=16)
cbar.ax.get_yaxis().labelpad = 30
fig.colorbar()
degrange = range(0,360,30)
#lines, labels = plt.thetagrids(degrange, labels=None, frac = 1.07)