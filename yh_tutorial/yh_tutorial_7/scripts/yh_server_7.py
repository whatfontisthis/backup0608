#!/usr/bin/python
# -*- coding: utf8 -*-

import rospy
from yh_tutorial_7.srv import yh_srv_7, yh_srv_7Response


def srvCallback(req):
    if req.a > req.b:
        return yh_srv_7Response(req.a - req.b)
    else:
        return yh_srv_7Response(req.b - req.a)


def yh_server():
    rospy.init_node("yh_server_7")
    service_server = rospy.Service("yh_service_7", yh_srv_7, srvCallback)
    rospy.spin()


if __name__ == "__main__":
    yh_server()
