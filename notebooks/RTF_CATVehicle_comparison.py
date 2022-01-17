#!/usr/bin/env python

# Author: Rahul Bhadani

"""
In this notebook we comparison trajectories obtained from different RTF
"""
import catvehicle
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from catvehicle import layout
X = list(np.arange(300,0, -30))
n_vehicles = len(X)
Y = [0]*len(X)
Yaw = [0]*len(X)
max_update_rate = 25.0
time_step = 0.01


update_rate = 20.0
log_time = 400.0

description = 'A very basic layout with {} catvehicles on a straightline'.format(len(X))
logdir = '/home/refulgent/Cyverse/sparkle/'

L = layout(n_vehicles=n_vehicles, X=X, Y=Y, Yaw=Yaw, max_update_rate = max_update_rate,
          time_step= time_step,  log_time = log_time, description = description, 
          logdir = logdir)

L.roscore()

L.create(initial_world = '/home/refulgent/catvehicle_ws/src/sparkle/launch/threelanes.launch')

l = [i+1 for i in range(len(X)-1)]
L.spawn(include_laser=l)
L.logdata(logdir = logdir, log_time = log_time)
ctrl = ['rl']*len(X)
ctrl[0] = 'launch'
L.control(control_method = ctrl)
time.sleep(log_time)
L.destroy()