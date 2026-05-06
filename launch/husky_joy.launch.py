from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    joy_node = Node(
        package='joy',
        executable='joy_node',
        name='joy_node',
        output='screen',
        parameters=[
            {
                'deadzone': 0.05,
                #'autorepeat_rate': 20.0,
            }
        ]
    )

    husky_teleop = Node(
        package='legion_joystick',
        executable='legion_joystick',
        name='legion_joystick',
        output='screen',
        remappings=[
            ('/cmd_vel', '/a300_00008/cmd_vel'),
        ]
    )

    return LaunchDescription([
        joy_node,
        husky_teleop,
    ])