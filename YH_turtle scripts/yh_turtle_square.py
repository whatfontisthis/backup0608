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

#to inherit from turtle_triangle class
#argument(python file name, class we want to inherit)
from yh_turtle_triangle import TurtleTriangle

#inheriting class by adding into argument the class to be imported
class TurtleSquare(TurtleTriangle): #means we will inherit TurtleTriangle
    
    #__init__ don't need change becuase we can use all the same values so we leave it empty

    #functions with same spelling will overwrite the original class
    #  writing new def will be added as new function
    def run(self): 
        self.client_teleport(5.544445 - self.length / 2, 5.544445 - self.length/2, 0)
        self.client_clear()

        loop_rate = rospy.Rate(1 * 20)
        msg = Twist()

        cnt = 0

        #will loop untill connections are made and 
        while self.pub.get_num_connections() < 1:  #pub.get returns how many topics are connected
            continue

        while not rospy.is_shutdown():
            msg.linear.x = self.length * 20
            msg.angular.z = 0
            self.pub.publish(msg)
            loop_rate.sleep()

            msg.linear.x = 0
            msg.angular.z = math.pi/2 * 20
            self.pub.publish(msg)
            loop_rate.sleep()

            # cnt +=1
            # if cnt ==4:
            #     self.client_clear() #clear screen
            #     cnt = 0


if __name__ == "__main__":

    rospy.init_node("yh_turtle_square")
    
    #get length input from user
    try:
        length = float(input("Enter length: "))
        turtle_triangle = TurtleSquare(length)
        turtle_triangle.run()
    except:
        pass
    
    
