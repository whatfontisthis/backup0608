#include "ros/ros.h"
#include "yh_tutorial_7/yh_srv_7.h"

bool srvCallback(yh_tutorial_7::yh_srv_7::Request &req, yh_tutorial_7::yh_srv_7::Response &res)
{
    if (req.a > req.b)
    {
        res.result = req.a - req.b;
    }
    else
    {
        res.result = req.b - req.a;
    }

    return true;
}

int main(int argc, char **argv)
{
    ros::init(argc, argv, "yh_server_7");
    ros::NodeHandle nh;

    ros::ServiceServer service_server = nh.advertiseService("yh_service_7", srvCallback);

    ROS_INFO("Service server ready.");

    ros::spin();

    return 0;
}


