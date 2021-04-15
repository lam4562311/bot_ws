#! /usr/bin/python

import math
import numpy as np
import rospy

from geometry_msgs.msg import Twist
from std_msgs.msg import String
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import Int32MultiArray
from sensor_msgs.msg import Joy

pubtw = None

reverse_fac = 1.0
speeding_fac = 1.0

def callback(data):
    global reverse_fac
    global speeding_fac
    
    bt = Int32MultiArray()
    bt.data = data.buttons

    keypad = Int32MultiArray()
    for index in range(0,4):
        keypad.data.append(bt.data[index]) # square, cross, circle, triangle, 0-3
    
    if bt.data[8] == 1:
        reverse_fac *= -1.0

    if bt.data[6] == 1 and speeding_fac == 1:
        speeding_fac = 1.5
    elif bt.data[7] == 1 and speeding_fac == 1:
        speeding_fac = 0.8
    else:
        speeding_fac = 1.0

    ax1 = np.round(20.0 * speeding_fac * reverse_fac * data.axes[0], 2)
    ax2 = np.round(20.0 * speeding_fac * reverse_fac * data.axes[1], 2)
    ax3 = np.round(20.0 * speeding_fac * reverse_fac * data.axes[2], 2)

    print("[INFO] data.axes[0]: {}".format(data.axes[0]))
    print("[INFO] data.axes[1]: {}".format(data.axes[1]))
    print("[INFO] data.axes[2]: {}".format(data.axes[2]))
    print("")
    print("[INFO] ax1: {}". format(ax1))
    print("[INFO] ax2: {}".format(ax2))
    print("[INFO] ax3: {}".format(ax3))
    print("=" * 50)
	
    twist = Twist()
    twist.linear.x = ax2
    twist.linear.y = ax1
    twist.angular.z = ax3
	
    pubtw.publish(twist)
    pubbt.publish(keypad)
# Intializes everything
def start():
    # publishing to "moving_base" and "fcn_button" to control mbed
    global pubax
    global pubbt
    global pubtw	#add a twist channel to test
    # starts the node
    rospy.init_node('Joy2mbed')
    rate = rospy.Rate(10)
    pubtw = rospy.Publisher("base_twist", 
                            Twist, 
                            tcp_nodelay = True, 
                            queue_size = 1)
    pubbt = rospy.Publisher("fcn_button",
			    Int32MultiArray,
			    tcp_nodelay = True, 
                            queue_size = 1)
    rospy.Subscriber("joy", 
                     Joy, 
                     callback, 
                     tcp_nodelay = True, 
                     queue_size = 1)
    rospy.spin()

if __name__ == '__main__':
    print("[INFO] Start reading PS4 controller...")

    try:
        start()
    except rospy.ROSInterruptException:
        pass
