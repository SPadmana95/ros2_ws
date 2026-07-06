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

## 5b. Publisher / Subscriber — Python (`my_py_pkg`)

**Terminal 1** — Run the publisher (robot_news_station):

```bash
ros2 run my_py_pkg robot_news_station
```

Publishes a `String` message on the `/robot_news` topic every 1 second.

**Terminal 2** — Run the subscriber (smartphone):

```bash
ros2 run my_py_pkg smartphone
```

Subscribes to `/robot_news` and prints every received message.

**Verify the topic:**

```bash
ros2 topic echo /robot_news
```

---

## 5c. Publisher / Subscriber — C++ (`my_cpp_pkg`)

**Terminal 1** — Run the publisher (robot_news_station):

```bash
ros2 run my_cpp_pkg robot_news_station
```

Publishes a `String` message on the `/robot_news` topic every 1 second.

**Terminal 2** — Run the subscriber (smartphone):

```bash
ros2 run my_cpp_pkg smartphone
```

Subscribes to `/robot_news` and prints every received message.

**Verify the topic:**

```bash
ros2 topic echo /robot_news
```

---

## 5d. Service Server / Client — Python (`my_py_pkg`)

**Terminal 1** — Run the service server:

```bash
ros2 run my_py_pkg add_two_ints_server
```

Starts the `add_two_ints` service that takes two integers and returns their sum.

**Terminal 2 (Option A)** — Run the OOP client (hardcoded calls: 3+5, 7+8, 12+15):

```bash
ros2 run my_py_pkg add_two_ints_client
```

**Terminal 2 (Option B)** — Run the non-OOP client (pass values at runtime):

```bash
ros2 run my_py_pkg add_two_ints_client_without_oop 3 7
```

Expected output: `Result of add_two_ints: 3 + 7 = 10`

**Or call the service manually from the terminal:**

```bash
ros2 service call /add_two_ints example_interfaces/srv/AddTwoInts "{a: 3, b: 7}"
```

**Inspect the service interface:**

```bash
ros2 interface show example_interfaces/srv/AddTwoInts
```

---

## 5e. Service Server / Client — C++ (`my_cpp_pkg`)

**Terminal 1** — Run the C++ service server:

```bash
ros2 run my_cpp_pkg add_two_ints_server
```

**Terminal 2** — Run the C++ non-OOP client (hardcoded: a=5, b=3):

```bash
ros2 run my_cpp_pkg add_two_ints_client_no_oop
```

Expected output: `Result: 8`

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
| `ros2 topic info /robot_news` | Show topic type and number of publishers/subscribers |
| `ros2 topic hz /robot_news` | Display the publishing rate of a topic in Hz |
| `ros2 topic bw /robot_news` | Display the bandwidth (bytes/sec) consumed by a topic |
| `ros2 topic pub -r 5 /robot_news example_interfaces/msg/String "{data: 'hello from the terminal'}"` | Publish a message manually to a topic at 5 Hz from the terminal |
| `ros2 run my_py_pkg robot_news_station --ros-args -r __node:=my_station` | Remap the node name at runtime to `my_station` |
| `ros2 run my_py_pkg robot_news_station --ros-args -r __node:=my_station -r robot_news:=abc` | Remap node name and topic name (`robot_news` → `abc`) at runtime |
| `ros2 run my_py_pkg smartphone --ros-args -r robot_news:=abc` | Remap subscriber topic to `abc` to match the remapped publisher |
| `ros2 interface show example_interfaces/srv/AddTwoInts` | Show the request/response fields of the AddTwoInts service interface |
| `ros2 service call /add_two_ints example_interfaces/srv/AddTwoInts "{a: 3, b: 7}"` | Manually call a service from the terminal with request values |