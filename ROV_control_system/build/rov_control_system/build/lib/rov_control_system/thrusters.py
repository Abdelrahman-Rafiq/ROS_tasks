import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class Thrusters (Node):
    def __init__ (self):
        super().__init__("thrusters")
        self.get_logger().info("thrusters have been intialized")
        self.sub_ = self.create_subscription(String,"/thruster_data",self.set_speed,10)
    
    def set_speed(self,msg:String):
        data = msg.data
        ls = data.split(":")
        channels_list = ls[0]
        speed = ls[1]
        speed = speed - 1500
        speed = speed / 500
        self.get_logger().info(f"{channels_list} is moving with speed : {speed}")

def main(args = None):
    rclpy.init(args=args)
    thrusters = Thrusters()
    rclpy.spin(thrusters)
    rclpy.shutdown()

if __name__ == "__main__":
    main()


# thrusters view
#      1
#    8   2
#   7     3 
#    6   4
#      5