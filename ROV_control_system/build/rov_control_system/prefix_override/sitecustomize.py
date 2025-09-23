import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/rafiq/Desktop/ROV_control_system/install/rov_control_system'
