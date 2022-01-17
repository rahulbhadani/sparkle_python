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

# try:
#     opts, args = getopt.getopt(argv,"hr:",["run_id="])
#     if len(opts) == 0:
#         print('Check options by typing:\n{} -h'.format(__file__))
#         sys.exit()
# except getopt.GetoptError:
#     print('Check options by typing:\n{} -h'.format(__file__))
#     sys.exit(2)

# print("OPTS: {}".format(opts))
# for opt, arg in opts:
#     if(opt == '-h'):
#         print('\n{} [OPTIONS]'.format(__file__))
#         print('\t -h, --help\t\t Get help')
#         print('\t -r, --run_id\t Run ID to distinguish specific ')
#         sys.exit()
#     elif(opt in ("-r", "--run_id")):
#         run_id  = arg


# run_id = "6b75bfb6bf43b294cae1"
# run_id = "12268da8a56f3c1de068"
#run_id = "6746d039d5c0174d4687"
run_id = "0b4dd8ad903c9d03e0b7"
run_id = "08b6a72b42bbda416e8d"
run_id = "d125f74cb495c2bb5ca7"
run_id = "3cb8a01654c5599b48a5"
run_id = "57d290c0a31167357976"
run_id = "fee25aca5ca6ba94e0c4"
run_id = "8ec760d7e69c71186467"
run_id = "518804d6cccd33ce132f"
run_id = "4642f9be1b3b791ca653"
run_id = "6bcd78ea7e445fc01213"
run_id = "ff4da50c05473ef35e9f"
run_id = "d4c28c7a8468b4d5d264"
run_id = "a9caf9d1cb5f669b0656"
run_id = "8f6e911f72d2a26a71d3"
run_id = "d1d39407e2dc464252ef"
run_id = "9aeeaedfc60a4c876d35"
run_id = "13f408d7972cd139b8a6"
run_id = "4bc0747bc56b57674355"
run_id = "cb14c938de68a130590c"
#run_id = "d9a4a64bde7c5299972e"
run_id = "505a4242fe8f60fe533c"
run_id = "9c6a5bee68c22bb7c1e5"
run_id = "2d17d35c077fb9cc2d2e"
run_id = "016eeb535255aa58ccee"
run_id = "a0bd74de602fe4692f51"
run_id = "fae74d175ff7f6293f18"
run_id = "cf8de74918582d8506c2"
run_id = "863cefbd79fabca6ac91"

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
gui_enabled = []
dynamics = []
N_cars = []
use_odom = []
use_lead_vel = []
update_rate = []

Lines = None
with open(logdir+run_id + '.txt', 'r') as f:
    Lines = f.readlines()
    
for i, Line in enumerate(Lines):
    Line = Line.strip()
    bagfiles.append(Line)
    splits = Line.split('_')
    N_cars.append(int(splits[splits.index('ncars') + 1]))
    dynamics.append(splits[splits.index('d') + 1])
    controller.append(splits[splits.index('c') + 1])
    real_time_factor.append('Sparkle Simulation {}, RTF '.format(i) + splits[splits.index('f') + 1])
    gui_enabled.append(splits[splits.index('G') + 1])
    use_odom.append(splits[splits.index('O') + 1])
    use_lead_vel.append(splits[splits.index('L') + 1])
    update_rate.append(splits[splits.index('u') + 1])

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
    for i in range(0, N_cars[index]):
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
            
    cmd_speed.append(cmd_speed_b)
    speed.append(speed_b)
    posX.append(odom_b)
    lead_dist.append(lead_dist_b)
    rel_vel.append(relvel_b)


# # per simuation plot
# fig, ax = bagpy.create_fig(nrows = len(cmd_speed), ncols = 2 )
# ax = ax.reshape(len(cmd_speed), 2 )
# for j in range(0, len(cmd_speed)):
    
#     cs = cmd_speed[j]
#     s = speed[j]
#     ld = lead_dist[j]
#     rv = rel_vel[j]
    
