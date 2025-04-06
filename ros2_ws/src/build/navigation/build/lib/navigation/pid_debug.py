import rclpy, struct, sys, time, select, smbus
from rclpy.node import Node
from sys import stdin

# This node can be used to debug PID constants on the ESP32 microcontroller (for heading control).
# It listens for key commands (ex. 'p0.5', 'i0.5', or 'd0.5') to modify the PID constants over I2C.
# Publishers: ''
# Subscribers: ''

class PIDDebug(Node):
    def __init__(self):
        super().__init__('pid_debug')
        
        # Create the timer to check keyboard inputs
        self.timer = self.create_timer(0.1, self.check_input)

        # Setup I2C device
        self.I2C_address = 0x55 #I2C address of ESP32
        self.bus = smbus.SMBus(1)       

    # Callback function to handle keyboard logic
    def check_input(self):
        # If information available, read the line and strip, send to other method to process
        if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
            key = sys.stdin.readline()
            key = key.strip()
            if key:
                self.process_key(key)

    # Processes the key input and sends message over I2C
    def process_key(self, key):
        data = None
        # 2 is P, 3 is I, 4 is D (pack the data into a byte array)
        if key[0] == 'p':
            data = struct.pack('if',2,float(key[1:]))
        elif key[0] == 'i':
            data = struct.pack('if',3,float(key[1:]))
        elif key[0] == 'd':
            data = struct.pack('if',4,float(key[1:]))
        
        try:
            # Compile into byte list and send over
            byte_list = list(data)
            self.bus.write_i2c_block_data(self.I2C_address, 0, byte_list)
        except:
            self.get_logger().info("Failed to send value")

    # Destroys the node
    def destroy_node(self):
        time.sleep(0.1)
        super().destroy_node()

# ROS stuff here
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