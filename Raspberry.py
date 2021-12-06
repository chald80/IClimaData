# port to broadcast to on UDP
BROADCAST_TO_PORT = 1313
import json
import time
from datetime import datetime
from sense_hat import SenseHat
# create a sensehat obejct
sense = SenseHat()

from socket import *
s = socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_BROADCAST,1)

while True:
	# collection of data from the sensehat
	t = sense.get_temperature()
	h = sense.get_humidity()
	now = datetime.now()
	date_time = now.strftime("%Y-%m-%d, %H:%M:%S")
	
	# RoomId
	r = 1
	# rounds the numbers with 1 decmial
	t = round(t, 1)
	h = round(h, 1)
	# here the json is created
	data_set = {"Date":str(date_time), "Temperature":(t), "Humidity":str(h), "RoomId":"1"}
	json_dump = json.dumps(data_set)
	# here the json is send
	s.sendto(bytes(json_dump, "UTF-8"), ('<broadcast>', BROADCAST_TO_PORT))
	# print the json in the console
	print(json_dump)
	# how often the raspberry sends the data
	time.sleep(1)

