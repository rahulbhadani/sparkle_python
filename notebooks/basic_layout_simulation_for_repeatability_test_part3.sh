#!/bin/bash
random_string=$(echo $RANDOM | md5sum | head -c 20; echo);

random_string=d9a4a64bde7c5299972e
echo $random_string
echo "Starting Test 1"
./basic_layout_simulation_for_repeatability_test.py --ncars=4 --max_update_rate=100.0 --time_step=0.01 --update_rate=20.0 --log_time=200.0 --dynamics=bicycle --controller=rl --run_id=$random_string --robot_model=catvehicle --enable_gui --newclock
sleep 10


echo "Starting Test 2"
./basic_layout_simulation_for_repeatability_test.py --ncars=4 --max_update_rate=50.0 --time_step=0.01 --update_rate=20.0 --log_time=200.0 --dynamics=bicycle --controller=rl --run_id=$random_string --robot_model=catvehicle --enable_gui --newclock
sleep 10

echo "Starting Test 3"
./basic_layout_simulation_for_repeatability_test.py --ncars=4 --max_update_rate=20.0 --time_step=0.01 --update_rate=20.0 --log_time=200.0 --dynamics=bicycle --controller=rl --run_id=$random_string --robot_model=catvehicle --enable_gui --newclock
sleep 10

echo "Starting Test 4"
./basic_layout_simulation_for_repeatability_test.py --ncars=4 --max_update_rate=100.0 --time_step=0.01 --update_rate=20.0 --log_time=200.0 --dynamics=bicycle --controller=rl --run_id=$random_string --robot_model=catvehicle --enable_gui --newclock
sleep 10

echo "Starting Test 5"
./basic_layout_simulation_for_repeatability_test.py --ncars=4 --max_update_rate=50.0 --time_step=0.01 --update_rate=20.0 --log_time=200.0 --dynamics=bicycle --controller=rl --run_id=$random_string --robot_model=catvehicle --enable_gui --newclock
sleep 10

echo "Starting Test 6"
./basic_layout_simulation_for_repeatability_test.py --ncars=4 --max_update_rate=20.0 --time_step=0.01 --update_rate=20.0 --log_time=200.0 --dynamics=bicycle --controller=rl --run_id=$random_string --robot_model=catvehicle --enable_gui --newclock
sleep 10

