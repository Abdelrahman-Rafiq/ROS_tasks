#! /usr/bin/python3
import rclpy
from rclpy.node import Node
import random
from std_msgs.msg import String

class Validator(Node):
    def __init__(self):
        super().__init__("Validator_Node")
        self.get_logger().info("Validator Node has been initialized")
        self.publisher_ = self.create_publisher(String,"/validation_result",10)
        self.us_subscriber=self.create_subscription(String,"/ultrasonic_range",self.get_ultrasonic,10)
        self.IR_subscriber=self.create_subscription(String,"/infrared_range",self.get_infrared,10)
        self.ultrasonic_reading = 0
        self.infrared_reading =0
        self.create_timer(1,self.send_validation_state)

    def get_ultrasonic(self,msg:String):
        self.ultrasonic_reading = int(msg.data)

    def get_infrared(self,msg:String):
        self.infrared_reading = int(msg.data)

    def send_validation_state(self):
        msg = String()
        diff = self.ultrasonic_reading - self.infrared_reading
        if 0<= abs(diff)<= 20:
            msg.data = f"Ultrasonic: {self.ultrasonic_reading},Infrared: {self.infrared_reading} -> Sensor readings consistent"
        else:
            msg.data = f"Ultrasonic: {self.ultrasonic_reading},Infrared: {self.infrared_reading} ->Sensor readings inconsistent"
        self.publisher_.publish(msg)
        

def main(args = None):
    rclpy.init(args=args)
    validator = Validator()
    rclpy.spin(validator)
    rclpy.shutdown()

if __name__ == "__main__":
    main()