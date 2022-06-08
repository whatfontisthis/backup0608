#!/usr/bin/python
# -*- coding: utf-8 -*-

import rospy
from geometry_msgs.msg import Twist
#SetPen is service, we only bring request part of the svc(above ---)
#in python, client will only use request
from turtlesim.srv import SetPen, SetPenRequest

class MyTurtle:
    def __init__(self):
        #receive from
        self.sub = rospy.Subscriber("cmd_vel", Twist, self.msgCallback)
        #send to
        self.pub = rospy.Publisher("turtle1/cmd_vel", Twist, queue_size = 1)

        #service name turtle/set_pen
        #service type = turtlesim/SetPen
        self.client_pen = rospy.ServiceProxy("turtle1/set_pen", SetPen, )
        self.pen = SetPenRequest() # so we can use the request
        self.pen.width = 3 #initialize value

    def msgCallback(self, msg):
        if msg.linear.z > 0:
            #change color
            self.pen.r = int(input("R Value: "))
            self.pen.g = int(input("G Value: "))
            self.pen.b = int(input("B Value: "))
            #get the color
            self.client_pen(self.pen)
            
        elif msg.linear.z < 0:
            #change width
            self.pen.width = int(input("Width Value: "))
            #get the widdth
            self.client_pen(self.pen)

        else:
            self.pub.publish(msg)
            #publish only when 

if __name__ == "__main__":
    rospy.init_node("yh_turtle_keyboard_pen")
    my_turtle = MyTurtle()
    rospy.spin()