import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/pi2/cleaningoceanplastics/ros2_ws/src/install/sensors'
