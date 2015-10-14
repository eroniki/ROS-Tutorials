#!/usr/bin/python
import sys, time, urllib2
from PyQt4 import QtCore, QtGui, uic
import rospy
from sensor_msgs.msg import Joy

def urlExecution(command):
    ip = 'http://192.168.1.76:81/decoder_control.cgi?loginuse=admin&loginpas=12345&command='
    oneStep = '&onestep=1&'
    gibberish = '7485621407675288&_='
    timeStamp = int(time.time())*1000
    fullURL = ip+str(command)+oneStep+str(timeStamp)+'.49641236611690986&_='+str(timeStamp)
    response = urllib2.urlopen(fullURL)
    #rospy.loginfo(fullURL)

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

def callback(data):
    if myWindow.radJoy.isChecked():
        #rospy.loginfo('~~~~~~~~~~~~~~~~~~')
        #rospy.loginfo(data)
    	horizontal = data.axes[4]
    	vertical = data.axes[5]
    	control_motors(vertical,horizontal)

form_class = uic.loadUiType("mainwindow.ui")[0]                 # Load the UI

class MainWindow(QtGui.QMainWindow, form_class):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.pushUp.clicked.connect(self.upCallback)  # Bind the event handlers
        self.pushDown.clicked.connect(self.downCallback)  #   to the buttons
        self.pushLeft.clicked.connect(self.leftCallback)
        self.pushRight.clicked.connect(self.rightCallback)
        rospy.init_node('camera_ui', anonymous=True)
        rospy.Subscriber("/joy", Joy, callback)

    def upCallback(self):
        if myWindow.radUI.isChecked():
            urlExecution(0)
            time.sleep(0.1)
            urlExecution(1)

    def downCallback(self):
        if myWindow.radUI.isChecked():
            urlExecution(2)
            time.sleep(0.1)
            urlExecution(3)

    def leftCallback(self):
        if myWindow.radUI.isChecked():
            urlExecution(4)
            time.sleep(0.1)
            urlExecution(5)

    def rightCallback(self):
        if myWindow.radUI.isChecked():
            urlExecution(6)
            time.sleep(0.1)
            urlExecution(7)


app = QtGui.QApplication(sys.argv)
myWindow = MainWindow(None)
myWindow.show()
app.exec_()
