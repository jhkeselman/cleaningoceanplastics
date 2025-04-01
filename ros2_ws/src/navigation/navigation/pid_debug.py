import rclpy
from rclpy.node import Node
import struct
import sys
import time
from sys import stdin
import select
import smbus

class PIDDebug(Node):
    def __init__(self):
        super().__init__('pid_debug')
        
        self.timer = self.create_timer(0.1, self.check_input)

        self.I2C_address = 0x55 #I2C address of ESP32
        self.bus = smbus.SMBus(1)       

    def check_input(self):
        if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
            key = sys.stdin.read(1)
            key = key.strip()
            if key:
                self.process_key(key)

    def process_key(self, key):
        data = 0
        
        # 2 is P, 3 is I, 4 is D
        if key[0] == 'p':
            data = struct.pack('if',2,key[1:])
        elif key[0] == 'i':
            data = struct.pack('if',3,key[1:])
        elif key[0] == 'd':
            data = struct.pack('if',4,key[1:])
        
        # Compile into byte list and send over
        byte_list = list(data)
        try:
            self.bus.write_i2c_block_data(self.I2C_address, 0, byte_list)
        except:
            self.get_logger().info("Failed to send value")


    def destroy_node(self):
        time.sleep(0.1)
        super().destroy_node()

def main(args=None):
    rclpy.init(args=args)

    pid_debug = PIDDebug()
    try:
        rclpy.spin(pid_debug)
    finally:
        pid_debug.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()