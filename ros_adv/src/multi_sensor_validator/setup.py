from setuptools import find_packages, setup

package_name = 'multi_sensor_validator'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name ,['launch/launch.launch.py'])
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='rafiq',
    maintainer_email='rafiq@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            "ultrasonic=multi_sensor_validator.ultrasonic:main",
            "infrared = multi_sensor_validator.infrared:main",
            "lidar=multi_sensor_validator.lidar:main",
            "validator= multi_sensor_validator.validator:main",
            "logger= multi_sensor_validator.logger:main",
            "server= multi_sensor_validator.service_server:main",
            "client= multi_sensor_validator.navigation_client_node:main",
        ],
    },
)
