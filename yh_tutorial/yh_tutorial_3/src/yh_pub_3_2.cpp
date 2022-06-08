#include "ros/ros.h"
#include "yh_tutorial_3/yh_msg_3.h"

int main(int argc, char ** argv)
{
    ros::init(argc, argv, "yh_pub_3_2");
    ros::NodeHandle nh;
    
    ros::Publisher pub = nh.advertise<yh_tutorial_3::yh_msg_3>("yh_topic_3", 100);
    ros::Rate loop_rate(5);
    int cnt = 0;
    yh_tutorial_3::yh_msg_3 msg;

    while (ros::ok())
    {
        msg.stamp = ros::Time::now();
        msg.data = cnt;
        cnt += 2;
        pub.publish(msg);
        loop_rate.sleep();
    }

    return 0;
}