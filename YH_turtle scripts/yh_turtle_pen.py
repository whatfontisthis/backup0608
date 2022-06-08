#!/usr/bin/python
# -*- coding: utf-8 -*-

import rospy
from turtlesim.srv import SetPen


class TurtlePen:
    
    def __init__(self):
     
        #make client (user) 
        #arguments (service name, service type) must match for service communication
        #c.f. in topic communication, topic name and message type must match
        self.client_pen = rospy.ServiceProxy("turtle1/set_pen", SetPen)


    def run(self):
        r = int(input("Enter r value: "))
        g = int(input("Enter g value: "))
        b = int(input("Enter b value: "))
        width = int(input("Enter width value: "))
        off = int(input("Enter off value: "))
        self.client_pen(r,g,b, width, off)

if __name__ == "__main__":
    rospy.init_node("yh_turtle_pen")
    turtle_pen = TurtlePen()
    while not rospy.is_shutdown(): #add while to keep accepting values
        turtle_pen.run()
