from logger_logic import Logger
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from interfaces.msg import SensorProperties


class LoggerNode(Node):
    def __init__(self):
        super().__init__("Logger_Node")
        self.get_logger().info("Logger has been initialized")
        self.sub_ = self.create_subscription(
            SensorProperties, "/sensor_properties", self.print_state, 10)
        self.obstacle = False

    def print_state(self, msg: SensorProperties):
        quality = msg.quality
        ultrasonic_reading = msg.sensor_values[0].range * 100
        infrared_reading = msg.sensor_values[1].range * 100
        lidar_reading = msg.sensor_values[2].range * 100
        sensors_list = [ultrasonic_reading, infrared_reading, lidar_reading]
        logger = Logger(sensors_readings=sensors_list, quality=quality)
        message = logger.get_logger_message()
        self.get_logger().info(message)


def main(args=None):
    rclpy.init(args=args)
    logger = LoggerNode()
    rclpy.spin(logger)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
