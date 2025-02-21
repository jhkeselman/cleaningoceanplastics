from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(package='test_input', executable='teleop', output='screen'),
        Node(package='test_input', executable='motor_control', output='screen'),
        Node(package='test_input', executable='control', output='screen'),
        Node(package='test_input', executable='imu_srv', output='screen'),
        Node(package='test_input', executable='water_sensor', output='screen'),
        Node(package='nmea_navsat_driver', executable='nmea_serial_driver', output='screen'),
    ])
