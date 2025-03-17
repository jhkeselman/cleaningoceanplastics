import time
import math


import rclpy
from rclpy.node import Node

from std_msgs.msg import Float64, Bool
from sensor_msgs.msg import NavSatFix
from services.srv import IMUData, GPSdata, KalmanState

import math
import numpy as np

RADIUS = 6371000
UERE = 4.0
AVERAGE = 10

class KalmanService(Node):

    def __init__(self):
        super().__init__('Kalman_service')
        self.srv = self.create_service(KalmanState, 'get_Kalman_state', self.return_state)

        self.imu_cli = self.create_client(IMUData, 'get_IMU_data')
        while not self.imu_cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('IMU service not available, waiting again...')
        self.imu_req = IMUData.Request()

        self.gps_cli = self.create_client(GPSdata, 'get_GPS_fix')
        while not self.gps_cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('GPS service not available, waiting again...')
        self.gps_req = GPSdata.Request()

        self.emergency_stop = self.create_subscription(
            Bool,
            'emergency_stop',
            self.destroy_node,
            10
        )

        
        self.avg_pos = np.zeros((AVERAGE,2))
        self.avg_i = 0
        imu_timer_period = 0.25
        gps_timer_period = 0.5
        self.timer = self.create_timer(imu_timer_period, self.get_imu_data)
        self.timer = self.create_timer(gps_timer_period, self.get_gps_data)

    def return_state(self, request, response):
        response.state = np.zeros(5)
        self.get_logger().info('Incoming request')
        return response
    
    def get_imu_data(self):
        self.imu_future = self.imu_cli.call_async(self.imu_req)
        self.imu_future.add_done_callback(self.imu_response_callback)

    def imu_response_callback(self,future):
        try:
            response = future.result()
            self.get_logger().info('IMU Heading %5.3f, Acc %5.3f, Omega %5.3f:' %(response.heading, response.acceleration, response.omega))
        except Exception as e:
            self.get_logger().error(f'Service call failed {str(e)}')

    def get_gps_data(self):
        self.gps_future = self.gps_cli.call_async(self.gps_req)
        self.gps_future.add_done_callback(self.gps_response_callback)

    def gps_response_callback(self,future):
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

    def destroy_node(self,msg):
        time.sleep(0.1)
        super().destroy_node()

def main():
    rclpy.init()

    kalman_service = KalmanService()

    rclpy.spin(kalman_service)
    kalman_service.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()