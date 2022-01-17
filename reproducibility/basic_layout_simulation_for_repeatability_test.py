#!/usr/bin/env python
# Author: Rahul Bhadani

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
from sparkle import layout
import rospkg
import os

import sys, getopt

argv = sys.argv[1:]

max_update_rate = 50.0 #m # same as clock rate when no gui
time_step = 0.01 #t
update_rate = 20.0 #u
log_time = 200.0 #l
dynamics = 'bicycle' #d
controller = 'rl' #c
use_lead_vel = False #L
use_odom = False #O
enable_gui = False #G
newclock = False #C
run_id = "run_id" #r
ncars = 24 #n
robot_model = 'sparkle' #b
standalone = False
hoffman = False #H, for steering control.


try:
    opts, args = getopt.getopt(argv,"HSCOLGhm:t:u:l:d:c:r:n:b:",["hoffman", "standalone", "newclock", "use_odom", "use_lead_vel", "enable_gui", "max_update_rate=", "time_step=", "update_rate=","log_time=","dynamics=","controller=","run_id=", "ncars=", "robot_model="])
    if len(opts) == 0:
        print('Check options by typing:\n{} -h'.format(__file__))
        sys.exit()

except getopt.GetoptError:
    print(getopt.GetoptError)
    print('Option Error. Check options by typing:\n{} -h'.format(__file__))
    sys.exit(2)

print("OPTS: {}".format(opts))
for opt, arg in opts:
    if(opt == '-h'):
        print('\n{} [OPTIONS]'.format(__file__))
        print('\t -h, --help\t\t Get help')
        print('\t -m, --max_update_rate\t Maximum Update Rate for Physics Engine (Gazebo). E.g. --max_update_rate=100.0')
        print('\t -n, --ncars\t\t Total number of cars for the simulation. E.g. --ncars=5')
        print('\t -t, --time_step\t Time Step of Gazebo. E.g. --time-step=0.01')
        print('\t -u, --update_rate\t Update Rate specified for state evolution of dynamics. E.g. --update_rate=20.0')
        print('\t -l, --log_time\t\t Amount of seconds to run simulation (approximately). E.g. --log_time=200.0')
        print('\t -d, --dynamics\t\t Choose vehicle dynamics. Current options: [bicycle, unit_dynamics]. Available options: [bicylce, unit_dynamics]. E.g --dynamics=bicycle')
        print('\t -c, --controller\t Controller to choose from for follower vehicles (except leader in Platoons). Available options: [rl, launch, injector]. E.g. --controller=rl')
        print('\t -r, --run_id\t\t Run ID to distinguish specific. Use any random alphanumric string. E.g. --run_id=abcdefg')
        print('\t -b, --robot_model\t Specify Robot Model for the car. Available options: [catvehicle, sparkle]. E.g. --robot_model=sparkle')
        print('\t -S, --standalone\t Standalone robot update: no director synchronization (boolean)')
        print('\t -C, --newclock\t\t Use custom simulated clock (boolean)')
        print('\t -O, --use_odom\t\t Use true odometry information for vehicle control (boolean)')
        print('\t -L, --use_lead_vel\t Use true leader velocity information for vehicle control (boolean)')
        print('\t -G, --enable_gui\t Enable 3D Physics Visualization and Sensors (boolean)')
        print('\t -H, --hoffman\t\t Use steering control from Hoffman Controller for keeping vehicles in a straightline (boolean)')
        sys.exit()
    elif(opt in ("-m", "--max_update_rate")):
        max_update_rate  = eval(arg)
    elif(opt in ("-t", "--time_step")):
        time_step  = eval(arg)
    elif(opt in ("-n", "--ncars")):
        ncars  = eval(arg)
    elif(opt in ("-u", "--update_rate")):
        update_rate  = eval(arg)
    elif(opt in ("-l", "--log_time")):
        log_time  = eval(arg)
    elif(opt in ("-d", "--dynamics")):
        dynamics  = arg
    elif(opt in ("-c", "--controller")):
        controller  = arg
    elif(opt in ("-r", "--run_id")):
        run_id  = arg
    elif(opt in ("-b", "--robot_model")):
        robot_model = arg
    elif(opt in ("-S", "--standalone")):
        standalone = True
    elif(opt in ("-C", "--newclock")):
        newclock = True
    elif(opt in ("-O", "--use_odom")):
        use_odom = True
    elif(opt in ("-L", "--use_lead_vel")):
        use_lead_vel = True
    elif(opt in ("-G", "--enable_gui")):
        enable_gui = True
    elif(opt in ("-H", "--hoffman")):
        hoffman = True

clock_factor = max_update_rate*time_step


homedir = os.path.expanduser('~')
logdir = homedir + '/Cyverse/sparkle/'
os.makedirs(logdir, exist_ok=True)


dt_object = datetime.datetime.fromtimestamp(time.time())
dt = dt_object.strftime('%Y-%m-%d-%H-%M-%S-%f')

X = list(np.linspace(30*int(ncars-1),0,int(ncars)))
n_vehicles = len(X)
Y = [0]*len(X)
Yaw = [0]*len(X)



description = '{}_ncars_{}_d_{}_c_{}_f_{}_u_{}_O_{}_L_{}_G_{}_C_{}'.format(robot_model, len(X), dynamics, controller, clock_factor, update_rate, use_odom, use_lead_vel, enable_gui, newclock)

print("Description:{}".format(description))
print("Real Time Factor is {}".format(clock_factor))

L = layout(n_vehicles=n_vehicles, X=X, Y=Y, Yaw=Yaw, max_update_rate = max_update_rate,
          time_step= time_step, update_rate = update_rate, log_time = log_time, 
          description = description, logdir = logdir, enable_gui = enable_gui,
          standalone = standalone)

if L.checkroscore() == True:
    L.destroy()

L.roscore()

# wait until ROS core starts
while(True):
    if L.checkroscore():
        break

print("max_update_rate = {}".format(max_update_rate))
print("time_step = {}".format(time_step))
print("update_rate = {}".format(update_rate))
print("use_odom = {}".format(use_odom))
print("use_lead_vel = {}".format(use_lead_vel))
print("enable_gui = {}".format(enable_gui))
print("newclock = {}".format(newclock))
print("clock_factor = {}".format(clock_factor))

time.sleep(15)

rospack = rospkg.RosPack()
sparkle_pkg =  rospack.get_path('sparkle')
if enable_gui:
    L.create(initial_world = sparkle_pkg + '/launch/threelanes.launch', clock_factor = clock_factor, rate = max_update_rate, newclock = newclock)
else:
    L.create(clock_factor = clock_factor, rate = max_update_rate, newclock = newclock)

robot_pkg = rospack.get_path(robot_model)

L.spawn(include_laser="followers", dynamics = dynamics, robot_pkg = robot_pkg)
L.logdata(logdir = logdir, log_time = log_time)

ctrl_method = [controller]*len(X)
ctrl_method[0] = 'launch'
ctrl_method

L.control(control_method = ctrl_method, use_lead_vel=use_lead_vel, use_odom = use_odom, hoffman = hoffman)
time.sleep(log_time/clock_factor)
L.destroy()

# Write down the bagfile to

with open(logdir+run_id + '.txt', 'a') as f:
    f.write(L.bagfile)
    f.write("\n")