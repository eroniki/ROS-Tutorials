/*
 * publisher.cpp
 *
 *  Created on: Sep 16, 2015
 *      Author: murat
 */
#include "ros/ros.h"
#include "std_msgs/String.h"
#include <iostream>
#include <sstream>
#include <string>
#include <stdio.h>
#include <time.h>

const std::string currentDateTime(){
    time_t     now = time(0);
    struct tm  tstruct;
    char       buf[80];
    tstruct = *localtime(&now);
    strftime(buf, sizeof(buf), "%Y-%m-%d.%X", &tstruct);
    return buf;
}

int main(int argc, char** argv){
	ros::init(argc, argv, "timedPublisher");
    ros::NodeHandle nh;
    ros::Rate rate(1);
    std_msgs::String msg;
    ros::Publisher chatter_pub = nh.advertise<std_msgs::String>("chatter", 1000);
	while (ros::ok()){
		std::stringstream stringStream;
		stringStream << "currentDateTime()=" << currentDateTime();
		msg.data = stringStream.str();
		ROS_INFO_STREAM(stringStream.str());
		chatter_pub.publish(msg);
		ros::spinOnce(); // Allow ROS to process incoming messages
		rate.sleep(); // Sleep for the rest of the cycle
	}
	return 0;
}


