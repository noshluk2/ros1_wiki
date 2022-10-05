#!/usr/bin/env python3
# license removed for brevity
import rospy
from std_msgs.msg import Int16

def number_publisher():
    pub = rospy.Publisher('number_out', Int16, queue_size=10)
    rospy.init_node('int_publisher')
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        num_msg = 23

        pub.publish(num_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        number_publisher()
    except rospy.ROSInterruptException:
        pass