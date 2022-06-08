#include "ros/ros.h"
#include "yh_tutorial_6/yh_srv_6.h"
#include <cstdlib>

int main(int argc, char ** argv)
{
    ros::init(argc, argv, "yh_client_6");

    if (argc != 4)
    {
        ROS_INFO("wrong command");
        return 1;
    }

    ros::NodeHandle nh;

    ros::ServiceClient service_client = nh.serviceClient<yh_tutorial_6::yh_srv_6>("yh_service_6");

    yh_tutorial_6::yh_srv_6 srv;

    srv.request.a = atoll(argv[1]);
    srv.request.b = atoll(argv[2]);
    srv.request.c = atoll(argv[3]);

    if (service_client.call(srv))
    {
        ROS_INFO("%ld", srv.response.result);
    }
    else
    {
        ROS_ERROR("Failed");
        return 1;
    }

    return 0;
}