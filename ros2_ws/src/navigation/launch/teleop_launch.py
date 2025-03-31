from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    sensors_launch_path = os.path.join(
        get_package_share_directory('sensors'),
        'launch',
        'sensors.launch.py'
    )

    return LaunchDescription([
        IncludeLaunchDescription(PythonLaunchDescriptionSource(sensors_launch_path)),
        Node(package='navigation', executable='motor_control', output='screen'),
    ])
