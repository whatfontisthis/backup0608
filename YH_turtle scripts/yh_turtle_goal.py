#!/usr/bin/python
# -*- coding: utf-8 -*-

import rospy
from geometry_msgs.msg import Twist
#get current position info we subscribe to turtlesim's pose
from turtlesim.msg import Pose
import math

class MyTurtle:
    def __init__(self):
        #publish to our turtle
        self.pub_cmd_vel = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size = 5)
        
        #get position data
        self.sub_pose = rospy.Subscriber("/turtle1/pose", Pose, self.update_pose)
        
        #save position value to variable so we can use 
        self.pose = Pose()
        
        self.loop_rate = rospy.Rate(10)

    def update_pose(self, msg):
        self.pose = msg
        self.pose.x = round(self.pose.x, 4) #round up 4 decimal places
        self.pose.y = round(self.pose.y, 4) #round up 4 decimal places

    def euclidean_distance(self, goal_pose):
        # (x1, y1) -> (x2,y2)
        # (self.pose) -> (goal_pose)
        delta_x = goal_pose.x - self.pose.x
        delta_y = goal_pose.y - self.pose.y
        #return the euclidean distance
        return math.sqrt(delta_x**2 + delta_y**2)

    #LINEAR VELOCITY
    #'constant=1.5' means it will take on value of 1.5 if no value is given
    def linear_vel(self, goal_pose, constant=10):  # higher constant = faster turtle
        #y = ax + b  slows down
        # to make the slowing smoother, look up PID controller
        return constant * self.euclidean_distance(goal_pose)

    # tan theta = oppisite / adjacent
    def steering_angle(self, goal_pose):
        return math.atan2((goal_pose.y - self.pose.y) , (goal_pose.x - self.pose.x))

    #ANGULAR VELOCITY
    def angular_vel(self, goal_pose, constant=10): #constant is slope, bigger value will turn faster (smaller turn angle)
        #0 angle is angle is in reference to east
        return constant * (self.steering_angle(goal_pose) - self.pose.theta)

    def move2goal(self):
        goal_pose = Pose()
        
        goal_pose.x = float(input("Enter x coordinate: "))
        goal_pose.y = float(input("Enter y coordinate: "))
        
        tolerance = float(input("Margin of error: "))

        msg = Twist()

        #loop untill distance is bigger than tolerance
        while self.euclidean_distance(goal_pose) >= tolerance:
            msg.linear.x = self.linear_vel(goal_pose)
            msg.angular.z = self.angular_vel(goal_pose)

            #publish
            self.pub_cmd_vel.publish(msg)
            self.loop_rate.sleep()

        #when you we quit loop, means we've arrived at goal_pose. so velocity becomes 0.
        msg.linear.x = 0
        msg.angular.z = 0
        self.pub_cmd_vel.publish(msg)

        print("You've arrived at the goal.")

if __name__ == "__main__":
    rospy.init_node("yh_turtle_goal")
    try:
        my_turtle = MyTurtle() #my turtle instance is created
        my_turtle.move2goal() #move to goal
    except rospy.ROSInterruptException:
        pass
