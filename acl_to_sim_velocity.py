import pickle as pk
import airsim



# connect to the AirSim simulator
client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True)
client.armDisarm(True)

client.takeoffAsync().join()

#Ascend to starting position
client.moveToPositionAsync(0, 0, -10, 5).join()

#takes in position, velocity, accleration in NED coordinate frame
#multiplied by 100 to account for conversion from m to cm in UE4
r = pk.load(open("rval.txt", 'rb'))*100
v = pk.load(open("vval.txt", 'rb'))*100
a = pk.load(open("aval.txt", 'rb'))*100
dtau = float(pk.load(open("dtauval.txt", 'rb')))

step = len(r)

airsim.wait_key('Press any key to enact ACL maneuver')
for x in range(0,step):
    client.moveByVelocityAsync(v[x][0], v[x][1], v[x][2], dtau).join()

#return to original state
airsim.wait_key('Press any key to reset to original state')

client.armDisarm(False)
client.reset()

