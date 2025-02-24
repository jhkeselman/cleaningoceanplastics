from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(package='test_input', executable='teleop', output='screen'),
        Node(package='test_input', executable='motor_control', output='screen'),
    ])
