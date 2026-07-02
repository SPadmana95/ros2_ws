#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyFirstNode(Node):
    def __init__(self):
        super().__init__("my_first_py_node")
        self.counter_ = 0
        self.get_logger().info("Hello ROS2")
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        self.get_logger().info("Hello ROS2 " + str(self.counter_))
        self.counter_ += 1

def main(args=None):
    rclpy.init(args=args)
    node = MyFirstNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()