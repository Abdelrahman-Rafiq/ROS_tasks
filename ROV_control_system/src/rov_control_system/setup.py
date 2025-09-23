from setuptools import find_packages, setup

package_name = 'rov_control_system'

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
            "joystick=rov_control_system.joystick:main",
            "navigation=rov_control_system.navigation:main",
            "pca=rov_control_system.PCA:main",
            "thrusters=rov_control_system.thrusters:main",
        ],
    },
)
