#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class RobotNewsStation(Node):
    def __init__(self):
        super().__init__('robot_news_station')
        self.get_logger().info('Robot News Station is up and running!')
        self.publisher_ = self.create_publisher(String, 'robot_news', 10)
        self.timer_ = self.create_timer(1.0, self.publish_news)  # Publish news every 1 seconds
        self.get_logger().info('Robot News Station is publishing news every 1 second.')
    def publish_news(self):
        msg = String()
        msg.data = "Hello, this is the latest news from the Robot News Station!"
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    node = RobotNewsStation()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()