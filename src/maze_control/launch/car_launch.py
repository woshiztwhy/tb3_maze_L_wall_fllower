import os
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    # 【改成自己world文件的路径！】
    world_path = "/home/zty/ros2maze_ws/src/custom/my_obstacle.world"

    # 启动Gazebo，加载自定义world
    gazebo = ExecuteProcess(
        cmd=[
            "gazebo",
            "--verbose",
            world_path,
            "-s", "libgazebo_ros_init.so",
            "-s", "libgazebo_ros_factory.so"
        ],
        output="screen"
    )

    # 生成TurtleBot3 Burger小车
    spawn_tb3 = Node(
        package="gazebo_ros",
        executable="spawn_entity.py",
        arguments=[
            "-topic", "robot_description",
            "-entity", "turtlebot3_burger",
            "-x", "0.0", "-y", "0.0", "-z", "0.01"
        ],
        output="screen"
    )

    # robot_state_publisher，发布机器人URDF
    tb3_model_dir = get_package_share_directory("turtlebot3_gazebo")
    urdf_path = os.path.join(tb3_model_dir, "models", "turtlebot3_burger", "model.sdf")
    robot_state_pub = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[{"robot_description": open(urdf_path).read()}]
    )

    return LaunchDescription([
        gazebo,
        robot_state_pub,
        spawn_tb3
    ])