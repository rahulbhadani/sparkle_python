#!/usr/bin/env python
# Initial Date: June 2020
# Author: Rahul Bhadani
# Copyright (c) Rahul Bhadani, Arizona Board of Regents
# All rights reserved.

from .launch import launch
import rospy
import time

#uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
#roslaunch.configure_logging(uuid)
#launch = roslaunch.parent.ROSLaunchParent(uuid, ["/home/ivory/VersionControl/catvehicle_ws/src/catvehicle/launch/catvehicle_empty.launch"])
#launch.start()

rospy.init_node('en_Mapping', anonymous=True)
launchfile="/home/ivory/VersionControl/catvehicle_ws/src/catvehicle/launch/catvehicle_empty.launch"
emptylaunch = launch(launchfile=launchfile)
emptylaunch.start()

spawnfile = "/home/ivory/VersionControl/catvehicle_ws/src/catvehicle/launch/catvehicle_spawn.launch"
spawnlaunch = launch(launchfile=spawnfile, X = 30, Y = 50)
spawnlaunch.start()

time.sleep(30)