#     for i, v in enumerate(cs):
#         ax[j, 0].scatter(x = 'Time', y = 'linear.x', data = cs[i], s = 1, label = 'vehicle {}'.format(i))
#         ax[j, 0].legend()
#         ax[j, 0].set_xlabel('Time')
#         ax[j, 0].set_ylabel('Speed m/s')
#         ax[j, 0].set_title('Commanded Speed for all Vehicles: Simulation {}, ({})'.format(j, real_time_factor[j]), fontsize = 20)

#     for i, v in enumerate(s):
#         ax[j, 1].scatter(x = 'Time', y = 'linear.x', data = s[i], s = 1, label = 'vehicle {}'.format(i))
#         ax[j, 1].legend()
#         ax[j, 1].set_xlabel('Time')
#         ax[j, 1].set_ylabel('Speed m/s')
#         ax[j, 1].set_title('Driving Speed for all Vehicles: Simulation {} ({})'.format(j, real_time_factor[j]), fontsize = 20)

        
# plt.suptitle("Run ID: {}".format(run_id), y = 1.001)
# plt.tight_layout()
# plt.savefig(logdir + run_id + '_speed_all_plot.png', bbox_inches='tight')
# plt.savefig(logdir + run_id + '_speed_all_plot.pdf', bbox_inches='tight')
# plt.show()

# per simuation plot
# fig, ax = bagpy.create_fig(nrows = len(cmd_speed), ncols = 2 )
import matplotlib as mpl
mpl.rcParams.update(mpl.rcParamsDefault)
fig, ax = plt.subplots(len(cmd_speed), ncols = 2, figsize=(12, 18))
ax = ax.reshape(len(cmd_speed), 2 )
for j in range(0, len(cmd_speed)):
    
    cs = cmd_speed[j]
    s = speed[j]
    ld = lead_dist[j]
    rv = rel_vel[j]
    
    max_start_time_1 = cs[0]['Time'].iloc[0]
    max_start_time_2 = s[0]['Time'].iloc[0]
    
    min_end_time_1 = cs[0]['Time'].iloc[-1]
    min_end_time_2 = s[0]['Time'].iloc[-1]

    for i, v in enumerate(cs):
        if (max_start_time_1 < cs[i]['Time'].iloc[0]):
            max_start_time_1 = cs[i]['Time'].iloc[0]
        if (min_end_time_1 > cs[i]['Time'].iloc[-1]):
            min_end_time_1 = cs[i]['Time'].iloc[-1]
        ax[j, 0].scatter(x = 'Time', y = 'linear.x', data = cs[i], s = 1, label = 'vehicle {}'.format(i))
        #ax[j, 0].legend()
        ax[j, 0].set_xlabel('Time', fontsize = 20)
        ax[j, 0].set_ylabel('Speed m/s', fontsize = 20)
        ax[j, 0].set_title('Simulation {}'.format(j), fontsize = 24)
        ax[j, 0].tick_params(axis='both', which='major', labelsize=18)
        ax[j, 0].tick_params(axis='both', which='minor', labelsize=16)

    ax[j, 0].set_xlim(max_start_time_1, min_end_time_1)

    for i, v in enumerate(s):
        if (max_start_time_2 < s[i]['Time'].iloc[0]):
            max_start_time_2 = s[i]['Time'].iloc[0]
        if (min_end_time_2 > s[i]['Time'].iloc[-1]):
            min_end_time_2 = s[i]['Time'].iloc[-1]
        ax[j, 1].scatter(x = s[i]['Time'], y = np.sqrt(s[i]['linear.x']**2 + s[i]['linear.y']**2), s = 1, label = 'vehicle {}'.format(i))
        #ax[j, 1].legend()
        ax[j, 1].set_xlabel('Time', fontsize = 20)
        ax[j, 1].set_ylabel('Speed m/s', fontsize = 20)
        ax[j, 1].set_title('Simulation {}'.format(j), fontsize = 24)
        ax[j, 1].tick_params(axis='both', which='major', labelsize=18)
        ax[j, 1].tick_params(axis='both', which='minor', labelsize=16)

    ax[j, 1].set_xlim(max_start_time_2, min_end_time_2)

