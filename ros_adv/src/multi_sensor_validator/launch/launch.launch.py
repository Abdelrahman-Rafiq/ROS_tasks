from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package= 'multi_sensor_validator',
            namespace='multi_sensor_validator',
            executable ='ultrasonic',
            name ='ultrasonic',
        ),
        Node(
            package= 'multi_sensor_validator',
            namespace='multi_sensor_validator',
            executable ='infrared',
            name ='infrared',
        ),
        Node(
            package= 'multi_sensor_validator',
            namespace='multi_sensor_validator',
            executable ='lidar',
            name ='lidar',
        ),
        Node(
            package= 'multi_sensor_validator',
            namespace='multi_sensor_validator',
            executable ='validator',
            name ='validator',
        ),
        Node(
            package= 'multi_sensor_validator',
            namespace='multi_sensor_validator',
            executable ='logger',
            name ='logger',
        ),
        Node(
            package= 'multi_sensor_validator',
            namespace='multi_sensor_validator',
            executable ='client',
            name ='client',
        ),
        Node(
            package= 'multi_sensor_validator',
            namespace='multi_sensor_validator',
            executable ='server',
            name ='server',
        ),
   ] )