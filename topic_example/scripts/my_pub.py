#!/usr/bin/python

import rospy
from topic_example.msg import my_msg


def talker():
    pub = rospy.Publisher("topic1", my_msg, queue_size=1)
    rospy.init_node("pub_node", anonymous=True)

    msg = my_msg()
    loop_rate = rospy.Rate(5)
    cnt = 0

    while not rospy.is_shutdown():
        msg.data = cnt
        pub.publish(msg)
        print(msg.data)
        cnt += 1
        loop_rate.sleep()


if __name__ == "__main__":
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
