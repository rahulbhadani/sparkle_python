#!/usr/bin/env python
# coding: utf-8

# In[10]:


import bagpy
from bagpy import bagreader
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


folder = '/home/ivory/CyverseData/ProjectSparkle/'
filename = 'sparkle_n_2_update_rate_20.0_max_update_rate_100.0_time_step_0.01_logtime_150.0_2020-06-18-16-39-19.bag'
b = bagreader(folder + filename)


# In[3]:


b.topic_table


# In[4]:


b.plot_odometry()


# In[5]:


b.plot_vel()


# In[6]:


odom_data = b.odometry_data()


# In[7]:


odom_data


# In[8]:


magna_odom = odom_data[0]
nebula_odom = odom_data[2]


# In[11]:


magna_odom_data = pd.read_csv(magna_odom)
nebula_odom_data = pd.read_csv(nebula_odom)


# In[12]:


magna_odom_data


# In[13]:


nebula_odom_data


# In[21]:


fig, ax = bagpy.create_fig(1)
ax[0].scatter(magna_odom_data['Time'], magna_odom_data['pose.y'], s =1 )
ax[0].scatter(nebula_odom_data['Time'], nebula_odom_data['pose.y'], s= 1)
plt.show()


# In[ ]:




