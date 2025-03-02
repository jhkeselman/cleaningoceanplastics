import sys
import time
import math

from std_msgs.msg import Bool
from sensor_msgs.msg import NavSatFix
from services.srv import GPSdata
import rclpy
from rclpy.node import Node
import numpy as np


RADIUS = 6371000
UERE = 4.0
AVERAGE = 10

class GPSClient(Node):

    def __init__(self):
        super().__init__('gps_client')
        self.cli = self.create_client(GPSdata, 'get_GPS_fix')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = GPSdata.Request()
        self.emergency_stop = self.create_subscription(
            Bool,
            'emergency_stop',
            self.destroy_node,
            10
        )
        timer_period = 1
        self.timer = self.create_timer(timer_period, self.send_request)
        self.avg_pos = np.zeros((AVERAGE,2))
        self.avg_i = 0

    def send_request(self):
        # self.get_logger().info('Sent Request')
        self.future = self.cli.call_async(self.req)
        self.future.add_done_callback(self.response_callback)
    
    def response_callback(self,future):
        try:
            response = future.result()
            fix_status = response.fix.status.status
            if fix_status >=0 :
                self.get_logger().info('GPS Fix %d, Lat %5.8f, Long %5.8f:' %(fix_status, response.fix.latitude, response.fix.longitude))
                self.get_logger().info('GPS Covariance Long %5.3f, Lat %5.2f' %(response.fix.position_covariance[0], response.fix.position_covariance[0]))
                if self.avg_i < AVERAGE-1:
                    fix = [math.radians(response.fix.latitude), math.radians(response.fix.longitude)]
                    self.avg_pos[self.avg_i,:] = fix    
                    self.avg_i += 1               
                elif self.avg_i == AVERAGE-1:
                    fix = [math.radians(response.fix.latitude), math.radians(response.fix.longitude)]
                    self.avg_pos[self.avg_i,:] = fix
                    avg_lat = self.avg_pos[:,0].mean(axis=0)
                    avg_lon = self.avg_pos[:,1].mean(axis=0)
                    self.first_fix = [avg_lat,avg_lon,math.cos(avg_lat)]
                    self.covariance = self.calc_covariance(response.fix)
                    self.dx = 0
                    self.dy = 0
                    self.get_logger().info('Position (X,Y): (%5.3f +/- %5.3f, %5.3f +/- %5.3f)' %(self.dx,self.covariance[0][0],self.dy,self.covariance[1][1]))  
                    self.avg_i += 1
                else:
                    [self.dx,self.dy] = self.calc_dist(response.fix)
                    self.covariance = self.calc_covariance(response.fix)
                    self.get_logger().info('Position (X,Y): (%5.3f +/- %5.3f, %5.3f +/- %5.3f)' %(self.dx,self.covariance[0][0],self.dy,self.covariance[1][1]))  
            else:
                 self.get_logger().info('No GPS Fix')


        except Exception as e:
            self.get_logger().error(f'Service call failed {str(e)}')

    def destroy_node(self,msg):
        time.sleep(0.1)
        super().destroy_node()
        
    def calc_dist(self,fix):
        dx = RADIUS*(math.radians(fix.longitude) - self.first_fix[1])*self.first_fix[2]
        dy = RADIUS*(math.radians(fix.latitude) - self.first_fix[0])
        return [dx,dy]
    
    def calc_covariance(self,fix):
        if fix.position_covariance_type == NavSatFix.COVARIANCE_TYPE_APPROXIMATED:
            x_lon = fix.position_covariance[0]*UERE
            y_lat = fix.position_covariance[4]*UERE
        else:
            x_lon = fix.position_covariance[0]
            y_lat = fix.position_covariance[4]
        sigma_x = x_lon
        sigma_y = y_lat

        covariance = np.array([[sigma_x**2,0],[0,sigma_y**2]])
        return covariance

def main(args=None):
    rclpy.init(args=args)

    gps_client = GPSClient()
    rclpy.spin(gps_client)
    gps_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()