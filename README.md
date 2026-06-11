# Legion Joystick Teleoperation

This ROS 2 package provides a node that converts joystick inputs (sensor_msgs/msg/Joy) into stamped velocity commands (geometry_msgs/msg/TwistStamped). It features a safety "deadman's switch" design, requiring the operator to hold down specific bumper buttons to move the robot at different speeds.

## Features
> 
> Two-Speed Modes using the controller bumpers: 
> * Slow mode -> Left Bumper (LB)
> * Fast mode -> Right Bumper (RB)
> 
>Safety Default: If no bumper is pressed, the robot will automatically publish zero velocity (stops moving).
> 
> Stamped Outputs: Publishes TwistStamped messages with accurate timestamps and frame IDs, ideal for modern ROS 2 navigation pipelines.
>
>Smooth Execution: Runs on a dedicated timer publishing at 20 Hz to ensure consistent command delivery.

## Control Mapping

By default, the script is configured for standard controllers (like an Xbox or Logitech controller mapped to a Linux system):
### Input	Action / Mapping
* Left Stick (Vertical)	Linear Velocity (Forward / Backward)
* Left Stick (Horizontal)	Angular Velocity (Turning Left / Right) 
* Left Bumper (LB)	Hold for Slow/Precise Mode (0.4 m/s, 0.8 rad/s)
* Right Bumper (RB)	Hold for Fast/Turbo Mode (1.0 m/s, 1.8 rad/s)

> If neither LB nor RB is pressed, the node will continuously publish zero velocity commands to keep the robot stationary.

## ROS 2 Interface
Subscribed Topics

    /joy (sensor_msgs/msg/Joy)

        Receives the raw joystick axis and button states.

Published Topics

    /cmd_vel (geometry_msgs/msg/TwistStamped)

        Publishes the calculated linear and angular velocities.

        header.frame_id is configured as 'base_link'.

The published topic is then remapped in the **launch file** to `/a300_0000x/platform/cmd_vel`

## Setup and Usage
### 1. Prerequisites

Ensure you have the standard ROS 2 joystick package installed to read your controller hardware:
Bash

```bash
sudo apt install ros-<ros2-distro>-joy
```

2. Running the Nodes

You can launch both the joystick driver and the teleop node simultaneously using the provided launch file:
```Bash
ros2 launch legion_joystick husky_joy.launch.py
```

## Customization

If your controller layout differs, you can easily change the button indices or speed limits directly inside the __init__ method of the script:

```Python

self.left_bumper_button = 4   # Change index for your controller
self.right_bumper_button = 5  # Change index for your controller

# Adjust maximum speed ceilings
self.slow_linear = 0.4
self.fast_linear = 1.0 
```