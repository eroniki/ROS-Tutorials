// include ROS headers to be able to use ROS classes
#include <ros/ros.h>
// to be able to use rand()
#include <stdlib.h>

int main(int argc, char** argv){
    int number;
    // initialize ROS
    ros::init(argc, argv, "log_messages");
    // establish the app as a node
    ros::NodeHandle nh;
    // shuffle the cards
    srand(time(0));
    // create log messages on timely basis (10 Hz), 10 numbers in a second
    ros::Rate rate(10);
    while(ros::ok()){
        number= rand()%100;
        ROS_DEBUG_STREAM("The lucky number: "<<number);
        if(number%3==0){
            ROS_INFO_STREAM("The number is divisible by 3. The node is going on creating numbers.");
        }
        else if(number%4==0){
            ROS_WARN_STREAM("The number is divisible by 4. The node is going on creating numbers.");
        }
        else if(number%5==0){
            ROS_ERROR_STREAM("The number is divisible by 5. The node is going on creating numbers.");
        }
        else{
            ROS_ERROR_STREAM("Possibility of being a prime number. The node is being stopped.");
            break;
        }
        rate.sleep();
    }

    return 0;
}
