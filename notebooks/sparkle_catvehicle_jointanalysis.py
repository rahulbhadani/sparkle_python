#!/usr/bin/env python
# Author: Rahul Bhadani

from matplotlib.pyplot import imshow
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
import sys, getopt
import ntpath
from fastdtw import fastdtw
from scipy.spatial.distance import euclidean
import seaborn as sns
argv = sys.argv[1:]
run_id = "run_id"

# Analysis
cmd_speed =[]
speed = []
posX = []
lead_dist = []
rel_vel = []
bagfiles = []

logdir = '/home/refulgent/Cyverse/sparkle/'

real_time_factor = []
controller = []
# bagfiles.append(logdir+'')
# bagfiles.append(logdir+'')
# bagfiles.append(logdir+'')
gui_enabled = []
dynamics = []
N_cars = []
use_odom = []
use_lead_vel = []
update_rate = []

real_time_factor.append('Sparkle RTF 1.0: Sensor Assisted')
real_time_factor.append('Sparkle RTF 1.0: Sensor Assisted')
real_time_factor.append('Sparkle RTF 1.0: Sensor Assisted')
real_time_factor.append('Sparkle RTF 1.0: Sensor Assisted')

# bagfiles.append(logdir+'sparkle_ncars_3_d_bicycle_c_rl_f_1.0_u_20.0_O_False_L_False_G_True_C_True_max_update_rate_100.0_time_step_0.01_recordtime_200.0_dynamics_bicycle_2021-12-22-17-25-32.bag')
# bagfiles.append(logdir+'sparkle_ncars_3_d_bicycle_c_rl_f_1.0_u_20.0_O_False_L_False_G_True_C_True_max_update_rate_100.0_time_step_0.01_recordtime_200.0_dynamics_bicycle_2021-12-22-17-31-58.bag')
# bagfiles.append(logdir+'sparkle_ncars_3_d_bicycle_c_rl_f_1.0_u_20.0_O_False_L_False_G_True_C_True_max_update_rate_100.0_time_step_0.01_recordtime_200.0_dynamics_bicycle_2021-12-22-17-38-18.bag')
# bagfiles.append(logdir+'sparkle_ncars_3_d_bicycle_c_rl_f_1.0_u_20.0_O_False_L_False_G_True_C_True_max_update_rate_100.0_time_step_0.01_recordtime_200.0_dynamics_bicycle_2021-12-22-17-44-36.bag')
bagfiles.append(logdir + 'sparkle_ncars_4_d_bicycle_c_rl_f_1.0_u_20.0_O_True_L_True_G_False_C_True_clock_rate_100.0_clockfactor_1.0_recordtime_200.0_dynamics_bicycle_2021-12-22-20-31-15.bag')

Blist = []
print(bagfiles)
for index, bf in enumerate(bagfiles):
    B = bagreader(bf)
    Blist.append(B)
    cmd_speed_b = []
    speed_b = []
    odom_b = []
    lead_dist_b = []
    relvel_b = []
    for i in range(0, 3):
            # print(i)
            cmdvel_file = B.message_by_topic('/sparkle_{:03d}/cmd_vel'.format(i))
            cmdvel = pd.read_csv(cmdvel_file)
            cmd_speed_b.append(cmdvel)
            
            vel_file = B.message_by_topic('/sparkle_{:03d}/vel'.format(i))
            vel = pd.read_csv(vel_file)
            speed_b.append(vel)
            
            if 'catvehicle' in bf:
                odom_file = B.message_by_topic('/sparkle_{:03d}/odom'.format(i))
            else:
                odom_file = B.message_by_topic('/sparkle_{:03d}/setvel'.format(i))
            odom = pd.read_csv(odom_file)
            odom_b.append(odom)

    # for i in range(1, 3):
    #         # print(i)
    #         leaddist_file = B.message_by_topic('/sparkle_{:03d}/lead_dist'.format(i))
    #         leadist = pd.read_csv(leaddist_file)
    #         lead_dist_b.append(leadist)
            
    #         relvel_file = B.message_by_topic('/sparkle_{:03d}/rel_vel'.format(i))
    #         relvel = pd.read_csv(relvel_file)
    #         relvel_b.append(relvel)
    
    cmd_speed.append(cmd_speed_b)
    speed.append(speed_b)
    posX.append(odom_b)
    lead_dist.append(lead_dist_b)
    rel_vel.append(relvel_b)


