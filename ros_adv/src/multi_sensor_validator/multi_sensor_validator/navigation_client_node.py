import rclpy
from rclpy.node import Node
from interfaces.srv import CheckObstacle
from interfaces.msg import SensorProperties
from functools import partial


class Client(Node):
    def __init__(self):
        super().__init__("Client_node")
        self.get_logger().info("Client node has been initialized")
        self.ultrasonic_reading = 0.0
        self.infrared_reading = 0.0
        self.lidar_reading = 0.0
        self.sub_ = self.create_subscription(
            SensorProperties, "/sensor_properties", self.get_sensor_data, 10)
        self.client = self.create_client(CheckObstacle, '/check_obstacle')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("Waiting for the service to be available")
        self.timer = self.create_timer(1.0, self.send_request)

    def get_sensor_data(self, msg: SensorProperties):
        self.ultrasonic_reading = msg.sensor_values[0].range * 100
        self.infrared_reading = msg.sensor_values[1].range * 100
        self.lidar_reading = msg.sensor_values[2].range * 100

    def send_request(self):
        request = CheckObstacle.Request()
        ultrasonic = self.ultrasonic_reading
        infrared = self.infrared_reading
        lidar = self.lidar_reading
        request.sensor_values[0].range = ultrasonic
        request.sensor_values[1].range = infrared
        request.sensor_values[2].range = lidar
        future = self.client.call_async(request=request)
        self.get_logger().info(
            f"Request sent → Ultrasonic: {ultrasonic:.2f}cm, Infrared:{infrared:.2f}cm , LiDAR: {lidar:.2f} cm")
        future.add_done_callback(partial(self.future_callback))

    def future_callback(self, future):
        response = future.result()
        message = f"Response → {response.message} "
        self.get_logger().info(message)


def main(args=None):
    rclpy.init(args=args)
    client = Client()
    rclpy.spin(client)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
