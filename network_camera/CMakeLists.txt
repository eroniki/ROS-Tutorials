cmake_minimum_required(VERSION 2.8.3)
project(network_camera)

## Find catkin macros and libraries
find_package(catkin REQUIRED COMPONENTS roscpp rospy std_msgs image_transport cv_bridge)
find_package(OpenCV)

## Declare catkin package
catkin_package()

## Specify additional locations of header files
include_directories(${catkin_INCLUDE_DIRS})
include_directories(${OpenCV_INCLUDE_DIRS})

## Declare a cpp executable
add_executable(network_streamer src/network_streamer.cpp)

## Specify libraries to link a library or executable target against
target_link_libraries(network_streamer ${catkin_LIBRARIES})
target_link_libraries(network_streamer ${OpenCV_LIBRARIES})