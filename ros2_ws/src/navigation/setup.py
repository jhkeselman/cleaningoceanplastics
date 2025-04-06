from setuptools import find_packages, setup
from glob import glob

package_name = 'navigation'

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
    install_requires=['setuptools','smbus'],
    zip_safe=True,
    maintainer='pi2',
    maintainer_email='coop530@comcast.net',
    description='TODO: Package description',
    license='TODO: License declaration',
    entry_points={
        'console_scripts': [
            'motor_control = navigation.motor_controller:main',
            'teleop = navigation.teleop:main',
            'pid_debug = navigation.pid_debug:main'
        ],
    },
)
