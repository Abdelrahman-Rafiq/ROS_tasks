#! /usr/bin/python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class Logger(Node):
    def __init__(self):
        super().__init__("Logger_Node")
        self.get_logger().info("Logger has been initialized")
        self.sub_ = self.create_subscription(String,"/validation_result",self.print_state,10)
        
    def print_state(self,msg:String):
        data = msg.data
        self.get_logger().info(data)
       

def main(args = None):
    rclpy.init(args=args)
    logger = Logger()
    rclpy.spin(logger)
    rclpy.shutdown()

if __name__ == "__main__":
    main()