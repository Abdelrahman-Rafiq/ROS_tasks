import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/rafiq/Desktop/task1_ws/install/multi_sensor_validator'
