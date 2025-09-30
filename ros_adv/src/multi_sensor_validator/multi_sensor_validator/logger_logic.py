class Logger:
    def __init__(self,sensors_readings:list,quality):
        self.sensors_readings = sensors_readings
        self.ultrasonic = sensors_readings[0]
        self.infrared = sensors_readings[1]
        self.lidar = sensors_readings[2]
        self.quality = quality
        self.obstacle = False
        self.message = ""
    
    def get_logger_message(self):
        for reading in self.sensors_readings:
            if reading <= 100:
                self.obstacle = True
        
        if self.quality > 50:
            if self.obstacle:
                self.message = f"Quality={self.quality} -> ultrasonic : {self.ultrasonic:.2f} , infrared :{self.infrared:.2f}, LiDAR :{self.lidar:.2f}->Obstacle detected"
            else:
                self.message = f"Quality={self.quality} -> ultrasonic : {self.ultrasonic:.2f} , infrared :{self.infrared:.2f}, LiDAR :{self.lidar:.2f}->Path clear"
            
        else :
            self.message =f"Quality={self.quality} -> QUALITY REJECTED"
        return self.message