from setuptools import find_packages, setup
from glob import glob

package_name = 'test_input'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', glob('launch/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='pi2',
    maintainer_email='pi2@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    py_modules=[
        'test_input.IMU_lib',  # Path to IMU_lib.py
    ],
    entry_points={
        'console_scripts': [
            'water_sensor = test_input.water_sensor:main',
            'imu_pub = test_input.imu_publisher:main',
            'object_detector = test_input.object_detector:main',
            'object_selector = test_input.object_selector:main',
            'gps_subscriber = test_input.gps_subscriber:main',
            'imu_srv = test_input.imu_service:main',
            'imu_cli = test_input.imu_client:main',
            'control = test_input.control:main',
            'kalman = test_input.Kalman_service:main',
            'motor_control = test_input.motor_controller:main'
        ],
    },
)
