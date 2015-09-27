cmake_minimum_required(VERSION 2.8.3)
project(lesson_3_89685)

## Find catkin macros and libraries
find_package(catkin REQUIRED COMPONENTS roscpp rospy std_msgs)

## Declare ROS messages and services
# add_message_files(FILES Message1.msg Message2.msg)
# add_service_files(FILES Service1.srv Service2.srv)

## Generate added messages and services 
# generate_messages(DEPENDENCIES std_msgs)

## Declare catkin package
catkin_package()

## Specify additional locations of header files
include_directories(${catkin_INCLUDE_DIRS})

## Declare a cpp executable
add_executable(moveTurtle src/moveTurtle.cpp)

## Specify libraries to link a library or executable target against
target_link_libraries(moveTurtle ${catkin_LIBRARIES})