# plt.suptitle("Run ID: {}".format(run_id), y = 1.001)
plt.suptitle("Left: Commanded Speed. Right: Driving Speed\n Sparkle Simulation, Modified Approach", y = 1.001, fontsize = 32)
plt.tight_layout()
plt.savefig(logdir + run_id + '_speed_all_plot.png', bbox_inches='tight')
plt.savefig(logdir + run_id + '_speed_all_plot.pdf', bbox_inches='tight')
plt.show()


max_car = np.max(N_cars)
figheight = fig.get_figheight()/len(cmd_speed)
fig, ax = bagpy.create_fig(nrows = int(np.ceil(max_car/2)), ncols = 2 )
fig.set_figheight( fig.get_figheight()*2)
ax = ax.ravel()
for j in range(0, len(cmd_speed[0])):
    
    s_i = 120
    for k in range(0, len(cmd_speed)):
        time = cmd_speed[k][j]['Time'].tolist()
        t0 = cmd_speed[k][0][cmd_speed[k][0]['linear.x'] > 0].iloc[0]['Time']
        ax[j].scatter(x= cmd_speed[k][j]['Time'] - t0, y = cmd_speed[k][j]['linear.x']  ,  s = s_i, label = 'Factor = {}'.format(real_time_factor[k]))

        s_i = s_i - 40
        if(s_i <10):
            s_i = 10
    ax[j].legend(loc='upper right', fontsize = 20)
    ax[j].set_xlabel('Time [s]')
    ax[j].set_ylabel('Speed m/s')
    ax[j].set_title('Commanded Speed for Vehicle {}'.format(j))

plt.suptitle("Run ID: {}".format(run_id), y = 1.001)
plt.tight_layout()
plt.savefig(logdir + run_id + '_cmdspeed_overlaid_zero_trimmed.png', bbox_inches='tight')
plt.savefig(logdir + run_id + '_cmdspeed_overlaid_zero_trimmed.pdf', bbox_inches='tight')
plt.show()

figheight = fig.get_figheight()/len(speed)
fig, ax = bagpy.create_fig(nrows = int(np.ceil(max_car/2)), ncols = 2 )
fig.set_figheight( fig.get_figheight()*2)
ax = ax.ravel()
for j in range(0, len(speed[0])):
    
    s_i = 120
    for k in range(0, len(speed)):
        time = speed[k][j]['Time'].tolist()
        t0 = speed[k][0][speed[k][0]['linear.x'] > 0].iloc[0]['Time']
        ax[j].scatter(x= speed[k][j]['Time'] - t0, y = speed[k][j]['linear.x']  ,  s = s_i, label = 'Factor = {}'.format(real_time_factor[k]))

        s_i = s_i - 40
        if(s_i <10):
            s_i = 10
    ax[j].legend(loc='upper right', fontsize = 20)
    ax[j].set_xlabel('Time [s]')
    ax[j].set_ylabel('Speed m/s')
    ax[j].set_title('Driving Speed for Vehicle {}'.format(j))

plt.suptitle("Run ID: {}".format(run_id), y = 1.001)
plt.tight_layout()
plt.savefig(logdir + run_id + '_speed_overlaid_zero_trimmed.png', bbox_inches='tight')
plt.savefig(logdir + run_id + '_speed_overlaid_zero_trimmed.pdf', bbox_inches='tight')
plt.show()

# per simuation plot
# fig, ax = bagpy.create_fig(nrows = int(np.ceil(len(cmd_speed)/2)), ncols = 2 )
# ax = ax.ravel()
# for j in range(0, len(cmd_speed)):
    
#     cs = posX[j]    
#     for i, v in enumerate(cs):
#         ax[j].scatter(x = 'Time', y = 'pose.pose.position.x', data = cs[i], s = 1, label = 'vehicle {}'.format(i))
#         ax[j].legend()
#         ax[j].set_xlabel('Time')
#         ax[j].set_ylabel('X')
#         ax[j].set_title('Position of all Vehicles: Simulation {}, ({})'.format(j, real_time_factor[j]))
        
