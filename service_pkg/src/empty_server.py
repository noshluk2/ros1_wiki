#!/usr/bin/env python3
'''
To run this service you need to call through a client ( terminal as an example )
'''
from std_srvs.srv import Empty,EmptyResponse
import rospy
from geometry_msgs.msg import Twist

def empty_response_cb(req):
    vel_msg = Twist()
    for i in range(10):
        vel_msg.linear.x= 1.0
        vel_msg.angular.z= 0.5
        pub.publish(vel_msg)
        rate.sleep()
    print("Just a service")
    return EmptyResponse()

if __name__ == "__main__":
    rospy.logwarn("Starting Empty Server")
    rospy.init_node('empty_server_service')
    pub= rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=2)
    s = rospy.Service('print_service', Empty, empty_response_cb)
    rate = rospy.Rate(1)

    rospy.spin()