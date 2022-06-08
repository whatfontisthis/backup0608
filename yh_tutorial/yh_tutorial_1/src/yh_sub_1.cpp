#include "ros/ros.h"
#include "yh_tutorial_1/yh_msg_1.h"

void msgCallback(const yh_tutorial_1::yh_msg_1::ConstPtr& msg)
{
    ROS_INFO("%d", msg->data);
}

int main(int argc, char ** argv)
{
    ros::init(argc, argv, "yh_sub_1");
    ros::NodeHandle nh;

    ros::Subscriber sub = nh.subscribe("yh_topic_1", 100, msgCallback);

    ros::spin();

    return 0;
}