import urllib2
import time
import simplejson as json
import serial

MAX_SERVO = 255.0
MAX_SPEED = 40.0

# The serial port on my machine was number 2
# yours may differ
ser = serial.Serial(2)

while 1:

	try:
		# I like JSON so I choose to use the JSON feed but other formats are avaliable
		data=urllib2.urlopen('http://www.pachube.com/v2/feeds/4037.json?key=YOUR_API_KEY')

		pachubeData = json.loads(data.read())

		for stream in pachubeData["datastreams"]:
			if u'average wind speed' in stream["tags"]: 
				# A crude bit of scaling so that the wind speed is correctly mapped
				# to a position that makes sense on the dial.
				speed = (float(stream[u'current_value'])/(MAX_SPEED/MAX_SERVO))
				val = "%ds" % (speed) 
				ser.write(val)
			
		# The API limits the number of requests you can make
		# I set this to a minute and things seems to be good.
		# You should set this based on how much data you require.
		# Getting the speed of a ship every second would be silly.
		time.sleep(60)
				
	except:
		continue
		
# If you were to productionize this code you would want
# to close the serial connection 		
ser.close()