#include "ros/ros.h"
#include "yh_tutorial_2/yh_msg_2.h"

int main(int argc, char **argv)
{
    ros::init(argc, argv, "yh_pub_2");
    ros::NodeHandle nh;

    ros::Rate loop_rate(5);
    int cnt = 0;

    ros::Publisher pub = nh.advertise<yh_tutorial_2::yh_msg_2>("yh_topic_2", 100);
    yh_tutorial_2::yh_msg_2 msg;

    while (ros::ok())
    {
        msg.stamp = ros::Time::now();
        msg.data = cnt;
        pub.publish(msg);
        cnt++;
        loop_rate.sleep();
    }

    return 0;
}