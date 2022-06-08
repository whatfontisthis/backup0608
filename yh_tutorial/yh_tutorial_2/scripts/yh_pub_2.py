#!/usr/bin/python
# -*- coding: utf8 -*-

import rospy
from yh_tutorial_2.msg import yh_msg_2

def talker():
    pub = rospy.Publisher("yh_topic_2", yh_msg_2, queue_size=100)
    rospy.init_node("yh_pub_2", anonymous=True)

    loop_rate = rospy.Rate(5)
    msg = yh_msg_2()
    cnt = 0

    while not rospy.is_shutdown():
        msg.stamp = rospy.get_rostime()
        msg.data = cnt
        pub.publish(msg)
        cnt += 1
        loop_rate.sleep()
    
if __name__ == "__main__":
    try:
        talker()
    except rospy.ROSInterruptException:
        pass