import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class PCA (Node):
    def __init__(self,channels):
        super().__init__("PCA_Node")
        self.get_logger().info("PCA Node has been initialized")
        self.sub_ = self.create_subscription(String,"/pwm_data",self.handle_pwm_data,10)
        self.publisher_ = self.create_publisher(String,"/thruster_data",10)
        self.timer = self.create_timer(1,self.send_thrusters)
        self.period = 20000
        self.pwm_range = 65535
        self.channels =[]
        self.required_channels = []
        for i in range(channels): self.channels.append(i+1)
        self.value =0
        
    def handle_pwm_data(self,msg:String):
        data =msg.data
        self.direction = data.split(":")[0]
        value =int(data.split(":")[1])
        if self.direction == "RL":
            self.required_channels = [channel for channel in self.channels if channel not in [1,5]]
        elif self.direction == "UD":
            self.required_channels = [channel for channel in self.channels if channel not in [3,7]]
        self.value = self.duty_to_microseconds(value)
    
    def duty_to_microseconds(self,value):
        return int((value / self.pwm_range) * self.period)

    def send_thrusters (self):
        msg =String()
        msg.data = f"{self.required_channels}||{self.value}"
        self.publisher_.publish(msg)
        self.get_logger().info(msg.data)
def main(args = None):
    rclpy.init(args=args)
    pca = PCA(8)
    rclpy.spin(pca)
    rclpy.shutdown()

if __name__ == "__main__":
    main()