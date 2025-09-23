import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Navigation(Node):
    def __init__(self):
        super().__init__("Navigation_Node")
        self.get_logger().info("Navigation Node has been initialized")
        self.command =""
        self.command_value = 0
        self.exp_flag = False
        self.sub_ =self.create_subscription(String,"/joystick_data",self.handle_joystick_data,10)
        self.publisher_ = self.create_publisher(String,"/pwm_data",10)
        self.timer =self.create_timer(0.25,self.control_smooth)
        self.last_pwm = 4915
        self.new_pwm = 4915
    def handle_joystick_data(self,msg:String):
        data = msg.data 
        if data.startswith("0"):
            data = data.split(":")
            data = float(data[1])
            self.command_value = data
            self.command = "RL"
        elif data.startswith("1"):
            data = data.split(":")
            data = float(data[1])
            self.command_value = -1*data
            self.command = "UD"
        elif data in ["right","left"]:
            self.command = "RL"
            if data == "right":self.command_value = 1
            else :self.command_value= -1      
        elif data in ["down","up"]:
            self.command = "UD"
            if data == "up" :  self.command_value = 1
            else :self.command_value= -1
        elif data.startswith("pressed") : 
            if self.exp_flag == False: self.exp_flag = True
            else : self.exp_flag = False

    def PWMMapper (self,value):
        if value >= 0:
            return  value * 1639 + 4915
        if value < 0:
            return (value+1)*1639 + 3277
        
    def linear_smooth(self):
        if self.new_pwm > self.last_pwm and self.last_pwm+25<=6554:
            self.new_pwm  = self.last_pwm + 25
        elif self.new_pwm < self.last_pwm and self.last_pwm-25>=6554:
            self.new_pwm = self.last_pwm -25 
        self.last_pwm = self.new_pwm
        return self.new_pwm
    
    def exp_smooth(self):
        if self.new_pwm > self.last_pwm and self.last_pwm*2<=6554:
            self.new_pwm  = self.last_pwm * 2
        elif self.new_pwm < self.last_pwm and self.last_pwm //2 >=3277:
            self.new_pwm = self.last_pwm //2
        self.last_pwm = self.new_pwm
        return self.new_pwm

    def control_smooth(self):
        msg = String()
        self.new_pwm = self.PWMMapper(self.command_value)
        if self.exp_flag : msg.data =str(self.exp_smooth())
        else : msg.data =str(self.linear_smooth())
        msg.data = f"{self.command}:{msg.data}"
        self.publisher_.publish(msg)
        self.get_logger().info(msg.data)
        

def main(args = None):
    rclpy.init(args=args)
    navigation = Navigation()
    rclpy.spin(navigation)
    rclpy.shutdown()

if __name__ == "__main__":
    main()