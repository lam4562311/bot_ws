#! /usr/bin/python

import math
import numpy as np
import rospy

from geometry_msgs.msg import Twist
from std_msgs.msg import String
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import Int32MultiArray
from std_msgs.msg import Bool
from sensor_msgs.msg import Joy

pubtw = None
pubbt = None
pubsqu = None
pubcro = None
pubcir = None
pubtri = None
pubL1 = None
pubR1 = None

reverse_fac = 1.0
speeding_fac = 1.0

def callback(data):
    global reverse_fac
    global speeding_fac
    
    bt = Int32MultiArray()
    bt.data = data.buttons

    keypad = Int32MultiArray()
    for index in range(0,4):
        keypad.data.append(bt.data[index]) # square, cross, circle, triangle, 0-3;
	                                   # L1, R1, 4-5
    squ = Bool()
    cro = Bool()
    cir = Bool()
    tri = Bool()
    L1 = Bool()
    R1 = Bool()

    squ.data = False
    cro.data = False
    cir.data = False
    tri.data = False
    L1.data = False
    R2.data = False

    if bt.data[0]==1:
        squ.data = True
    else:
        squ.data = False
    if bt.data[1]==1:
        cro.data = True
    else:
        cro.data = False
    if bt.data[2]==1:
        cir.data = True
    else:
        cir.data = False
    if bt.data[3]==1:
        tri.data = True
    else:
        tri.data = False
	
    if bt.data[4] == 1:
	L1.data = True
    else:
	L1.data = False
    if bt.data[5] == 1:
	R1.data = True
    else:
	R1.data = Fales

    if bt.data[8] == 1:
        reverse_fac *= -1.0 #share

    if bt.data[6] == 1 and speeding_fac == 1:
        speeding_fac = 1.5 #L2
    elif bt.data[7] == 1 and speeding_fac == 1:
        speeding_fac = 0.5  #R2
    else:
        speeding_fac = 1.0

    ax1 = np.round(20.0 * speeding_fac * reverse_fac * data.axes[0], 2)
    ax2 = np.round(20.0 * speeding_fac * reverse_fac * data.axes[1], 2)
    ax3 = np.round(20.0 * speeding_fac * reverse_fac * data.axes[2], 2)

    axKL = data.axes[6]
    axKU = data.axes[7]
    # print("[INFO] data.axes[0]: {}".format(data.axes[0]))
    # print("[INFO] data.axes[1]: {}".format(data.axes[1]))
    # print("[INFO] data.axes[2]: {}".format(data.axes[2]))
    # print("")
    # print("[INFO] ax1: {}".format(ax1))
    # print("[INFO] ax2: {}".format(ax2))
    # print("[INFO] ax3: {}".format(ax3))
    # print("=" * 50)
	
    twist = Twist()
    twist.linear.x = ax2
    twist.linear.y = ax1
    twist.angular.z = ax3
	
    keypad = Twist()
    keypad.linear.x = axKL
    keypad.linear.y = axKU

    print(squ.data)
    print(cro.data)
    print(cir.data)
    print(tri.data)
    print(L1.data)
    print(R1.data)
 

    pubtw.publish(twist)
    # pubbt.publish(keypad)
    pubsqu.publish(squ)
    pubcro.publish(cro)
    pubcir.publish(cir)
    pubtri.publish(tri)
    pubL1.publish(L1)
    pubR1.publish(R1)
    pubkey.publish(keypad)
    
# Intializes everything
def start():
    # publishing to "moving_base" and "fcn_button" to control mbed
    global pubax
    global pubbt
    global pubsqu
    global pubcro
    global pubcir
    global pubtri
    global pubtw
    global pubkey
    global pubL1
    global pubR1

    # starts the node
    rospy.init_node('Joy2mbed')
    rate = rospy.Rate(10)
    pubtw = rospy.Publisher("base_twist", 
                            Twist, 
                            tcp_nodelay = True, 
                            queue_size = 1)

    pubsqu = rospy.Publisher("button_square",
			                Bool,
                            queue_size = 1)
    pubcro = rospy.Publisher("button_cross",
			                Bool,
                            queue_size = 1)
    pubcir = rospy.Publisher("button_circle",
			                Bool,
                            queue_size = 1)
    pubtri = rospy.Publisher("button_triangle",
			                Bool,
                            queue_size = 1)
    pubL1 = rospy.Publisher("button_L1",
			            Bool,
			    queue_size = 1)
    pubR1 = rospy.Publisher("button_R1",
			           Bool,
			   queue_size = 1)

    pubkey = rospy.Publisher("button_keypad",
                             Twist,
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
        print("[Error] ROS error")
        pass