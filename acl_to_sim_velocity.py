import pickle as pk
import airsim
from airsim import Vector3r, Quaternionr, Pose
from airsim.utils import to_quaternion
import numpy as np
import pprint
import time



# connect to the AirSim simulator
client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True)
client.armDisarm(True)

#takes in position, velocity, accleration in NED coordinate frame
#multiplied by 100 to account for conversion from m to cm in UE4
r = pk.load(open("rval.txt", 'rb'))*100
v = pk.load(open("vval.txt", 'rb'))*100
a = pk.load(open("aval.txt", 'rb'))*100
tau = float(pk.load(open("tauval.txt", 'rb')))
step = len(r)

#Plotting expected trajectory from drone_min_time
client.simFlushPersistentMarkers()

client.simPlotLineStrip(points = [Vector3r(x_val=r[x][0], y_val=r[x][1], z_val=r[x][2]-10) for x in range(0,step)],color_rgba=[1.0, 0.0, 0.0, 1.0], thickness = 5, is_persistent = True)

# plot transforms
#client.simPlotStrings(strings = ["Microsoft AirSim" for i in range(5)], positions = [Vector3r(x,y,-1) for x, y in zip(np.linspace(0,5,5), np.linspace(0,0,5))],
#                        scale = 1, color_rgba=[1.0, 1.0, 1.0, 1.0], duration = 1200.0)

#Drone takes off
client.takeoffAsync().join()


# Ascend to starting position
client.moveToPositionAsync(0, 0, -10, 5)


airsim.wait_key('Press any key to enact ACL maneuver')
for x in range(1, step):
    #client.moveByVelocityAsync(v[x][0], v[x][1], v[x][2], tau)
    task = client.moveToPositionAsync(r[x][0], r[x][1], r[x][2]-10, np.linalg.norm(v[x]))

    #get feedback from UAV for plotting purposes

    current_time = 0
    start_time = time.time()
    finished = False
    while not finished:
        groundtruth = client.getMultirotorState()
        position = groundtruth.kinematics_estimated.position
        velocity = groundtruth.kinematics_estimated.linear_velocity
        acceleration = groundtruth.kinematics_estimated.linear_acceleration
        current_time = groundtruth.timestamp
        finished = task.is_done()
        if current_time - start_time > 500*1000000:
            print(position)
            client.simPlotArrows()
            start_time = current_time

#return to original state
airsim.wait_key('Press any key to reset to original state')

client.armDisarm(False)
client.reset()

