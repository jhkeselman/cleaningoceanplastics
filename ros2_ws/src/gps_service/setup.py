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
        ('share/' + package_name, ['share/test_nmea_path.txt']),
    ],
    zip_safe=True,
    install_requires=['setuptools',
                    'pyserial',
                    'numpy',
                    'pyyaml',
                    'gps'],
    py_modules=[
        'gps_service.checksum_utils',
        'gps_service.parser',
        'gps_service.driver'
    ],
    maintainer='johnk',
    maintainer_email='jkhall@wpi.edu',
    description='TODO: Package description',
    license='TODO: License declaration',
    entry_points={
        'console_scripts': ['gps_srv = gps_service.nmea_service_driver:main',
                            'gps_cli = gps_service.gps_client:main',
                            'fix_srv = gps_service.fix_service:main'
        ],
    },
)
