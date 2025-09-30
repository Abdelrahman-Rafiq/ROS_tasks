class Server:
    def __init__(self, ultrasonic, infrared, lidar):
        self.ultrasonic = ultrasonic
        self.infrared = infrared
        self.lidar = lidar
        self.obstacle = False

    def process_readings(self):
        message = "Obstacle detected by: "
        if self.ultrasonic < 50:
            message += "ultrasonic"
            self.obstacle = True
        if self.infrared < 50:
            if self.obstacle:
                message += ", "
            message += "infrared"
            self.obstacle = True
        if self.lidar < 50:
            if self.obstacle:
                message += ", "
            message += "lidar"
            self.obstacle = True
        if self.obstacle == False:
            message = "path is clear"
        return message, self.obstacle
