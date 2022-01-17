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

dt_object = datetime.datetime.fromtimestamp(time.time())
dt = dt_object.strftime('%Y-%m-%d-%H-%M-%S-%f')

# Analysis
cmd_speed =[]
speed = []
posX = []
lead_dist = []
rel_vel = []
bagfiles = []



# no gui sparkle
#bagfiles.append('/home/refulgent/Cyverse/sparkle/sparkle_n_24_clock_rate_100_clockfactor_0.5_recordtime_1000.0_2021-12-06-00-48-14.bag')
#bagfiles.append('/home/refulgent/Cyverse/sparkle/sparkle_n_24_clock_rate_100_clockfactor_0.2_recordtime_1000.0_2021-12-06-00-09-25.bag')

# bagfiles.append('/home/refulgent/Cyverse/sparkle/sparkle_ncars_4_d_bicycle_c_rl_f_1.0_u_20.0_O_True_L_True_G_True_max_update_rate_100.0_time_step_0.01_recordtime_200.0_dynamics_bicycle_2021-12-08-00-34-36.bag')
# bagfiles.append('/home/refulgent/Cyverse/sparkle/sparkle_ncars_4_d_bicycle_c_rl_f_0.5_u_20.0_O_True_L_True_G_True_max_update_rate_50.0_time_step_0.01_recordtime_200.0_dynamics_bicycle_2021-12-08-00-40-40.bag')


# bagfiles.append('/home/refulgent/Cyverse/sparkle/A_very_basic_layout_testing_with_24_cars_clock_rate_100_clockfactor_0.25_recordtime_200.0_dynamics_unit_dynamics_2021-12-08-14-21-03.bag')
# bagfiles.append('/home/refulgent/Cyverse/sparkle/A_very_basic_layout_testing_with_24_cars_clock_rate_100_clockfactor_0.5_recordtime_200.0_dynamics_unit_dynamics_2021-12-08-14-44-44.bag')


# bagfiles.append('/home/refulgent/Cyverse/sparkle/A_very_basic_layout_testing_with_24_cars_clock_rate_100_clockfactor_0.25_recordtime_200.0_dynamics_bicycle_2021-12-08-15-21-47.bag')

# bagfiles.append('/home/refulgent/Cyverse/sparkle/A_very_basic_layout_testing_with_24_cars_clock_rate_100_clockfactor_0.5_recordtime_200.0_dynamics_bicycle_2021-12-08-21-15-21.bag')

bagfiles.append('/home/refulgent/Cyverse/sparkle/sparkle_ncars_4_d_bicycle_c_rl_f_1.0_u_20.0_O_True_L_True_G_False_clock_rate_100.0_clockfactor_1.0_recordtime_200.0_dynamics_bicycle_2021-12-08-23-33-32.bag')

bagfiles.append('/home/refulgent/Cyverse/sparkle/sparkle_ncars_4_d_bicycle_c_rl_f_0.5_u_20.0_O_True_L_True_G_False_clock_rate_50.0_clockfactor_0.5_recordtime_200.0_dynamics_bicycle_2021-12-08-23-39-50.bag')

n_cars = 4
Blist = []
for bf in bagfiles:
    B = bagreader(bf)
    Blist.append(B)
    cmd_speed_b = []
    speed_b = []
    odom_b = []
    lead_dist_b = []
    relvel_b = []
    for i in range(0, n_cars):
            # print(i)
            cmdvel_file = B.message_by_topic('/sparkle_{:03d}/cmd_vel'.format(i))
            cmdvel = pd.read_csv(cmdvel_file)
            cmd_speed_b.append(cmdvel)
            
            vel_file = B.message_by_topic('/sparkle_{:03d}/vel'.format(i))
            vel = pd.read_csv(vel_file)
            speed_b.append(vel)
            
            odom_file = B.message_by_topic('/sparkle_{:03d}/setvel'.format(i))
            odom = pd.read_csv(odom_file)
            odom_b.append(odom)
            
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
        ax[j, 0].set_title('Commanded Speed for all Vehicles: Simulation {}'.format(j))

    for i, v in enumerate(s):
        ax[j, 1].scatter(x = 'Time', y = 'linear.x', data = s[i], s = 1, label = 'vehicle {}'.format(i))
        ax[j, 1].legend()
        ax[j, 1].set_xlabel('Time')
        ax[j, 1].set_ylabel('Speed m/s')
        ax[j, 1].set_title('Driving Speed for all Vehicles: Simulation {}'.format(j))
        
fig.show()
#fig.savefig("persimulationplots_RTFhalf_vs_quarter_{}.png".format(dt), dpi = 100, bbox_inches='tight')


# overlaid plot
fig, ax = bagpy.create_fig(ncols = 2, nrows = int(np.ceil(n_cars/2)))

# p = [0]    
# for k in range(1, len(cmd_speed)):
#     p1 = strymread.time_shift(df1=cmd_speed[0][0], df2=cmd_speed[k][0], msg_col1 = 'linear.x', msg_col2='linear.x')
#     p.append(p1)

