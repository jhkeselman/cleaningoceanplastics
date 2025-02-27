from setuptools import find_packages, setup
from glob import glob

package_name = 'sensors'

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
    install_requires=['setuptools','numpy'],
    zip_safe=True,
    maintainer='pi2',
    maintainer_email='pi2@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    py_modules=[
        'sensors.IMU_lib',  # Path to IMU_lib.py
    ],
    entry_points={
        'console_scripts': [
            'water_sensor = sensors.water_sensor:main',
            'imu_pub = sensors.imu_publisher:main',
            'object_detector = sensors.object_detector:main',
            'object_selector = sensors.object_selector:main',
            'gps_subscriber = sensors.gps_subscriber:main',
            'imu_srv = sensors.imu_service:main',
            'imu_cli = sensors.imu_client:main',
            'kalman = sensors.Kalman_service:main'
        ],
    },
)
