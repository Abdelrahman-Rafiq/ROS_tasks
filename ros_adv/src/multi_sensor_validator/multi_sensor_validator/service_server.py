import rclpy
from rclpy.node import Node
from interfaces.srv import CheckObstacle
from server_logic import Server


class ServerNode(Node):
    def __init__(self):
        super().__init__("Server_Node")
        self.get_logger().info("Server node has been initialized")
        self.srv = self.create_service(
            CheckObstacle, "/check_obstacle", self.process_readings)

    def process_readings(self, request, response):
        ultrasonic = request.sensor_values[0].range
        infrared = request.sensor_values[1].range
        lidar = request.sensor_values[2].range
        self.server = Server(ultrasonic, infrared, lidar)
        response.message, response.obstacle_detected = self.server.process_readings()
        return response


def main(args=None):
    rclpy.init(args=args)
    server = ServerNode()
    rclpy.spin(server)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
