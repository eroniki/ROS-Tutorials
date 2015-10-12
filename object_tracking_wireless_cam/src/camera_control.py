#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32MultiArray
from geometry_msgs.msg import Twist
import urllib2
import time 
import cv2

def control_motors(x,y):
	if(x<0):
		urlExecution(6)
		print("Right")
	elif(x>0):
		urlExecution(4)
		print("Left")
	if(y>0):
		urlExecution(0)
		print("Up")
	elif(y<0):
		urlExecution(2)
		print("Down")

def urlExecution(command):
	ip = 'http://192.168.1.38:81/decoder_control.cgi?loginuse=admin&loginpas=12345&command='
	oneStep = '&onestep=1&'
	gibberish = '7485621407675288&_='
	timeStamp = int(time.time())*1000
	fullURL = ip+str(command)+oneStep+str(timeStamp)+'.49641236611690986&_='+str(timeStamp)
	response = urllib2.urlopen(fullURL)
	rospy.loginfo(fullURL)

def callback(data):
	rospy.loginfo('~~~~~~~~~~~~~~~~~~')
	rospy.loginfo('Linear: ')
	rospy.loginfo(data.linear.x)
	rospy.loginfo('~~~~~~~~~~~~~~~~~~')
	rospy.loginfo('Angular: ')
	rospy.loginfo(data.angular.z)
	control_motors(data.angular.z, data.linear.x);

    
def listener():
    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('camera_control', anonymous=True)

    rospy.Subscriber("/turtle1/cmd_vel", Twist, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
