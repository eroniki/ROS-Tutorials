// include ROS headers to be able to use ROS classes
#include <ros/ros.h>
// include geometry_msgs/Twist.h to use geometry_msgs::Twist
#include <geometry_msgs/Twist.h>

// The callback function that ROS runs when data transmission finishes
void messageRecieved(const geometry_msgs::Twist& message){
    // log message to the console
    ROS_INFO_STREAM("The message I got:"
    <<" linear= "<<message.linear.x
    <<" angular= "<<message.angular.z);
}

int main(int argc, char** argv){
    // init ROS
    ros::init(argc, argv, "subscriber_geometry_msgs");
    // Establish this program as a ROS node
    ros::NodeHandle nh;
    // Create subscriber object with following options: topic="/turtle1/cmd_vel", queue size= 1000 and callback function= messageRecieved
    ros::Subscriber subsriber= nh.subscribe("/turtle1/cmd_vel", 1000, &messageRecieved);
    // Give ROS explicit permission the call callback function
    ros::spin();
    return 0;
}
