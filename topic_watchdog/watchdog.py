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
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()



if __name__ == '__main__':
    main()