# plt.suptitle("Run ID: {}".format(run_id), y = 1.0001)
# plt.tight_layout()
# plt.savefig(logdir + run_id + '_pos_persim_plot.png', bbox_inches='tight')
# plt.savefig(logdir + run_id + '_pos_persim_plot.pdf', bbox_inches='tight')
# plt.show()

#fig, ax = bagpy.create_fig(nrows = int(np.ceil(len(cmd_speed)/2)), ncols = 2 )
fig, ax = plt.subplots(int(np.ceil(len(cmd_speed))), 2, figsize=(12, 18))
ax = ax.reshape(len(cmd_speed), 2 )
for j in range(0, len(cmd_speed)):
    
    cs = posX[j]
    max_start_time_1 = cs[0]['Time'].iloc[0]
    min_end_time_1 = cs[0]['Time'].iloc[-1]
    
    for i, v in enumerate(cs):
        if (max_start_time_1 < cs[i]['Time'].iloc[0]):
            max_start_time_1 = cs[i]['Time'].iloc[0]
        if (min_end_time_1 > cs[i]['Time'].iloc[-1]):
            min_end_time_1 = cs[i]['Time'].iloc[-1]
            
        ax[j, 0].scatter(x = 'Time', y = 'pose.pose.position.x', data = cs[i], s = 1, label = 'vehicle {}'.format(i))
        #ax[j].legend()
        ax[j, 0].set_xlabel('Time [s]', fontsize = 20)
        ax[j, 0].set_ylabel('X [m]', fontsize = 20)
        ax[j, 0].set_title('Simulation {}'.format(j), fontsize = 24)
        ax[j, 0].tick_params(axis='both', which='major', labelsize=18)
        ax[j, 0].tick_params(axis='both', which='minor', labelsize=16)
    
    for i, v in enumerate(cs):
        ax[j, 1].scatter(x = 'Time', y = 'pose.pose.position.y', data = cs[i], s = 1, label = 'vehicle {}'.format(i))
        #ax[j].legend()
        ax[j, 1].set_xlabel('Time [s]', fontsize = 20)
        ax[j, 1].set_ylabel('Y [m]', fontsize = 20)
        ax[j, 1].set_title('Simulation {}'.format(j), fontsize = 24)
        ax[j, 1].tick_params(axis='both', which='major', labelsize=18)
        ax[j, 1].tick_params(axis='both', which='minor', labelsize=16)
        
    ax[j, 0].set_xlim(max_start_time_1, min_end_time_1)
    ax[j, 1].set_xlim(max_start_time_1, min_end_time_1)

#plt.suptitle("Run ID: {}".format(run_id), y = 1.0001)
plt.suptitle("Coordinates of Vehicles: Left: X, Right: Y\n Sparkle Simulation, Modified Approach", y = 1.001, fontsize = 32)
plt.tight_layout()
plt.savefig(logdir + run_id + '_pos_persim_plot.png', bbox_inches='tight')
plt.savefig(logdir + run_id + '_pos_persim_plot.pdf', bbox_inches='tight')
plt.show()


fig, ax = plt.subplots(int(np.ceil(len(cmd_speed)/2)), 2, figsize=(12, 18))
ax = ax.ravel()
for j in range(0, len(cmd_speed)):
    
    cs = posX[j]    
    for i, v in enumerate(cs):
        ax[j].scatter(x = 'pose.pose.position.x', y = 'pose.pose.position.y', data = cs[i], s = 1, label = 'vehicle {}'.format(i))
        #ax[j].legend()
        ax[j].set_xlabel('X [m]', fontsize = 20)
        ax[j].set_ylabel('Y [m]', fontsize = 20)
        ax[j].set_title('Simulation {}'.format(j), fontsize = 24)
        ax[j].tick_params(axis='both', which='major', labelsize=18)
        ax[j].tick_params(axis='both', which='minor', labelsize=16)
        
