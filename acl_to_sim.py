import pickle as pk
import math
import numpy as np
import airsim
import os
import tempfile
import pprint
import cv2


# connect to the AirSim simulator
client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True)
client.armDisarm(True)

client.takeoffAsync().join()

client.moveToPositionAsync(-10, 10, -10, 5).join()

#takes in position, velocity, accleration in NED coordinate frame
r = pk.load(open("rval.txt", 'rb'))
v = pk.load(open("vval.txt", 'rb'))
a = pk.load(open("aval.txt", 'rb'))
dtau = pk.load(open("dtauval.txt", 'rb'))

#print(v)
print(v[0])
print(v[0][1])
print(v[0][2])
#print(v[0][3])

client.moveByVelocityAsync(v[0][0], v[0][1], v[0][2], dtau).join()

#def xmatrix()
#    x_m = [1 0 0
#           0 math.cos(gamma) -math.sin(gamma)
#           0 math.sin(gamma) math.cos(gamma)]

