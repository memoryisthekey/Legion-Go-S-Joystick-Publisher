#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
from geometry_msgs.msg import TwistStamped


class LegionJoystick(Node):
    def __init__(self):
        super().__init__('legion_joystick')

        self.cmd_pub = self.create_publisher(TwistStamped, '/cmd_vel', 10)
        self.joy_sub = self.create_subscription(Joy, '/joy', self.joy_callback, 10)

        self.timer = self.create_timer(0.05, self.publish_cmd)  # 20 Hz

        self.latest_joy = None

        self.left_bumper_button = 4
        self.right_bumper_button = 5

        # left stick vertical = axes[1]
        # left stick horizontal = axes[0]
        self.linear_axis = 1
        self.angular_axis = 0

        self.slow_linear = 0.4
        self.slow_angular = 0.8

        self.fast_linear = 1.5
        self.fast_angular = 1.8

    def joy_callback(self, msg):
        self.latest_joy = msg

    def publish_cmd(self):
        twist_stamped = TwistStamped()

        twist_stamped.header.stamp = self.get_clock().now().to_msg()
        twist_stamped.header.frame_id = 'base_link'  # or 'cmd_vel_link', depending on your robot setup

        if self.latest_joy is None:
            self.cmd_pub.publish(twist_stamped)
            return

        buttons = self.latest_joy.buttons
        axes = self.latest_joy.axes

        slow_pressed = buttons[self.left_bumper_button] == 1
        fast_pressed = buttons[self.right_bumper_button] == 1

        if slow_pressed:
            twist_stamped.twist.linear.x = self.slow_linear * axes[self.linear_axis]
            twist_stamped.twist.angular.z = self.slow_angular * axes[self.angular_axis]

        elif fast_pressed:
            twist_stamped.twist.linear.x = self.fast_linear * axes[self.linear_axis]
            twist_stamped.twist.angular.z = self.fast_angular * axes[self.angular_axis]

        else:
            twist_stamped.twist.linear.x = 0.0
            twist_stamped.twist.angular.z = 0.0

        self.cmd_pub.publish(twist_stamped)


def main():
    rclpy.init()
    node = LegionJoystick()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()