# ros2_ws

## 1. Install ROS2 Jazzy for Ubuntu 24.04

Reference: [Ubuntu (deb packages) — ROS 2 Documentation: Jazzy](https://docs.ros.org/en/jazzy/Installation/Ubuntu-Install-Debs.html)

Setup the build environment on every terminal. Add the below line to `.bashrc`:

```bash
source /opt/ros/jazzy/setup.bash
```

To validate the ROS2 installation, open two new terminals and run the below commands on each:

```bash
# Terminal 1
ros2 run demo_nodes_cpp talker

# Terminal 2
ros2 run demo_nodes_cpp listener
```

---

## 2. Create ROS2 Workspace

```bash
mkdir ros2_ws
mkdir -p ros2_ws/src
```

---

## 3. Create ROS2 Python Package

```bash
cd ~/ros2_ws/src
ros2 pkg create my_py_pkg --build-type ament_python --dependencies rclpy

cd ~/ros2_ws
colcon build

# Build only the Python package
colcon build --packages-select my_py_pkg
```

---

## 4. Create ROS2 C++ Package

```bash
cd ~/ros2_ws/src
ros2 pkg create my_cpp_pkg --build-type ament_cmake --dependencies rclcpp

cd ~/ros2_ws
colcon build

# Build only the C++ package
colcon build --packages-select my_cpp_pkg
```

---

## 5. Run a Node

Source the workspace before running any node:

```bash
source ~/ros2_ws/install/setup.bash
```

Run the first Python node:

```bash
ros2 run my_py_pkg my_first_py_node
```

Run the first C++ node:

```bash
ros2 run my_cpp_pkg my_first_node
```

---

## 6. Useful Commands

| Command | Description |
|---|---|
| `ros2 interface show example_interfaces/msg/String` | Show the fields and types of a ROS2 message interface |
| `colcon build --packages-select my_cpp_pkg --symlink-install` | Build a specific package; `--symlink-install` avoids rebuilding for Python/script changes |
| `ros2 node list` | List all active ROS2 nodes |
| `ros2 node info /robot_news_station` | Show details of a node: publishers, subscribers, services |
| `ros2 topic list` | List all active ROS2 topics |
| `ros2 topic echo /robot_news` | Print messages published on a topic in real time |