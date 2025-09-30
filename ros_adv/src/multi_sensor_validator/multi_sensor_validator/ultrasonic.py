
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import random


class UltraSonic(Node):
    def __init__(self):
        super().__init__("UltraSonic_sensor")
        self.get_logger().info("UltraSonic Sensor has been initialized")
        self.publisher_ = self.create_publisher(
            String, "/ultrasonic_range", 10)
        self.create_timer(1, self.generate_readings)

    def generate_readings(self):
        msg = String()
        msg.data = f"{random.uniform(0.02,5.0):.2f}"
        self.get_logger().info(f"Ultrasonic sensor has published {msg.data}")
        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    ultrasonic = UltraSonic()
    rclpy.spin(ultrasonic)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
