#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge

class sensor_cheking:

    def __init__(self):
        sub_topic_name ="/camera/rgb/image_raw"
        self.camera_subscriber = rospy.Subscriber(sub_topic_name, Image, self.camera_cb)
        self.out = cv2.VideoWriter('/home/luqman/output.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (640,480))
        self.bridge = CvBridge()

    def camera_cb(self, data):
        frame = self.bridge.imgmsg_to_cv2(data)
        print(frame.shape)
        # edge_frame = cv2.Canny(frame, 100, 200)
        # self.out.write(frame)
        cv2.imshow("output" , frame)
        cv2.waitKey(1)




if __name__ == '__main__':
    node_name ="camera_check"
    rospy.init_node(node_name)
    sensor_cheking()
    rospy.spin()