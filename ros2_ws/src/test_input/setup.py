from setuptools import find_packages, setup

package_name = 'test_input'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='pi2',
    maintainer_email='pi2@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    py_modules=[
        'test_input.IMU',  # Path to IMU.py
    ],
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'water_sensor = test_input.water_sensor:main',
            'imu = test_input.imu_publisher:main',
            'object_detector = test_input.object_detector:main',
            'object_selector = test_input.object_selector:main',
            'gps_subscriber = test_input.gps_subscriber:main'
        ],
    },
)
