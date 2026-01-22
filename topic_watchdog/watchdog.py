#!/usr/bin/env python3
import rclpy
from rclpy.node import Node


class Watchdog(Node):
    def __init__(self):
        super().__init__('watchdog')
        self.get_logger().info('watchdog node started')


def main():
    rclpy.init()
    node = Watchdog()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()

