#!/usr/bin/python
# -*- coding: utf-8 -*-

import rospy
from geometry_msgs.msg import Twist

# makes global publisher
pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=1) 
        
def msgCallback(msg):
    pub.publish(msg) # publish message to pub

def listener():
    rospy.init_node("yh_turtle_keyboard") # initiate node
    sub = rospy.Subscriber("/cmd_vel", Twist, msgCallback) # subscribe to cmd_vel
    rospy.spin()

if __name__ == "__main__":
    listener()
