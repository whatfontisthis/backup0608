#!/usr/bin/python
# -*- coding: utf8 -*-
import rospy
from yh_tutorial_1.msg import yh_msg_1

def talker():
    pub = rospy.Publisher("yh_topic_1", yh_msg_1, queue_size=100)
    rospy.init_node("yh_pub_1", anonymous=True)
    loop_rate = rospy.Rate(2)
    cnt = 0
    msg = yh_msg_1()
    while not rospy.is_shutdown():
        msg.stamp = rospy.Time.now()
        msg.data = cnt
        pub.publish(msg)
        cnt += 1
        loop_rate.sleep()

if __name__ == "__main__":
    try:
        talker()
    except rospy.ROSInterruptException:
        pass