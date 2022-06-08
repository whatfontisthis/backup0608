#!/usr/bin/python
# -*- coding: utf8 -*-

import rospy
from yh_tutorial_7.srv import yh_srv_7
import sys


def yh_client(a, b):
    rospy.wait_for_service("yh_service_7")
    try:
        service_client = rospy.ServiceProxy("yh_service_7", yh_srv_7)
        res = service_client(a, b)
        return res.result
    except rospy.ServiceException as e:
        rospy.logerr(e)


if __name__ == "__main__":
    rospy.init_node("yh_client_7")
    if len(sys.argv) != 3:
        rospy.loginfo("wrong")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[2])
    res = yh_client(a, b)
    rospy.loginfo("%d", res)
