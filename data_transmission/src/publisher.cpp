// include ROS headers to be able to use ROS classes
#include <ros/ros.h>
// include geometry_msgs/Twist.h to use geometry_msgs::Twist
#include <geometry_msgs/Twist.h>
// include stdlib to use rand() and RAND_MAX
#include <stdlib.h>

int main(int argc, char** argv){
    // init ROS
    ros::init(argc, argv, "publisher_geometry_msgs");
    // establish this program as a ROS node
    ros::NodeHandle nh;
    // create publisher object with following options: message type= geometry_msgs::Twist, topic="/turtle1/cmd_vel" and queue size= 1000
    ros::Publisher publisher= nh.advertise<geometry_msgs::Twist>("turtle1/cmd_vel",1000);
    // seed the srand()
    srand(time(0));
    // set loop rate to 2Hz until the node is shut down
    ros::Rate rate(2);
    // create message
    geometry_msgs::Twist message;
    // infinite loop until ROS says stop
    while(ros::ok()){
        // create the values that will be transmitted to another nodes
        message.linear.x= double(rand())/double(RAND_MAX);
        message.angular.z= double(rand())/double(RAND_MAX)-1;
        // publish it
        publisher.publish(message);
        // dump the same message to the console
        ROS_INFO_STREAM("The message contains random velocity command"
        <<" linear= "<<message.linear.x
        <<" angular= "<<message.angular.z);
        // wait until 0.5 second (2Hz) passes
        rate.sleep();
    }
    return 0;
}
