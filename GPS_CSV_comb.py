import time
import serial
import string
from pynmea import nmea
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import matplotlib.animation as animation
import csv

ser = serial.Serial()
ser.port = "/dev/ttyUSB0"
ser.baudrate = 9600
ser.timeout = 1
ser.open()
gpgga = nmea.GPGGA()


data = ['LATITUDE', 'LONGITUDE']

with open('GPS_combi_file.csv', 'w') as f:
	update = csv.writer(f)
	update.writerow(data)


plt.plot([8123,8265],[5126,5443],linewidth=3,linestyle="-",c='red',alpha = 0.3)
#plt.plot(8265,5243,'g^')
while True:
    data = ser.readline()
    if data[0:6] == '$GPGGA':
        ##method for parsing the sentence
        gpgga.parse(data)
        lats = gpgga.latitude
        print "Latitude values : " + str(lats)

        longs = gpgga.longitude
        print "Longitude values : " + str(longs)

        print ' '

        lat = str(lats)
        lon = str(longs)
        lat = lat[5:9]
        lon = lon[6:10]
	data1 = [lats,longs]
	
	with open('GPS_combi_file.csv', 'a+') as f:
	    update = csv.writer(f)
	    update.writerow(data1)	

        print lat, lon
        plt.ion()
        plt.axis([8000,9000,5000,6000])
        plt.plot(lat,lon,'g^', alpha = 1)
        plt.pause(1)
          


    
        

        

        
