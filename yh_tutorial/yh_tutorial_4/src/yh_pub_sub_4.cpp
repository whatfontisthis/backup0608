#include "ros/ros.h"
#include "yh_tutorial_4/yh_msg_4.h"

ros::Publisher pub;

void msgCallback(const yh_tutorial_4::yh_msg_4::ConstPtr &msg)
{
    if (msg->data % 5 == 0)
    {
        pub.publish(msg);
    }
}

int main(int argc, char** argv)
{
    ros::init(argc, argv, "yh_pub_sub_4");
    ros::NodeHandle nh;

    pub = nh.advertise<yh_tutorial_4::yh_msg_4>("raspberry_pie", 100);
    ros::Subscriber sub = nh.subscribe("yh_topic_4", 100, msgCallback);

    ros::spin();

    return 0;
}