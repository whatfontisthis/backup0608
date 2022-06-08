#!/usr/bin/python
# -*- coding: utf8 -*-

import rospy
from yh_tutorial_6.srv import yh_srv_6, yh_srv_6Response

def srvCallback(req):
    return yh_srv_6Response(req.a + req.b + req.c)

def yh_server():
    rospy.init_node("yh_server_6")
    service_server = rospy.Service("yh_service_6", yh_srv_6, srvCallback)
    rospy.spin()

if __name__ == "__main__":
    yh_server()