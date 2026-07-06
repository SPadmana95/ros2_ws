#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class AddTwoIntsClient(Node):
    def __init__(self):
        super().__init__("add_two_ints_client")
        self.client = self.create_client(AddTwoInts, "add_two_ints")

    def call_add_two_ints(self, a: int, b: int):
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().warning("Service not available, waiting again...")
        
        request = AddTwoInts.Request()
        request.a = a
        request.b = b
        future = self.client.call_async(request)
        rclpy.spin_until_future_complete(self, future)
        self.handle_response(future)

    def handle_response(self, future):
        try:
            response = future.result()
            self.get_logger().info(f"Result of add_two_ints: {response.sum}")
        except Exception as e:
            self.get_logger().error(f"Service call failed: {e}")

def main(args=None):
    rclpy.init(args=args)
    node = AddTwoIntsClient()
    node.call_add_two_ints(3, 5)  # Example call with a=3 and b=5
    node.call_add_two_ints(7, 8)
    node.call_add_two_ints(12, 15)
    rclpy.shutdown()

if __name__ == "__main__":
    main()