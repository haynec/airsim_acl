import setup_path 
import airsim

import numpy as np
import os
import tempfile
import pprint
import cv2

# connect to the AirSim simulator
client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True)
client.armDisarm(True)

#Drone takes off
client.takeoffAsync().join()

#Drone flies to -20,10,-20 at a speed of 10
airsim.wait_key('Press any key to have Drone begin square')
client.moveToPositionAsync(0,0,-10, 2).join()
state = client.getMultirotorState()
s = pprint.pformat(state)
print("state: %s" % s)
client.moveToPositionAsync(0,10,-10,2).join()
client.moveToPositionAsync(10,10,-10,2).join()
client.moveToPositionAsync(10,0,-10,2).join()
client.moveToPositionAsync(0,0,-10,2).join()



#Drone returns to initial position
airsim.wait_key('Press any key to have Drone return to initial position')
client.goHomeAsync().join()

#Drone lands
client.landAsync().join()

#Disconnect the AirSim simulator
client.enableApiControl(False)