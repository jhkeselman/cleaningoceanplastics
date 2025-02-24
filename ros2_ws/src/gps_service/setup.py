from setuptools import find_packages, setup

package_name = 'gps_service'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    zip_safe=True,
    install_requires=['setuptools',
                    'pyserial',
                    'numpy',
                    'pyyaml'],
    maintainer='johnk',
    maintainer_email='jkhall@wpi.edu',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': ['gps_srv = nmea_service_driver:main'
        ],
    },
)
