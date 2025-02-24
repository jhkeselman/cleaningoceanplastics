from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(package='sensors', executable='teleop', output='screen'),
        Node(package='sensors', executable='motor_control', output='screen'),
    ])
