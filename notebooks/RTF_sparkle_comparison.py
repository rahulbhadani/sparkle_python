#!/usr/bin/env python

# Author: Rahul Bhadani

"""
In this notebook we comparison trajectories obtained from different RTF
"""

import sparkle
import time
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import bagpy
from bagpy import bagreader
from strym import strymread
import datetime
import time

dt_object = datetime.datetime.fromtimestamp(time.time())
dt = dt_object.strftime('%Y-%m-%d-%H-%M-%S-%f')


print(sparkle.__version__)

## RTF 0.25
from sparkle import layout

X = list(np.arange(300,0, -30))
n_vehicles = len(X)
Y = [0]*len(X)
Yaw = [0]*len(X)
max_update_rate = 25.0
time_step = 0.005

print("Real-time factor is {}".format(max_update_rate*time_step))

update_rate = 20.0
log_time = 400.0
description = 'A very basic layout with {} cars on a straightline'.format(len(X))
logdir = '/home/refulgent/Cyverse/sparkle/'

L = layout(n_vehicles=n_vehicles, X=X, Y=Y, Yaw=Yaw, max_update_rate = max_update_rate,
          time_step= time_step, update_rate = update_rate, log_time = log_time, description = description, 
          logdir = logdir)

if L.checkroscore() == True:
    L.destroy()

# start roscore
L.roscore()

L.create(initial_world = '/home/refulgent/catvehicle_ws/src/sparkle/launch/threelanes.launch')
L.spawn(include_laser="all")
L.logdata(logdir = logdir, log_time = log_time)

ctrl_method = ['rl']*len(X)
ctrl_method[0] = 'launch'
ctrl_method

#L.control(control_method = ['launch', 'rl', 'rl', 'rl'], use_lead_vel=True)
L.control(control_method = ctrl_method, use_lead_vel=True)
time.sleep(log_time)
L.destroy()

print(L.bagfile)