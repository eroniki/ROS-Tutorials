#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Joy
import urllib2
import time 
import cv2

def control_motors(vertical, horizontal):
	if(horizontal>0):
		urlExecution(4)
		time.sleep(0.1)
		urlExecution(5)
	elif(horizontal<0):
		urlExecution(6)
		time.sleep(0.1)
		urlExecution(7)
	if(vertical>0):
		urlExecution(0)
		time.sleep(0.1)
		urlExecution(1)
	elif(vertical<0):
		urlExecution(2)
		time.sleep(0.1)
		urlExecution(3)

def urlExecution(command):
	ip = 'http://192.168.1.76:81/decoder_control.cgi?loginuse=admin&loginpas=12345&command='
	oneStep = '&onestep=1&'
	gibberish = '7485621407675288&_='
	timeStamp = int(time.time())*1000
	fullURL = ip+str(command)+oneStep+str(timeStamp)+'.49641236611690986&_='+str(timeStamp)
	response = urllib2.urlopen(fullURL)
	rospy.loginfo(fullURL)

def callback(data):
	rospy.loginfo(data)
	rospy.loginfo('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
	horizontal = data.axes[4]
	vertical = data.axes[5]
	control_motors(vertical,horizontal)
		
#	rospy.loginfo('X: ' + str(data.data[9]))
#	rospy.loginfo('Y: ' + str(data.data[10]))
#	control_motors(error_x,error_y);

    
def listener():
    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('object_tracking', anonymous=True)

    rospy.Subscriber("/joy", Joy, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
