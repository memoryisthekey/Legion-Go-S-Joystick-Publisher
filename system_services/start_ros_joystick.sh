#!/bin/bash
set -e
source /opt/ros/jazzy/setup.bash
source /home/legion/ros2_ws/install/setup.bash
source /home/legion/.bashrc

ros2 launch legion_joystick husky_joy.launch.py

