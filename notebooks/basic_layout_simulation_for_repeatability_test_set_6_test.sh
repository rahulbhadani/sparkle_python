#!/bin/bash
random_string=$(echo $RANDOM | md5sum | head -c 20; echo);

#random_string=016eeb535255aa58ccee

echo $random_string

echo "Starting Test 1"

./basic_layout_simulation_for_repeatability_test.py --ncars=20 --max_update_rate=100.0 --time_step=0.01 --update_rate=20.0 --log_time=200.0 --dynamics=bicycle --controller=rl --run_id=$random_string --enable_gui --use_odom --use_lead_vel
sleep 10
./basic_layout_simulation_for_repeatability_test.py --ncars=20 --max_update_rate=100.0 --time_step=0.01 --update_rate=20.0 --log_time=200.0 --dynamics=bicycle --controller=rl --run_id=$random_string --enable_gui --use_odom --use_lead_vel
sleep 10
./basic_layout_simulation_for_repeatability_test.py --ncars=20 --max_update_rate=100.0 --time_step=0.01 --update_rate=20.0 --log_time=200.0 --dynamics=bicycle --controller=rl --run_id=$random_string --enable_gui --use_odom --use_lead_vel
sleep 10
./basic_layout_simulation_for_repeatability_test.py --ncars=20 --max_update_rate=100.0 --time_step=0.01 --update_rate=20.0 --log_time=200.0 --dynamics=bicycle --controller=rl --run_id=$random_string --enable_gui --use_odom --use_lead_vel
sleep 10
./basic_layout_simulation_for_repeatability_test.py --ncars=20 --max_update_rate=100.0 --time_step=0.01 --update_rate=20.0 --log_time=200.0 --dynamics=bicycle --controller=rl --run_id=$random_string --enable_gui --use_odom --use_lead_vel
sleep 10
./basic_layout_simulation_for_repeatability_test.py --ncars=20 --max_update_rate=100.0 --time_step=0.01 --update_rate=20.0 --log_time=200.0 --dynamics=bicycle --controller=rl --run_id=$random_string --enable_gui --use_odom --use_lead_vel



