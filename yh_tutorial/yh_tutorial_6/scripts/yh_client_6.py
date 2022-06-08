#!/usr/bin/python
# -*- coding: utf8 -*-

import rospy
from yh_tutorial_6.srv import yh_srv_6
import sys

def yh_client(a, b, c):
    rospy.wait_for_service("yh_service_6")
    try:
        service_client = rospy.ServiceProxy("yh_service_6", yh_srv_6)
        res = service_client(a, b, c)
        return res.result
    except rospy.ServiceException as e:
        rospy.logerr(e)

if __name__ == "__main__":
    rospy.init_node("yh_client_6")
    if len(sys.argv) != 4:
        rospy.loginfo("wrong")
        sys.exit(1)
    
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = int(sys.argv[3])
    res = yh_client(a, b, c)
    rospy.loginfo("%d", res)