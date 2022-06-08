#!/usr/bin/python
# -*- coding: utf8 -*-

import rospy
from yh_tutorial_2.msg import yh_msg_2

def msgCallback(msg):
    if msg.data % 2 == 1:
        rospy.loginfo("%d", msg.data)

def listener():
    rospy.init_node("yh_sub_2_int", anonymous=True)
    rospy.Subscriber("yh_topic_2", yh_msg_2, msgCallback)
    rospy.spin()

if __name__ == "__main__":
    listener()