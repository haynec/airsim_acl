#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pickle as pk
import math
import numpy as np


# In[17]:


a = pk.load(open("aval.txt", 'rb'))
# 3 column matrix so 3 degrees (x, y, and z axes)
print(a)
len(a)


# In[ ]:


# in calculating pitch and roll angles and throttle, we assumed that the acceleration
# vector is of the form that the axes are ordered as x, y, and z 


# In[32]:


# input: acceleration vector
# output: pitch angle as an array
def pitchCalc(a):
    pitchVals = []
    for acc in a:
        # based on the math that pitch=atan2(accx,sqrt(accy^2+accz^2))
        pitchAng = math.atan2(acc[0],math.sqrt(acc[1]**2 + acc[2]**2))
        pitchVals.append([pitchAng])
    return pitchVals

pitch = pitchCalc(a)
print(pitch)
len(pitch)


# In[31]:


# input: acceleration vector
# output: roll angle as an array
def rollCalc(a):
    rollVals = []
    for acc in a:
        # based on the math that roll=atan2(accy,sqrt(accx^2+accz^2))
        rollAng = math.atan2(acc[1],math.sqrt(acc[0]**2 + acc[2]**2))
        rollVals.append([rollAng])
    return rollVals

roll = rollCalc(a)
print(roll)
len(roll)


# In[34]:


# yaw is defined as 0 as requested
# added the length of the array to be 50 to match those of the pitch and the roll
yaw = np.zeros(50)
print(yaw)
len(50)


# In[ ]:


# need to calculate throttle

