#!/usr/bin/env python3
import sys
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

def main(args=None):
    rclpy.init(args=args)
    node = Node("add_two_ints_client_without_oop")

    if len(sys.argv) != 3:
        node.get_logger().error("Usage: add_two_ints_client_without_oop <a> <b>")
        rclpy.shutdown()
        return

    client = node.create_client(AddTwoInts, "add_two_ints")
    while not client.wait_for_service(timeout_sec=1.0):
        node.get_logger().warning("Service not available, waiting again...")

    request = AddTwoInts.Request()
    request.a = int(sys.argv[1])
    request.b = int(sys.argv[2])

    future = client.call_async(request)
    rclpy.spin_until_future_complete(node, future)

    response = future.result()
    node.get_logger().info(f"Result of add_two_ints: {request.a} + {request.b} = {response.sum}")

    node.destroy_node()
    rclpy.shutdown()