// include ROS headers to reach and use ROS classes
#include <ros/ros.h>

int main(int argc, char** argv){
    // init ROS with a node name "hello_world"
    ros::init(argc,argv, "hello_world");
    // Establish this program as ROS node
    ros::NodeHandle nh;
    // Keep saying "hello" until ROS says stop
    while(ros::ok()){
        // Log the famous quote of Dennis Ritchie's
        ROS_INFO_STREAM("Hello world, this is my first ROS Package");
    }
    return 0;
}
