#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/srv/add_two_ints.hpp"

using namespace std::chrono_literals;
int main(int argc, char **argv)
{
  rclcpp::init(argc, argv);

  auto node = rclcpp::Node::make_shared("add_two_ints_client_no_oop");
  auto client = node->create_client<example_interfaces::srv::AddTwoInts>("add_two_ints");
  while (!client->wait_for_service(1s)) {
  
    RCLCPP_INFO(node->get_logger(), "Waiting for service to be available...");
  }

  auto request = std::make_shared<example_interfaces::srv::AddTwoInts::Request>();
  request->a = 5;
  request->b = 3;

  auto future = client->async_send_request(request);
  if (rclcpp::spin_until_future_complete(node, future) == rclcpp::FutureReturnCode::SUCCESS) {
    auto response = future.get();
    RCLCPP_INFO(node->get_logger(), "Result: %ld", response->sum);
  } else {
    RCLCPP_ERROR(node->get_logger(), "Failed to call service add_two_ints");
  }

  rclcpp::shutdown();
  return 0;
}