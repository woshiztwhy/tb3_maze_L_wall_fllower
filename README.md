#迷宫左墙跟随项目src源码
#该项目通过简单的PD控制保持小车与左墙的距离，从而实现左墙跟随走迷宫的功能
#基于ros2 tb3 gazebo urdf
#核心控制算法位于~/maze_control/maze_control/tb3_wall_follower
#目录结构
.
├── custom
│   └── my_obstacle.world
├── maze_control
│   ├── launch
│   │   └── car_launch.py
│   ├── maze_control
│   │   ├── __init__.py
│   │   ├── scan_region_node.py
│   │   ├── tb3_avoid.py
│   │   ├── tb3_point2point.py
│   │   └── tb3_wall_follower.py
│   ├── package.xml
│   ├── resource
│   │   └── maze_control
│   ├── setup.cfg
│   ├── setup.py
│   └── test
│       ├── test_copyright.py
│       ├── test_flake8.py
│       └── test_pep257.py
└── turtlebot3
    ├── CONTRIBUTING.md
    ├── docker
    │   ├── humble
    │   │   ├── container.sh
    │   │   ├── docker-compose.yml
    │   │   └── Dockerfile
    │   └── jazzy
    │       ├── container.sh
    │       ├── docker-compose.yml
    │       └── Dockerfile
    ├── ISSUE_TEMPLATE.md
    ├── LICENSE
    ├── README.md
    ├── turtlebot3
    │   ├── CHANGELOG.rst
    │   ├── CMakeLists.txt
    │   └── package.xml
    ├── turtlebot3_bringup
    │   ├── CHANGELOG.rst
    │   ├── CMakeLists.txt
    │   ├── launch
    │   │   ├── camera.launch.py
    │   │   ├── robot.launch.py
    │   │   ├── rviz2.launch.py
    │   │   └── turtlebot3_state_publisher.launch.py
    │   ├── package.xml
    │   ├── param
    │   │   ├── burger.yaml
    │   │   ├── humble
    │   │   │   ├── burger.yaml
    │   │   │   ├── waffle_pi.yaml
    │   │   │   └── waffle.yaml
    │   │   ├── waffle_pi.yaml
    │   │   └── waffle.yaml
    │   └── script
    │       ├── 99-turtlebot3-cdc.rules
    │       └── create_udev_rules
    ├── turtlebot3_cartographer
    │   ├── CHANGELOG.rst
    │   ├── CMakeLists.txt
    │   ├── config
    │   │   └── turtlebot3_lds_2d.lua
    │   ├── launch
    │   │   ├── cartographer.launch.py
    │   │   └── occupancy_grid.launch.py
    │   ├── package.xml
    │   └── rviz
    │       └── tb3_cartographer.rviz
    ├── turtlebot3_ci.repos
    ├── turtlebot3_description
    │   ├── CHANGELOG.rst
    │   ├── CMakeLists.txt
    │   ├── meshes
    │   │   ├── bases
    │   │   │   ├── burger_base.stl
    │   │   │   ├── waffle_base.stl
    │   │   │   └── waffle_pi_base.stl
    │   │   ├── sensors
    │   │   │   ├── astra.dae
    │   │   │   ├── astra.jpg
    │   │   │   ├── lds.stl
    │   │   │   ├── r200.dae
    │   │   │   └── r200.jpg
    │   │   └── wheels
    │   │       ├── left_tire.stl
    │   │       └── right_tire.stl
    │   ├── package.xml
    │   ├── rviz
    │   │   └── model.rviz
    │   └── urdf
    │       ├── common_properties.urdf
    │       ├── turtlebot3_burger.urdf
    │       ├── turtlebot3_waffle_pi.urdf
    │       └── turtlebot3_waffle.urdf
    ├── turtlebot3_example
    │   ├── CHANGELOG.rst
    │   ├── package.xml
    │   ├── resource
    │   │   └── turtlebot3_example
    │   ├── setup.cfg
    │   ├── setup.py
    │   └── turtlebot3_example
    │       ├── __init__.py
    │       ├── turtlebot3_absolute_move
    │       │   ├── __init__.py
    │       │   └── turtlebot3_absolute_move.py
    │       ├── turtlebot3_interactive_marker
    │       │   ├── __init__.py
    │       │   └── turtlebot3_interactive_marker.py
    │       ├── turtlebot3_obstacle_detection
    │       │   ├── __init__.py
    │       │   └── turtlebot3_obstacle_detection.py
    │       ├── turtlebot3_patrol
    │       │   ├── __init__.py
    │       │   ├── turtlebot3_patrol_client.py
    │       │   └── turtlebot3_patrol_server.py
    │       └── turtlebot3_relative_move
    │           ├── __init__.py
    │           └── turtlebot3_relative_move.py
    ├── turtlebot3_navigation2
    │   ├── CHANGELOG.rst
    │   ├── CMakeLists.txt
    │   ├── launch
    │   │   └── navigation2.launch.py
    │   ├── map
    │   │   ├── map.pgm
    │   │   └── map.yaml
    │   ├── package.xml
    │   ├── param
    │   │   ├── burger_cam.yaml
    │   │   ├── burger.yaml
    │   │   ├── humble
    │   │   │   ├── burger_cam.yaml
    │   │   │   ├── burger.yaml
    │   │   │   ├── waffle_pi.yaml
    │   │   │   └── waffle.yaml
    │   │   ├── waffle_pi.yaml
    │   │   └── waffle.yaml
    │   └── rviz
    │       └── tb3_navigation2.rviz
    ├── turtlebot3_node
    │   ├── CHANGELOG.rst
    │   ├── CMakeLists.txt
    │   ├── include
    │   │   └── turtlebot3_node
    │   │       ├── control_table.hpp
    │   │       ├── devices
    │   │       │   ├── devices.hpp
    │   │       │   ├── motor_power.hpp
    │   │       │   ├── reset.hpp
    │   │       │   └── sound.hpp
    │   │       ├── diff_drive_controller.hpp
    │   │       ├── dynamixel_sdk_wrapper.hpp
    │   │       ├── odometry.hpp
    │   │       ├── sensors
    │   │       │   ├── battery_state.hpp
    │   │       │   ├── imu.hpp
    │   │       │   ├── joint_state.hpp
    │   │       │   ├── sensors.hpp
    │   │       │   └── sensor_state.hpp
    │   │       ├── turtlebot3.hpp
    │   │       ├── twist_publisher.hpp
    │   │       └── twist_subscriber.hpp
    │   ├── package.xml
    │   ├── param
    │   │   ├── burger.yaml
    │   │   ├── waffle_pi.yaml
    │   │   └── waffle.yaml
    │   └── src
    │       ├── devices
    │       │   ├── motor_power.cpp
    │       │   ├── reset.cpp
    │       │   └── sound.cpp
    │       ├── diff_drive_controller.cpp
    │       ├── dynamixel_sdk_wrapper.cpp
    │       ├── node_main.cpp
    │       ├── odometry.cpp
    │       ├── sensors
    │       │   ├── battery_state.cpp
    │       │   ├── imu.cpp
    │       │   ├── joint_state.cpp
    │       │   └── sensor_state.cpp
    │       └── turtlebot3.cpp
    ├── turtlebot3.repos
    └── turtlebot3_teleop
        ├── CHANGELOG.rst
        ├── package.xml
        ├── resource
        │   └── turtlebot3_teleop
        ├── setup.cfg
        ├── setup.py
        └── turtlebot3_teleop
            ├── __init__.py
            └── script
                ├── __init__.py
                └── teleop_keyboard.py

