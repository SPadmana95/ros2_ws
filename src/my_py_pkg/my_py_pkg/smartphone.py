#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class Smartphone(Node):
    def __init__(self):
        super().__init__('smartphone')
        self.get_logger().info('Smartphone node is up and running!')
        self.subscriber_ = self.create_subscription( 
            String, 'robot_news', self.robot_news_callback, 10)
        self.subscriber_  # prevent unused variable warning
        self.get_logger().info('Smartphone node is subscribed to the "robot_news" topic.')

    def robot_news_callback(self, msg):
        self.get_logger().info('Received news: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    node = Smartphone()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()       

if __name__ == '__main__':
    main()