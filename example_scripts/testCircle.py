#!/usr/bin/env python
#
# Author: Rahul Bhadani
# Copyright (c) 2019 Rahul Bhadani, Arizona Board of Regents
# All rights reserved.

import matlab.engine
import pandas as pd
import matplotlib.pyplot as pt
import matplotlib.animation as animation
from matplotlib import style
import datetime
import time
import sys, math, time
import signal
import subprocess, shlex
from subprocess import call
import psutil
import numpy as np
import matlab.engine
import glob
import os
from gzstats import gzstats
from circle import circle
# dt_object = datetime.datetime.fromtimestamp(time.time())
# dt = dt_object.strftime('%Y-%m-%d-%H-%M-%S-%f')
    
# gzstatsFile ='./gz_stats_' + dt + '.txt'
# gzstats = subprocess.Popen(["gz stats > " + gzstatsFile ], stdout=subprocess.PIPE, shell=True)
# gzstatsPID =   gzstats.pid


# ls = subprocess.Popen(["ls" , "-lrt" ], stdout=subprocess.PIPE, shell=True)
# lsPID =   ls.pid

# (oo, ee) = ls.communicate()

# print(oo)


# time.sleep(10)
# gzstats.terminate()

# print("## terminated #.")

#G = gzstats('Circle_Test_n_20_updateRate_1_2019-12-02-13-13-35_gzStats.txt')
#G.plotRTF()
#G.plotSimStatus()



simConfig = {"circumference": 260.0, "num_vehicle":  2, "update_rate": 1, "log_time": 90.0, "max_update_rate": 30.0, "time_step": 0.01}
cl = circle(**simConfig)