# per simuation plot
fig, ax = bagpy.create_fig(nrows = len(cmd_speed), ncols = 2 )
ax = ax.reshape(len(cmd_speed), 2 )
for j in range(0, len(cmd_speed)):
    
    cs = cmd_speed[j]
    s = speed[j]
    ld = lead_dist[j]
    rv = rel_vel[j]
    
    for i, v in enumerate(cs):
        ax[j, 0].scatter(x = 'Time', y = 'linear.x', data = cs[i], s = 1, label = 'vehicle {}'.format(i))
        ax[j, 0].legend()
        ax[j, 0].set_xlabel('Time')
        ax[j, 0].set_ylabel('Speed m/s')
        ax[j, 0].set_title('Commanded Speed for all Vehicles: Simulation {}, ({})'.format(j, real_time_factor[j]), fontsize = 20)

    for i, v in enumerate(s):
        ax[j, 1].scatter(x = 'Time', y = 'linear.x', data = s[i], s = 1, label = 'vehicle {}'.format(i))
        ax[j, 1].legend()
        ax[j, 1].set_xlabel('Time')
        ax[j, 1].set_ylabel('Speed m/s')
        ax[j, 1].set_title('Driving Speed for all Vehicles: Simulation {} ({})'.format(j, real_time_factor[j]), fontsize = 20)

        
plt.suptitle("Run ID: {}".format(run_id), y = 1.001)
plt.tight_layout()
plt.show()

# per simulation plot
fig, ax = bagpy.create_fig(nrows = int(np.ceil(len(cmd_speed)/2)), ncols = 2 )
ax = ax.ravel()
for j in range(0, len(cmd_speed)):
    
    cs = posX[j]

    
    for i, v in enumerate(cs):
        ax[j].scatter(x = 'Time', y = 'pose.pose.position.x', data = cs[i], s = 1, label = 'vehicle {}'.format(i))
        ax[j].legend()
        ax[j].set_xlabel('Time')
        ax[j].set_ylabel('X')
        ax[j].set_title('Position of all Vehicles: Simulation {}, ({})'.format(j, real_time_factor[j]))
        
plt.suptitle("Run ID: {}".format(run_id), y = 1.0001)
plt.tight_layout()
plt.show()

# per simulation plot
fig, ax = bagpy.create_fig(nrows = int(np.ceil(len(lead_dist)/2)), ncols = 2 )
ax = ax.ravel()
for j in range(0, len(lead_dist)):
    
    cs = lead_dist[j]

    
    for i, v in enumerate(cs):
        ax[j].scatter(x = 'Time', y = 'data', data = cs[i], s = 1, label = 'vehicle {}'.format(i+1))
        ax[j].legend()
        ax[j].set_xlabel('Time')
        ax[j].set_ylabel('X')
        ax[j].set_title('Space gaps: Simulation {}, ({})'.format(j, real_time_factor[j]))
        
plt.suptitle("Run ID: {}".format(run_id), y = 1.0001)
plt.tight_layout()


# per simulation plot
fig, ax = bagpy.create_fig(nrows = int(np.ceil(len(rel_vel)/2)), ncols = 2 )
ax = ax.ravel()
for j in range(0, len(rel_vel)):
    
    cs = rel_vel[j]

    
    for i, v in enumerate(cs):
        ax[j].scatter(x = 'Time', y = 'linear.z', data = cs[i], s = 1, label = 'vehicle {}'.format(i+1))
        ax[j].legend()
        ax[j].set_xlabel('Time')
        ax[j].set_ylabel('X')
        ax[j].set_title('Relative Speed: Simulation {}, ({})'.format(j, real_time_factor[j]))
        
plt.suptitle("Run ID: {}".format(run_id), y = 1.0001)
plt.tight_layout()
