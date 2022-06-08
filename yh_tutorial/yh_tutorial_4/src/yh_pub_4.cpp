#include "ros/ros.h"
#include "yh_tutorial_4/yh_msg_4.h"

int main(int argc, char ** argv)
{
    ros::init(argc, argv, "yh_pub_4");
    ros::NodeHandle nh;
    
    ros::Publisher pub = nh.advertise<yh_tutorial_4::yh_msg_4>("yh_topic_4", 100);
    ros::Rate loop_rate(10);
    int cnt = 0;
    yh_tutorial_4::yh_msg_4 msg;

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