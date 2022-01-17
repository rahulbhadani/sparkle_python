#!/bin/bash
random_string=$(echo $RANDOM | md5sum | head -c 20; echo);

random_string=157aa878b98a0494a528

echo $random_string

./circular_layout_simulation_for_repeatability_test.py --ncars=21 --max_update_rate=100.0 --time_step=0.01 --update_rate=20.0 --log_time=200.0 --dynamics=bicycle --controller=injector --run_id=$random_string --enable_gui --use_odom --use_lead_vel
#sleep 10
#./circular_layout_simulation_for_repeatability_test.py --ncars=21 --max_update_rate=100.0 --time_step=0.01 --update_rate=20.0 --log_time=200.0 --dynamics=bicycle --controller=injector --run_id=$random_string --enable_gui --use_odom --use_lead_vel
#sleep 10
#./circular_layout_simulation_for_repeatability_test.py --ncars=21 --max_update_rate=100.0 --time_step=0.01 --update_rate=20.0 --log_time=200.0 --dynamics=bicycle --controller=injector --run_id=$random_string --enable_gui --use_odom --use_lead_vel
#sleep 10
#./circular_layout_simulation_for_repeatability_test.py --ncars=21 --max_update_rate=100.0 --time_step=0.01 --update_rate=20.0 --log_time=200.0 --dynamics=bicycle --controller=injector --run_id=$random_string --enable_gui --use_odom --use_lead_vel
#sleep 10
#./circular_layout_simulation_for_repeatability_test.py --ncars=21 --max_update_rate=100.0 --time_step=0.01 --update_rate=20.0 --log_time=200.0 --dynamics=bicycle --controller=injector --run_id=$random_string --enable_gui --use_odom --use_lead_vel
#sleep 10
#./circular_layout_simulation_for_repeatability_test.py --ncars=21 --max_update_rate=100.0 --time_step=0.01 --update_rate=20.0 --log_time=200.0 --dynamics=bicycle --controller=injector --run_id=$random_string --enable_gui --use_odom --use_lead_vel