#plt.suptitle("Run ID: {}".format(run_id), y = 1.0001)
plt.suptitle("Trajectory of Vehicles\n Sparkle Simulation, Modified Approach", y = 1.001, fontsize = 32)
plt.tight_layout()
plt.savefig(logdir + run_id + '_traj_persim_plot.png', bbox_inches='tight')
plt.savefig(logdir + run_id + '_traj_persim_plot.pdf', bbox_inches='tight')
plt.show()


## Calculate the difference of output velocity profile:


def calc_rms(df_2dlist, key, overlap_plots = False):
    """
    Argument
    ---------

    df_2dlist:
        2D list of PandasDataFrame

    Returns
    --------
    rms_matrix

    """
    rms_matrix = np.zeros((len(df_2dlist[0]), len(df_2dlist), len(df_2dlist)))

    if key == 'pose.pose.position.x':
        ylabel = 'X-coordinate [m]'
    elif key== 'pose.pose.position.y':
        ylabel = 'Y-coordinaye [m]'
    elif key == 'linear.x':
        ylabel = 'Speed [m/s]'
    else:
        ylabel = 'Message'
    
    figa = []
    axa = []

    if overlap_plots:
        for kp in range(0, len(df_2dlist[0])):
            f, a = plt.subplots(len(df_2dlist), len(df_2dlist))
            f.set_figheight(f.get_figheight()*2)
            f.set_figwidth(f.get_figwidth()*2)
            figa.append(f)
            axa.append(a)
        sns.set_context("paper")

    # rms_matrix_msgs = np.zeros((len(df_2dlist[0]), len(df_2dlist), len(df_2dlist)))
    for ii in range(0, len(df_2dlist)):
        for jj in range(0, len(df_2dlist)):
            if (ii >= jj):
                if overlap_plots:
                    for vehicle  in range(0,len(df_2dlist[0])):
                        axa[vehicle][ii,jj].axis('off')
                continue
            df1 = pd.DataFrame()
            df2 = pd.DataFrame()
            # use speed for calculating shift
            df1['Time'] = speed[ii][0]['Time'].iloc[:-25] - speed[ii][0]['Time'].iloc[0]
            df1['Message'] = speed[ii][0]['linear.x'].iloc[:-25] # remove last 25 points when sim starts breaking down
            df2['Time'] = speed[jj][0]['Time'].iloc[:-25] - speed[jj][0]['Time'].iloc[0]
            df2['Message'] = speed[jj][0]['linear.x'].iloc[:-25] # remove last 25 points when sim starts breaking down
            df1new, df2new = strymread.ts_sync(df1, df2, rate ='first', method = 'nearest')      
            shift = strymread.time_shift(df1new,df2new,correlation_threshold=0.9)
            for vehicle  in range(0,len(df_2dlist[0])):
                df1 = pd.DataFrame()
                df2 = pd.DataFrame()
                df1['Time'] = df_2dlist[ii][vehicle]['Time'].iloc[:-25] - df_2dlist[ii][vehicle]['Time'].iloc[0]
                df1['Message'] = df_2dlist[ii][vehicle][key].iloc[:-25] # remove last 25 points when sim starts breaking down
                df2['Time'] = df_2dlist[jj][vehicle]['Time'].iloc[:-25] - df_2dlist[jj][vehicle]['Time'].iloc[0]
                df2['Message'] = df_2dlist[jj][vehicle][key].iloc[:-25] # remove last 25 points when sim starts breaking down
                df2['Time'] = df2['Time']+shift
                df1new, df2new = strymread.ts_sync(df1, df2, rate ='first', method = 'nearest')

                if overlap_plots:
                    #fig, ax = bagpy.create_fig(1)
                    sns.lineplot(x = 'Time', y = 'Message', data = df1new, linewidth= 1.5, label='Sim {}, Vehicle {}'.format(ii, vehicle), ax = axa[vehicle][ii,jj])
                    sns.lineplot(x = 'Time', y = 'Message', data = df2new, linewidth = 1.0, linestyle='--', label='Sim {}, Vehicle {}'.format(jj, vehicle), ax = axa[vehicle][ii,jj])
                    axa[vehicle][ii,jj].set_xlabel('Time [s]')
                    axa[vehicle][ii,jj].set_ylabel(ylabel)
                    axa[vehicle][ii,jj].legend()
                    #fig.show()  
                # shift = strymread.time_shift(df1new,df2new,correlation_threshold=0.9)
                
                RMSf = (df1new['Message'] - df2new['Message'])**2  + (df1new['Time'] - df2new['Time'])**2  
                RMSf_MSG = (df1new['Message'] - df2new['Message'])**2 
                RMS = np.sqrt( np.mean(RMSf.values))
                # RMS_MSG = np.sqrt( np.mean(RMSf_MSG.values))
                rms_matrix[vehicle][ii][jj] = RMS
                # rms_matrix_msgs[vehicle][ii][jj] = RMS_MSG

    if overlap_plots:
        for vehicle  in range(0,len(df_2dlist[0])):
            figa[vehicle].tight_layout()
            figa[vehicle].show()
        
    return rms_matrix

