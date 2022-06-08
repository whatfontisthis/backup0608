#!/usr/bin/python
# -*- coding: utf-8 -*-

import rospy
#from geometry bring just twist
from geometry_msgs.msg import Twist
#from service only bring teleport 
from turtlesim.srv import TeleportAbsolute
#from standard service just bring empty
from std_srvs.srv import Empty
import math
#to receive inpuut from user
import sys

class TurtleTriangle:
    def __init__(self, length):
        self.pub = rospy.Publisher("turtle1/cmd_vel", Twist, queue_size = 10)
        self.client_teleport = rospy.ServiceProxy("turtle1/teleport_absolute", TeleportAbsolute)
        self.client_clear = rospy.ServiceProxy("/clear", Empty)
        self.length = length

    def run(self):
        #teleport argu: (x,y,theta)
        self.client_teleport(5.544445 - self.length/2 , 5.544445 - (math.sqrt(3)) / 4 * self.length, 0)
        #doesn't take argument becuase is empty
        self.client_clear()
        
        #make loop 1 second
        loop_rate = rospy.Rate(1)
        msg = Twist()

        cnt = 0

        #will loop untill connections are made and 
        while self.pub.get_num_connections() < 1:  #pub.get() returns how many topics are connected
            continue

        #what to do each loop
        while not rospy.is_shutdown():
            #go forward
            msg.linear.x = self.length
            msg.angular.z = 0
            self.pub.publish(msg)
            loop_rate.sleep() #sleep one second

            #turn 
            msg.linear.x = 0
            msg.angular.z = math.pi * 2/3 #because it turns CCW
            self.pub.publish(msg)
            loop_rate.sleep() #sleep one second

            cnt +=1
            if cnt ==3:
                self.client_clear() #clear screen
                cnt = 0

if __name__ == "__main__":

    rospy.init_node("yh_turtle_triangle")
    if len(sys.argv) != 2:
        print("arg error")
        sys.exit(1)
    
    #takes input from the user with argv
    turtle_triangle = TurtleTriangle(float(sys.argv[1]))
    turtle_triangle.run()
    
