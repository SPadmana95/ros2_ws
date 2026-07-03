#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts


class AddTwoIntsServer(Node):
    def __init__(self):
        super().__init__("add_two_ints_server")
        self.server = self.create_service(AddTwoInts, "add_two_ints", self.add_two_ints_callback)
        self.get_logger().info("Add Two Ints Server is ready to receive requests.")
    
    def add_two_ints_callback(self, request: AddTwoInts.Request, response: AddTwoInts.Response):
        response.sum = request.a + request.b
        self.get_logger().info(f"Received request: a={request.a}, b={request.b}, sum={response.sum}")
        return response

def main(args=None):
    rclpy.init(args=args)
    node = AddTwoIntsServer()
    node.get_logger().info("Add Two Ints Server is up and running!")
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()