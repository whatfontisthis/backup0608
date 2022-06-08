#!/usr/bin/python

import rospy
from topic_example.msg import my_msg


def callback(msg):
    print(msg.data)


def listener():
    rospy.Subscriber("topic1", my_msg, callback)
    rospy.init_node("sub_node", anonymous=True)
    rospy.spin()


if __name__ == "__main__":
    listener()
