
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import random


class Lidar(Node):
    def __init__(self):
        super().__init__("Lidar")
        self.get_logger().info("Lidar Sensor has been initialized")
        self.publisher_ = self.create_publisher(String, "/lidar_range", 10)
        self.create_timer(1, self.generate_readings)

    def generate_readings(self):
        msg = String()
        msg.data = f"{random.uniform(0.1,10.0):.2f}"
        self.get_logger().info(f"lidar sensor has published {msg.data}")
        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    lidar = Lidar()
    rclpy.spin(lidar)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
