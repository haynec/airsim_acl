import setup_path
import airsim
import numpy as np
import os
import tempfile
import pprint
import cv2
import time
import csv

# connect to the Airsim simulator
client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True)


while True:
	state = client.getMultirotorState()
	s = pprint.pformat(state)
	print('state: %s' % s)
	with open('log.csv', mode='w') as log_file:
		log_writer = csv.writer(log_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		log_writer.writerows(s)
		
	time.sleep(0.01)
