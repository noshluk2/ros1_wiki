#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

from service_pkg.srv import velocity , velocityResponse

class vel_manipulator:

    def __init__(self):
        pub_topic_name ="/turtle1/cmd_vel"
        sub_topic_name ="/turtle1/pose"

        self.pub = rospy.Publisher(pub_topic_name, Twist, queue_size=10)
        self.number_subscriber = rospy.Subscriber(sub_topic_name, Pose, self.pose_callback)
        self.service = rospy.Service('velocity_change_service', velocity, self.velocity_change_cb)

        self.velocity_msg = Twist()

    def velocity_change_cb(self,request):
        self.velocity_msg.linear.x = request.vel
        self.velocity_msg.angular.z = request.angle

        return "Velocity of the robot has been changed"

    def pose_callback(self, msg):
        self.pub.publish(self.velocity_msg)


if __name__ == '__main__':
    node_name ="Turtlesim_testing"
    rospy.init_node(node_name)
    vel_manipulator()
    rospy.spin()