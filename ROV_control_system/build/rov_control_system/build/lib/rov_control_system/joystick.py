import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import pygame
import time


class Joystick(Node):
    def __init__(self,id):
        super().__init__("Joystick")
        self.joystick = pygame.joystick.Joystick(id)
        self.joystick.init()
        self.publisher_ = self.create_publisher(String,"/joystick_data",10)
        self.get_logger().info("Joystick node has been initialized")
        self.create_timer(1.0,self.find_status)
        

    def button_analog_status(self):
        pygame.event.pump()
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 13:
                    return "up"
                elif event.button == 14:
                    return "down"
                
                elif event.button == 15:
                    return "left"
                
                elif event.button == 16:
                    return "right"
                else :
                    return event.button
            if event.type == pygame.JOYAXISMOTION:
                if event.axis == 0:
                    if abs(event.value )>0.2 : return f"0:{event.value:.2f}"
                if event.axis == 1:
                    if abs(event.value )>0.2 : return f"1:{event.value:.2f}"
                


    def find_status (self):
        msg = String()
        data = self.button_analog_status()
        msg.data = data
        self.publisher_.publish(msg)
        self.get_logger().info(f"joystick has published : {msg.data}")


def main(args = None):
    pygame.init()
    pygame.joystick.init()
    pygame.display.set_mode((500, 500)) 
    rclpy.init(args=args)
    joystick = Joystick(0)
    rclpy.spin(joystick)
    rclpy.shutdown()

if __name__ == "__main__":
    main()