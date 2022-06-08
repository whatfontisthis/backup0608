#include "ros/ros.h"
#include "yh_tutorial_1/yh_msg_1.h"

int main(int argc, char ** argv)
{
    ros::init(argc, argv, "yh_pub_1");
    ros::NodeHandle nh;

    ros::Publisher pub = nh.advertise<yh_tutorial_1::yh_msg_1>("yh_topic_1", 100);
    ros::Rate loop_rate(2);
    int cnt = 0;
    yh_tutorial_1::yh_msg_1 msg;
    while (ros::ok())
    {
        msg.stamp = ros::Time::now();
        msg.data = cnt;
        cnt++;
        pub.publish(msg);
        loop_rate.sleep();
    }

    return 0;
}