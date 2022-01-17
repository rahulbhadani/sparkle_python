#!/bin/bash
random_string=$(echo $RANDOM | md5sum | head -c 20; echo);

#random_string=0b4dd8ad903c9d03e0b7

echo $random_string

echo "Starting Test 1"
./basic_layout_simulation_for_repeatability_test.py --ncars=3 --max_update_rate=100.0 --time_step=0.01 --update_rate=20.0 --log_time=200.0 --dynamics=bicycle --controller=rl --run_id=$random_string --enable_gui --newclock --standalone
sleep 10
echo "Starting Test 2"
./basic_layout_simulation_for_repeatability_test.py --ncars=3 --max_update_rate=100.0 --time_step=0.01 --update_rate=20.0 --log_time=200.0 --dynamics=bicycle --controller=rl --run_id=$random_string --enable_gui --newclock --standalone
sleep 10
echo "Starting Test 3"
./basic_layout_simulation_for_repeatability_test.py --ncars=3 --max_update_rate=100.0 --time_step=0.01 --update_rate=20.0 --log_time=200.0 --dynamics=bicycle --controller=rl --run_id=$random_string --enable_gui --newclock --standalone
sleep 10
echo "Starting Test 4"
./basic_layout_simulation_for_repeatability_test.py --ncars=3 --max_update_rate=100.0 --time_step=0.01 --update_rate=20.0 --log_time=200.0 --dynamics=bicycle --controller=rl --run_id=$random_string --enable_gui --newclock --standalone
sleep 10
echo "Starting Test 5"
./basic_layout_simulation_for_repeatability_test.py --ncars=3 --max_update_rate=100.0 --time_step=0.01 --update_rate=20.0 --log_time=200.0 --dynamics=bicycle --controller=rl --run_id=$random_string --enable_gui --newclock --standalone
sleep 10
echo "Starting Test 6"
./basic_layout_simulation_for_repeatability_test.py --ncars=3 --max_update_rate=100.0 --time_step=0.01 --update_rate=20.0 --log_time=200.0 --dynamics=bicycle --controller=rl --run_id=$random_string --enable_gui --newclock --standalone
sleep 10
echo "Starting Test 7"
./basic_layout_simulation_for_repeatability_test.py --ncars=3 --max_update_rate=100.0 --time_step=0.01 --update_rate=20.0 --log_time=200.0 --dynamics=bicycle --controller=rl --run_id=$random_string --enable_gui --newclock --standalone
sleep 10
echo "Starting Test 8"
./basic_layout_simulation_for_repeatability_test.py --ncars=3 --max_update_rate=100.0 --time_step=0.01 --update_rate=20.0 --log_time=200.0 --dynamics=bicycle --controller=rl --run_id=$random_string --enable_gui --newclock --standalone
sleep 10
echo "Starting Test 9"
./basic_layout_simulation_for_repeatability_test.py --ncars=3 --max_update_rate=100.0 --time_step=0.01 --update_rate=20.0 --log_time=200.0 --dynamics=bicycle --controller=rl --run_id=$random_string --enable_gui --newclock --standalone