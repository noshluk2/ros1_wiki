#!/usr/bin/env python3

import sys
import rospy

from service_pkg.srv import addition , additionResponse

def add_two_ints_client(x, y):
    rospy.wait_for_service('add_two_ints')
    add_two_ints = rospy.ServiceProxy('add_two_ints', addition)
    resp1 = add_two_ints(x, y)
    print(resp1.result)


if __name__ == "__main__":
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    add_two_ints_client(x, y)