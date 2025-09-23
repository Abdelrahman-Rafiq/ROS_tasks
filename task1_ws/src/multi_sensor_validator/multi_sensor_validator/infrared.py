#! usr/bin/python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import random


class InfraRed(Node):
    def __init__(self):
        super().__init__("Infrared_sensor")
        self.get_logger().info("Infrared Sensor has been initialized")
        self.publisher_ = self.create_publisher(String,"/infrared_range",10)
        self.create_timer(1,self.generate_readings)
    def generate_readings(self):
        msg = String()
        msg.data = f"{random.randint(10,200)}"
        self.get_logger().info(f"Infrared sensor has published {msg.data}")
        self.publisher_.publish(msg)



def main(args = None):
    rclpy.init(args=args)
    infrared = InfraRed()
    rclpy.spin(infrared)
    rclpy.shutdown()

if __name__ == "__main__":
    main()