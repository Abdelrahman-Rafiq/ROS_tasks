import rclpy
from rclpy.node import Node
import random
from std_msgs.msg import String
from interfaces.msg import SensorProperties


class Validator(Node):
    def __init__(self):
        super().__init__("Validator_Node")
        self.get_logger().info("Validator Node has been initialized")
        self.publisher_ = self.create_publisher(
            SensorProperties, "/sensor_properties", 10)
        self.us_subscriber = self.create_subscription(
            String, "/ultrasonic_range", self.get_ultrasonic, 10)
        self.IR_subscriber = self.create_subscription(
            String, "/infrared_range", self.get_infrared, 10)
        self.Lidar_subscriber = self.create_subscription(
            String, "/lidar_range", self.get_lidar, 10)
        self.ultrasonic_reading = 0.0
        self.infrared_reading = 0.0
        self.lidar_reading = 0.0
        self.create_timer(1, self.send_validation_state)

    def get_ultrasonic(self, msg: String):
        self.ultrasonic_reading = float(msg.data)

    def get_infrared(self, msg: String):
        self.infrared_reading = float(msg.data)

    def get_lidar(self, msg: String):
        self.lidar_reading = float(msg.data)

    def send_validation_state(self):
        msg = SensorProperties()
        msg.quality = random.randint(1, 100)
        msg.sensor_values[0].min_range = 0.02
        msg.sensor_values[0].max_range = 5.0
        msg.sensor_values[0].range = self.ultrasonic_reading
        msg.sensor_values[1].min_range = 0.01
        msg.sensor_values[1].max_range = 0.8
        msg.sensor_values[1].range = self.infrared_reading
        msg.sensor_values[2].min_range = 0.1
        msg.sensor_values[2].max_range = 10.0
        msg.sensor_values[2].range = self.lidar_reading

        self.publisher_.publish(msg)
        self.get_logger().info(
            f'validator has published with {msg.quality} qulaity: ultrasonic ={msg.sensor_values[0].range:.2f}m, infrared ={msg.sensor_values[1].range:.2f}m and lidar = {msg.sensor_values[2].range:.2f}m')


def main(args=None):
    rclpy.init(args=args)
    validator = Validator()
    rclpy.spin(validator)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
