from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(package='sensors', executable='control', output='screen'),
        Node(package='sensors', executable='imu_srv', output='screen'),
        Node(package='sensors', executable='water_sensor', output='screen'),
        Node(package='nmea_navsat_driver', executable='nmea_serial_driver', output='screen'),
    ])
