#!/usr/bin/python
# -*- coding: utf8 -*-

from logging.config import listen
import rospy
from yh_tutorial_1.msg import yh_msg_1

def msgCallback(msg):
    rospy.loginfo("%d", msg.data)

def listener():
    rospy.init_node("yh_sub_1", anonymous=True)
    rospy.Subscriber("yh_topic_1", yh_msg_1, msgCallback)

    rospy.spin()

if __name__ == "__main__":
    listener()