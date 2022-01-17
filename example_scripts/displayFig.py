#!/usr/bin/env python
#
# Author: Rahul Bhadani
# Copyright (c) 2019 Rahul Bhadani, Arizona Board of Regents
# All rights reserved.
import pandas as pd
import sys, math, time, datetime
import matplotlib.pyplot as pt
import matplotlib.animation as animation
from matplotlib import style
import numpy as np
from matplotlib.pyplot import cm
import pickle


# Load figure from disk and display
fileName1 = '/home/ivory/CyverseData/PandaData/2020_02_03/2020-02-03-12-36-29-522681__CAN_Message_.pickle'
#fileName2 = '/home/ivory/VersionControl/catvehicle_ws/src/sparkle/src/Consolidated Plot/
fig_handle1 = pickle.load(open(fileName1,'rb'))

# ax = pt.gca()
# lines = ax.lines[0]
# x1 = lines.get_xdata()
# y1 = lines.get_ydata()

#fig_handle2 = pickle.load(open(fileName2,'rb'))

# ax = pt.gca()
# lines = ax.lines[0]
# x2 = lines.get_xdata()
# y2 = lines.get_ydata()


# pt.plot(x1, y1)
# pt.plot(x2, y2)
# ax = fig_handle1.add_subplot(1,1,1)
# ax.legend(['Simulation with 0.75 RTF - 9 Cars only - plot for first car', 'Simulation with 0.75 RTF - 1 Car only - plot for first car' ])
pt.show()