#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

uav1 = rospy.Publisher('/uav1/cmd_vel', Twist, queue_size=10)
uav2 = rospy.Publisher('/uav2/cmd_vel', Twist, queue_size=10)
uav3 = rospy.Publisher('/uav3/cmd_vel', Twist, queue_size=10)
uav4 = rospy.Publisher('/uav4/cmd_vel', Twist, queue_size=10)
uav5 = rospy.Publisher('/uav5/cmd_vel', Twist, queue_size=10)
uav6 = rospy.Publisher('/uav6/cmd_vel', Twist, queue_size=10)
uav7 = rospy.Publisher('/uav7/cmd_vel', Twist, queue_size=10)
uav8 = rospy.Publisher('/uav8/cmd_vel', Twist, queue_size=10)

def callback(data):
    rospy.loginfo(data.linear)
    rospy.loginfo(data.angular)
    rospy.loginfo("~~~~~~~~~~~~~~~~~~~")
    massPublish(data)

def massPublish(data):
    uav1.publish(data)
    uav2.publish(data)
    uav3.publish(data)
    uav4.publish(data)
    uav5.publish(data)
    uav6.publish(data)
    uav7.publish(data)
    uav8.publish(data)

def demux():
    rospy.init_node('topic_demux', anonymous=True)
    rospy.Subscriber("/turtle1/cmd_vel", Twist, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        demux()
    except rospy.ROSInterruptException:
        pass
