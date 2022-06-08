#include "ros/ros.h"
#include "yh_tutorial_6/yh_srv_6.h"

bool srvCallback(yh_tutorial_6::yh_srv_6::Request &req, yh_tutorial_6::yh_srv_6::Response &res)
{
    res.result = req.a + req.b + req.c;

    return true;
}

int main(int argc, char **argv)
{
    ros::init(argc, argv, "yh_server_6");
    ros::NodeHandle nh;

    ros::ServiceServer service_server = nh.advertiseService("yh_service_6", srvCallback);

    ROS_INFO("Service server ready.");

    ros::spin();

    return 0;
}


