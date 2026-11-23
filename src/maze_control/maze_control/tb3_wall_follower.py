import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from math import pi

class LeftWallFollower(Node):
    """左墙跟随：保持左侧墙面距离；前方过小原地右转"""
    def __init__(self):
        super().__init__('tb3_wall_follower')
        self.cmd_pub = self.create_publisher(Twist, '/cmd_vel', 10)
        self.scan_sub = self.create_subscription(LaserScan, '/scan', self.scan_callback, 10)

        self.target_left = 1      # 期望左侧墙距 m
        self.front_danger = 0.35    # 前方危险距离 m
        self.v = 0.15               # 直行速度
        self.w = 0.4                # 转弯角速度

        self.front = 10.0
        self.left = 10.0
        self.timer = self.create_timer(0.1, self.control_loop)

        self.kp=0.6
        self.kd=0.15

        self.err=0
        self.err_last=0


    def scan_callback(self, msg):
        n = len(msg.ranges)
        inc = msg.angle_increment
        a_min = msg.angle_min

        def dist_at(angle_deg):
            # 分区域读取：角度换算成 ranges 索引
            i = int((angle_deg * pi / 180.0 - a_min) / inc)
            i = max(0, min(n - 1, i))
            return msg.ranges[i]

        # 前方 0°±15°；左侧取 60°~90°（正左侧附近）
        self.front = min(dist_at(0), dist_at(15), dist_at(-15))
        self.left = min(dist_at(60), dist_at(75), dist_at(90))

    def control_loop(self):
        self.err_last = self.err
        self.err = self.left - self.target_left
        
        twist = Twist()
        if self.front < self.front_danger:
            # 前方距离过小 → 原地右转
            twist.linear.x = 0.0
            twist.angular.z = -self.w
        elif self.left > self.target_left:
            # 左侧距离偏大 → 向左微调
            if self.err>0.25:
                twist.linear.x = 0.12
            else:
                twist.linear.x = self.v
            twist.angular.z = self.kp*(self.left - self.target_left) + self.kd*(self.err - self.err_last)
        elif self.left < self.target_left:
            # 左侧太近 → 向右微调（防撞墙）
            if self.err<-0.25:
                twist.linear.x = 0.12
            else:
                twist.linear.x = self.v
            twist.angular.z = -self.kp*(self.target_left - self.left) - self.kd*(self.err - self.err_last)
        else:
            # 左侧保持设定距离 → 直线前进
            twist.linear.x = self.v
            twist.angular.z = 0.0
        
        self.cmd_pub.publish(twist)

def main():
    rclpy.init()
    node = LeftWallFollower()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

'''
pkill -f gzserver
pkill -f gzclient
pkill -f gazebo

source /opt/ros/humble/setup.bash
ros2 launch gazebo_ros gazebo.launch.py world:=$HOME/maze_tb3.world
'''

'''
export TURTLEBOT3_MODEL=burger
ros2 run robot_state_publisher robot_state_publisher \
--ros-args -p robot_description:="$(cat $(ros2 pkg prefix turtlebot3_description)/share/turtlebot3_description/urdf/turtlebot3_burger.urdf)"
'''


'''
source /opt/ros/humble/setup.bash
export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:$(ros2 pkg prefix turtlebot3_gazebo)/share/turtlebot3_gazebo/models
ros2 run gazebo_ros spawn_entity.py \
-file $(ros2 pkg prefix turtlebot3_gazebo)/share/turtlebot3_gazebo/models/turtlebot3_burger/model.sdf \
-entity turtlebot3 -x 1 -y 2 -z 0.01 -Y 0


cd ~/ros2maze_ws
colcon build --packages-select maze_control
source install/setup.bash
ros2 run maze_control tb3_wall_follower
'''

