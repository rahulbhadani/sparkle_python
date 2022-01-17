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

4. Clone following repositories in `~/catkin_ws/src` as additional dependencies:
```
cd ~/catkin_ws/src
git clone https://github.com/jmscslgroup/hoffmansubsystem
```
5. Do `catkin_make`
```
cd ~/catkin_ws
catkin_make
```
6. Source devel/setup.bash
```
echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
source ~/.bashrc
```
7. Install python package associated with sparkle package
```
roscd sparkle
python setup.py install

```
8. Clone this repository anywhere
```
cd ~
https://github.com/rahulbhadani/sparkle_python/

```

# Running the code
To run the code to reproduce results from the manuscript, we have to scripts in `reproducibility` folder of this repository;
1. `basic_layout_simulation_for_repeatability_test.py` for vehicle movement in a straightline. 
2. `circular_layout_simulation_for_repeatability_test.py` for vehicle movement in a circular track.

To get help type:

```
./basic_layout_simulation_for_repeatability_test.py -h
```

and 

```
./circular_layout_simulation_for_repeatability_test.py -h
```

An example script to run via command line:

```
./basic_layout_simulation_for_repeatability_test.py --ncars=4 --max_update_rate=100.0 --time_step=0.01 --update_rate=20.0 --log_time=200.0 --dynamics=bicycle --controller=rl --run_id=$random_string --robot_model=catvehicle --enable_gui
```

and

```
./circular_layout_simulation_for_repeatability_test.py --ncars=21 --max_update_rate=100.0 --time_step=0.01 --update_rate=20.0 --log_time=200.0 --dynamics=bicycle --controller=injector --run_id=$random_string --enable_gui --use_odom --use_lead_vel
```