# TODO
def traj_calc_rms(df_2dlist, overlap_plots = False):
    """
    Argument
    ---------

    df_2dlist:
        2D list of PandasDataFrame

    Returns
    --------
    rms_matrix

    """
    rms_matrix = np.zeros((len(df_2dlist[0]), len(df_2dlist), len(df_2dlist)))
    # rms_matrix_msgs = np.zeros((len(df_2dlist[0]), len(df_2dlist), len(df_2dlist)))
    for ii in range(0, len(df_2dlist)):
        for jj in range(0, len(df_2dlist)):
            if (ii >= jj):
                continue
            df1 = pd.DataFrame()
            df2 = pd.DataFrame()
            # use speed for calculating shift
            df1['Time'] = speed[ii][0]['Time'].iloc[:-25] - speed[ii][0]['Time'].iloc[0]
            df1['Message'] = speed[ii][0]['linear.x'].iloc[:-25] # remove last 25 points when sim starts breaking down
            df2['Time'] = speed[jj][0]['Time'].iloc[:-25] - speed[jj][0]['Time'].iloc[0]
            df2['Message'] = speed[jj][0]['linear.x'].iloc[:-25] # remove last 25 points when sim starts breaking down
            df1new, df2new = strymread.ts_sync(df1, df2, rate ='first', method = 'nearest')      
            shift = strymread.time_shift(df1new,df2new,correlation_threshold=0.9)
            for vehicle  in range(0,len(df_2dlist[0])):
                df1x = pd.DataFrame()
                df2x = pd.DataFrame()
                df1x['Time'] = df_2dlist[ii][vehicle]['Time'].iloc[:-25] - df_2dlist[ii][vehicle]['Time'].iloc[0]
                df1x['Message'] = df_2dlist[ii][vehicle]['pose.pose.position.x'].iloc[:-25] # remove last 25 points when sim starts breaking down
                df2x['Time'] = df_2dlist[jj][vehicle]['Time'].iloc[:-25] - df_2dlist[jj][vehicle]['Time'].iloc[0]
                df2x['Message'] = df_2dlist[jj][vehicle]['pose.pose.position.x'].iloc[:-25] # remove last 25 points when sim starts breaking down
                df2x['Time'] = df2x['Time']+shift
                df1xnew, df2xnew = strymread.ts_sync(df1x, df2x, rate ='first', method = 'nearest')

                df1y = pd.DataFrame()
                df2y = pd.DataFrame()
                df1y['Time'] = df_2dlist[ii][vehicle]['Time'].iloc[:-25] - df_2dlist[ii][vehicle]['Time'].iloc[0]
                df1y['Message'] = df_2dlist[ii][vehicle]['pose.pose.position.y'].iloc[:-25] # remove last 25 points when sim starts breaking down
                df2y['Time'] = df_2dlist[jj][vehicle]['Time'].iloc[:-25] - df_2dlist[jj][vehicle]['Time'].iloc[0]
                df2y['Message'] = df_2dlist[jj][vehicle]['pose.pose.position.y'].iloc[:-25] # remove last 25 points when sim starts breaking down
                df2y['Time'] = df2y['Time']+shift
                df1ynew, df2ynew = strymread.ts_sync(df1y, df2y, rate ='first', method = 'nearest')
                
                assert df1xnew.shape[0] == df1ynew.shape[0]
                assert df1ynew.shape[0] == df2ynew.shape[0]

                df1xnew.columns = ['Time', 'X']
                df1xnew['Y'] = df1ynew['Message']

                df2xnew.columns = ['Time', 'X']
                df2xnew['Y'] = df2ynew['Message']

                if overlap_plots:
                    fig, ax = bagpy.create_fig(1)
                    ax.scatter(x = 'X', y = 'Y', data = df1xnew, s= 20, label='Sim {}, Vehicle {}'.format(ii, vehicle))
                    ax.scatter(x = 'X', y = 'Y', data = df2xnew, s= 1, label='Sim {}, Vehicle {}'.format(jj, vehicle))
                    ax.legend()
                    fig.show()  
            
                RMSf = (df1xnew['X'] - df2xnew['X'])**2  + (df1xnew['Y'] - df2xnew['Y'])**2  
                RMS = np.sqrt( np.mean(RMSf.values))
                rms_matrix[vehicle][ii][jj] = RMS 
    return rms_matrix

