import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/cooper530/MQP/cleaningoceanplastics/install/nmea_navsat_driver'
