/*
 * subscriber.cpp
 *
 *  Created on: Sep 16, 2015
 *      Author: murat
 */

#include <ros/ros.h>
#include "std_msgs/String.h"
#include <iostream>
#include <sstream>
#include <string>
#include <stdio.h>
#include <time.h>

void chatterCallback(const std_msgs::String::ConstPtr& msg){
	ROS_INFO_STREAM("I heard: " << msg->data);
}

int main(int argc, char** argv){
	ros::init(argc, argv, "timedSubscriber");
    ros::NodeHandle nh;
    ros::Subscriber sub = nh.subscribe("chatter", 1000, chatterCallback);

    ros::spin();
	return 0;
}