def plot_rmsheatmap(df_2dlist, rms_matrix, max_car, data_name = 'Velocity'):
    sns.set()
    fig, ax = bagpy.create_fig(nrows = int(np.ceil(len(cmd_speed)/2)), ncols = 2 )
    fig2, ax2 = plt.subplots(int(np.ceil(max_car/2)), 2)
    fig2.set_figheight(fig2.get_figheight()*(len(df_2dlist)/4))
    fig2.set_figwidth(24)
    ax2 = ax2.ravel()
    for vehicle in range(0,len(df_2dlist[0])):
        cmap= sns.cubehelix_palette()
        g = sns.heatmap(rms_matrix[vehicle], annot=True, ax = ax2[vehicle], linewidths=.5, xticklabels = real_time_factor, yticklabels=real_time_factor,  square=True,  annot_kws={"size": 16*(len(df_2dlist)/5)}, cbar_kws={"shrink": 0.60/(len(df_2dlist)/4)}, cmap=cmap, vmax=np.max(rms_matrix)*1.05, vmin = 0.0, fmt='.2f')
        g.invert_yaxis()
        ax2[vehicle].set_title('{} RMS Error b/w\nsimulations for vehicle {}'.format(data_name, vehicle), fontsize = 22*(len(df_2dlist)/4))
        g.set_xticklabels(g.get_xmajorticklabels(), fontsize = 18*(len(df_2dlist)/4), rotation = 90)
        g.set_yticklabels(g.get_ymajorticklabels(), fontsize = 18*(len(df_2dlist)/4), rotation = 45)
        cbar = ax2[vehicle].collections[0].colorbar
        cbar.ax.tick_params(labelsize=20*(len(df_2dlist)/4))

    fig2.tight_layout()
    fig2.savefig(logdir + run_id + '_{}_rms_veh_plot.png'.format(data_name), bbox_inches='tight')
    fig2.savefig(logdir + run_id + '_{}_rms_veh_plot.pdf'.format(data_name), bbox_inches='tight')
    fig2.show()