for j in range(0, len(cmd_speed[0])):
    
    # print('Vehicle: {}'.format(j))
    p = [0, 0.0]
    #scale = [1.0, 2.0]
    marker = ["o", "v", "s"]
    s= [2.0, 2.0, 2.0]
    
    lb = [  'Simulation 1: Factor = 0.25', \
            'Simulation 1: Factor = 0.50']

    for k in range(0, len(cmd_speed)):

        time = cmd_speed[k][j]['Time'].tolist()
        ax[j].scatter(x= cmd_speed[k][j]['Time'] + p[k], y = cmd_speed[k][j]['linear.x']  ,  s = s[k], label = lb[k] + " commanded speed", marker =marker[k])

        ax[j].scatter(x= speed[k][j]['Time'] + p[k], y = speed[k][j]['linear.x']  ,  s = s[k], label = lb[k] + " driving speed", marker =marker[k])

    

    ax[j].legend()
    ax[j].set_xlabel('Time')
    ax[j].set_ylabel('Speed m/s')
    ax[j].set_title('Commanded Speed for Vehicle {}'.format(j))
    fig.show()


fig, ax = bagpy.create_fig(ncols = 2, nrows = int(np.ceil(n_cars/2)))
for j in range(0, len(cmd_speed[0])):
    p = [0, 0.0]
    marker = ["o", "v", "s"]
    s= [2.0, 2.0, 2.0]    
    lb = [  'Simulation 1: Factor = 0.25', \
            'Simulation 1: Factor = 0.50']

    for k in range(0, len(cmd_speed)):

        time = cmd_speed[k][j]['Time'].tolist()
        ax[j].scatter(x= np.arange(0, cmd_speed[k][j].shape[0]) + p[k], y = cmd_speed[k][j]['linear.x']  ,  s = s[k], label = lb[k] + ' commanded speed', marker =marker[k])

        ax[j].scatter(x= np.arange(0, speed[k][j].shape[0]) + p[k], y = speed[k][j]['linear.x']  ,  s = s[k], label = lb[k] + ' driving speed', marker =marker[k])
        

    ax[j].legend()
    ax[j].set_xlabel('Time')
    ax[j].set_ylabel('Speed m/s')
    ax[j].set_title('Commanded Speed for Vehicle {}'.format(j))
    fig.show()
    

B0 = Blist[0]
clock_file = B0.message_by_topic('/clock')
clock_df1 = pd.read_csv(clock_file)
clock_df1['Total_Time'] = clock_df1['clock.secs'] + clock_df1['clock.nsecs']*1e-9
clock_df1['Tdiff'] =clock_df1['Total_Time'].diff()

B1 = Blist[1]
clock_file = B1.message_by_topic('/clock')
clock_df2 = pd.read_csv(clock_file)
clock_df2['Total_Time'] = clock_df2['clock.secs'] + clock_df2['clock.nsecs']*1e-9
clock_df2['Tdiff'] =clock_df2['Total_Time'].diff()


# overlaid plot
fig, ax = plt.subplots(int(np.ceil(n_cars/2)), 2)
ax = ax.ravel()
for j in range(0, len(cmd_speed[0])):
    marker = ["o", "v", "s"]
    s= [2.0, 2.0, 2.0]
    lb = [  'Simulation 0: Factor = 0.25', \
            'Simulation 1: Factor = 0.50']

    ax2 = ax[j].twiny()
    axx = [ax[j], ax2]

    color =['green', 'red']
    legend_loc = ['upper right', 'upper left']
    for k in range(0, len(cmd_speed)):

        time = cmd_speed[k][j]['Time'].tolist()

        t0 = cmd_speed[k][0][cmd_speed[k][0]['linear.x'] > 0].iloc[0]['Time']
        axx[k].scatter(x= cmd_speed[k][j]['Time'] - t0, y = cmd_speed[k][j]['linear.x']  ,  s = s[k], label = lb[k], marker =marker[k], c=color[k])

        axx[k].grid(True)

        axx[k].tick_params(axis='x', labelcolor=color[k])
    

        axx[k].legend(loc=legend_loc[k])
        axx[k].set_xlabel('Time [s] (Simulation {})'.format(k))

    ax[j].set_ylabel('Speed m/s')
    ax[j].set_title('Commanded Speed for Vehicle {}'.format(j))
    fig.tight_layout() 
    fig.show()


# overlaid plot
fig, ax = plt.subplots(int(np.ceil(n_cars/2)), 2)
ax = ax.ravel()
for j in range(0, len(cmd_speed[0])):
    marker = ["o", "v", "s"]
    s= [22.0, 2.0, 2.0]
    lb = [  'Simulation 0: Factor = 0.25', \
            'Simulation 1: Factor = 0.50']
    color =['green', 'red']
    legend_loc = ['upper right', 'upper left']
    for k in range(0, len(cmd_speed)):
        time = cmd_speed[k][j]['Time'].tolist()
        t0 = cmd_speed[k][0][cmd_speed[k][0]['linear.x'] > 0].iloc[0]['Time']
        ax[j].scatter(x= cmd_speed[k][j]['Time'] - t0, y = cmd_speed[k][j]['linear.x']  ,  s = s[k], label = lb[k], marker =marker[k], c=color[k])
    ax[j].legend(loc=legend_loc[k])
    ax[j].set_xlabel('Time [s] (Simulation {})'.format(k))
    ax[j].set_ylabel('Speed m/s')
    ax[j].set_title('Commanded Speed for Vehicle {}'.format(j))
    fig.tight_layout() 
    fig.show()