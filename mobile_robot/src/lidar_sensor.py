#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import LaserScan


class sensor_cheking:

    def __init__(self):
        sub_topic_name ="/scan"
        self.lidar_subscriber = rospy.Subscriber(sub_topic_name, LaserScan, self.lidar_cb)

    def lidar_cb(self, data):
        region_a = min( min(data.ranges[0:120]) , 10 ) #infinity
        region_b = min(data.ranges[121:240])
        region_c = min(data.ranges[241:360])
        print("A :" , round(region_a,3) , " B :", round(region_b,3) , " C ", round(region_c,3) )


        if

if __name__ == '__main__':
    node_name ="lidar_check"
    rospy.init_node(node_name)
    sensor_cheking()
    rospy.spin()