def plot_rmsheatmap(df_2dlist, rms_matrix, max_car, data_name = 'Velocity'):
    sns.set()
    fig, ax = bagpy.create_fig(nrows = int(np.ceil(len(cmd_speed)/2)), ncols = 2 )
    fig2, ax2 = plt.subplots(int(np.ceil(max_car/2)), 2)
    fig2.set_figheight(fig2.get_figheight()*(len(df_2dlist)*1.25))
    fig2.set_figwidth(21)
    ax2 = ax2.ravel()
    for vehicle in range(0,len(df_2dlist[0])):
        cmap= sns.cubehelix_palette()
        g = sns.heatmap(rms_matrix[vehicle], annot=True, ax = ax2[vehicle], linewidths=.5, xticklabels = real_time_factor, yticklabels=real_time_factor,  square=True,  annot_kws={"size": 8*(len(df_2dlist)/5)}, cbar_kws={"shrink": 0.60/(len(df_2dlist)/4)}, cmap=cmap, vmax=np.max(rms_matrix)*1.05, vmin = 0.0, fmt='.2f')
        g.invert_yaxis()
        ax2[vehicle].set_title('{} RMS Error b/w\nsimulations for vehicle {}'.format(data_name, vehicle), fontsize = 22*(len(df_2dlist)/4))
        g.set_xticklabels(g.get_xmajorticklabels(), fontsize = 18*(len(df_2dlist)/4), rotation = 90)
        g.set_yticklabels(g.get_ymajorticklabels(), fontsize = 18*(len(df_2dlist)/4), rotation = 45)
        cbar = ax2[vehicle].collections[0].colorbar
        cbar.ax.tick_params(labelsize=20*(len(df_2dlist)/4))

    fig2.tight_layout()
    fig2.savefig(logdir + run_id + '_{}_rms_veh_plot.png'.format(data_name), bbox_inches='tight')
    fig2.savefig(logdir + run_id + '_{}_rms_veh_plot.pdf'.format(data_name), bbox_inches='tight')
    fig2.show()
        


rms_matrix_speed  = calc_rms(speed, key = 'linear.x' , overlap_plots = False)
%pylab inline
plot_rmsheatmap(speed, rms_matrix_speed, max_car=max_car, data_name='Velocity')


rms_matrix_posX  = calc_rms(posX, key='pose.pose.position.x', overlap_plots = False)
%pylab inline
plot_rmsheatmap(posX, rms_matrix_posX, max_car=max_car, data_name='X-Coordinates' )

rms_matrix_posY  = calc_rms(posX, key='pose.pose.position.y', overlap_plots = False)
%pylab inline
plot_rmsheatmap(posX, rms_matrix_posY, max_car=max_car, data_name='Y-Coordinates' )

rms_matrix_traj  = traj_calc_rms(posX, overlap_plots = False)
%pylab inline
plot_rmsheatmap(posX, rms_matrix_traj, max_car=max_car, data_name='Trajectory' )


from sparkle import gzstats

RTF_df = []

for b in bagfiles:
    main_file = ntpath.basename(b)
    directory = ntpath.dirname(b)
    rtf_file = directory + '/' + main_file.replace('.bag', '/') + main_file.replace('.bag', '_gzStats.txt')
    G = gzstats(rtf_file)
    RTF_df.append(G.dataframe)

sns.set()
sns.set_context("talk")
sns.set_style("whitegrid")
fig, ax = plt.subplots(2,1,figsize=(12, 9))
for i, df in enumerate(RTF_df):
    
    sns.lineplot(x = 'SimTime', y = 'Factor', data = df, linewidth = 1, ax = ax[0], label='Simulation {}'.format(i))
    sns.lineplot(x = 'RealTime', y = 'Factor', data = df, linewidth = 1, ax = ax[1], label='Simulation {}'.format(i))
    ax[0].set_xlabel('Sim Time [s]')
    ax[1].set_xlabel('Real Time [s]')
    ax[0].set_ylabel('Real-Time Factor')
    ax[1].set_ylabel('Real-Time Factor')

ax[0].legend(loc='upper left')
ax[1].legend(loc='upper left')
plt.tight_layout()
fig.savefig(logdir + run_id + '_gzstats.png', bbox_inches='tight')
fig.savefig(logdir + run_id + '_gzstats.pdf', bbox_inches='tight')
fig.show()

