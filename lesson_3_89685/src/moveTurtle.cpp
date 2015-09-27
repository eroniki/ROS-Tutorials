/*
 * moveTurtle.cpp
 *
 *  Created on: Sep 16, 2015
 *      Author: murat
 */

#include "ros/ros.h"
#include "std_msgs/String.h"
#include "geometry_msgs/Twist.h"
#include <iostream>
#include <sstream>
#include <string>
#include <stdio.h>
#include <time.h>

int main(int argc, char** argv){
	ros::init(argc, argv, "moveTurtle");
    ros::NodeHandle nh;
    ros::Rate rate(1);
    geometry_msgs::Twist msg;
    ros::Publisher chatter_pub = nh.advertise<geometry_msgs::Twist>("/turtle1/cmd_vel", 1000);
	msg.linear.x = 1;
	chatter_pub.publish(msg);
	return 0;
}
