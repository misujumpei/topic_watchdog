#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 misujumpei
# SPDX-License-Identifier: MIT


import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool


class Watchdog(Node):
    def __init__(self):
        super().__init__('watchdog')

        self.publisher_ = self.create_publisher(
            Bool,
            'watchdog/heartbeat',
            10
        )

        self.timer = self.create_timer(
            1.0,
            self.publish_heartbeat
        )

        self.get_logger().info('watchdog node started')

    def publish_heartbeat(self):
        msg = Bool()
        msg.data = True
        self.publisher_.publish(msg)
        self.get_logger().debug('heartbeat published')


def main():
    rclpy.init()
    node = Watchdog()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()

