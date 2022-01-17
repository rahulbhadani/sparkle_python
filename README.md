# Multi-Vehicle Simulation for Repeatability
This package provides scripts for creating multi-vehicle simulations using Sparkle ROS package

# Instruction
1. Prerequisite is ROS Noetic on Ubuntu 20.04. See http://wiki.ros.org/noetic/Installation/Ubuntu for installation instruction.
2. Clone sparkle ROS package into `~/catkin_ws/src` directory. 
```
mkdir -p catkin_ws/src
cd ~/catkin_ws/src
git clone https://github.com/jmscslgroup/sparkle
```
3. Clone CAT Vehicle ROS package into `~/catkin_ws/src` and change to `noetic_gazebo-11` branch
```
cd ~/catkin_ws/src
git clone https://github.com/jmscslgroup/catvehicle
git checkout noetic_gazebo-11
```
Follow the README of https://github.com/jmscslgroup/catvehicle to install any dependencies that are required.

4. Do `catkin_make`
```
cd ~/catkin_ws
catkin_make
```

5. Source devel/setup.bash
```
echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

Install python package associated with sparkle package
```
roscd sparkle
python setup.py install

```

5. Clone this repository anywhere
```
cd ~
https://github.com/rahulbhadani/sparkle_python/

```

# Running the code

