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
publ1 = None
pubr1 = None
publ3 = None
pubr3 = None
pubopt = None
pubps = None
pubpad = None

squ = Bool()
cro = Bool()
cir = Bool()
tri = Bool()
l1 = Bool()
r1 = Bool()
l3 = Bool()
r3 = Bool()
opt = Bool()
ps = Bool()
pad = Bool()

keypad = Twist()
keypad.linear.x = 0
keypad.linear.y = 0

squ.data = False
cro.data = False
cir.data = False
tri.data = False
l1.data = False
r1.data = False
l3.data = False
r3.data = False
opt.data = False
ps.data = False
pad.data = False


reverse_fac = 1.0
speeding_fac = 1.0


def callback(data):
    global reverse_fac
    global speeding_fac
    
    bt = Int32MultiArray()
    bt.data = data.buttons


    if bt.data[0]!=squ.data:
        squ.data = bt.data[0]
        pubsqu.publish(squ)
    if bt.data[1]!=cro.data:
        cro.data = bt.data[1]
        pubcro.publish(cro)
    if bt.data[2]!=cir.data:
        cir.data = bt.data[2]
        pubcir.publish(cir)
    if bt.data[3]!=tri.data:
        tri.data = bt.data[3]
        pubtri.publish(tri)
    if bt.data[4]!=l1.data:
        l1.data = bt.data[4]
        publ1.publish(l1)
    if bt.data[5]!=r1.data:
        r1.data = bt.data[5]
        pubr1.publish(r1)
    if bt.data[8] == 1:
        reverse_fac *= -1.0 #share
    if bt.data[9]!=opt.data:
        opt.data = bt.data[9]
        pubopt.publish(opt)
    if bt.data[10]!=l3.data:
        l3.data = bt.data[10]
        publ3.publish(l3)
    if bt.data[11]!=r3.data:
        r3.data = bt.data[11]
        pubr3.publish(r3)
    if bt.data[12]!=ps.data:
        ps.data = bt.data[12]
        pubps.publish(ps)
    if  bt.data[13]!=pad.data:
        pad.data = bt.data[13]
        pubpad.publish(pad)

    speeding_fac = 1.0
    # -> deceleration
    if not data.axes[3] - 1 == 0: #L2 state
        speeding_fac = speeding_fac - abs(data.axes[3] - 1)/2 +0.05
    # -> acceleration
    if not data.axes[4] - 1 == 0: #R2 state
        speeding_fac = speeding_fac - (data.axes[4] - 1)/2*9
    

    ax1 = np.round(1.0 * speeding_fac * reverse_fac * data.axes[0], 2)
    ax2 = np.round(1.0 * speeding_fac * reverse_fac * data.axes[1], 2)
    ax3 = -np.round(1.0 * speeding_fac * reverse_fac * data.axes[2], 2)

    axKL = data.axes[6]
    axKU = data.axes[7]
	
    twist = Twist()
    twist.linear.x = ax2
    twist.linear.y = ax1
    twist.angular.z = ax3

    if  keypad.linear.x != axKL:
        keypad.linear.x = axKL
    #     keypad.linear.z = 1
    # else:
    #     keypad.linear.z = 0

    if  keypad.linear.y != axKU:
        keypad.linear.y = axKU
    #     keypad.angular.z = 1
    # else:
    #     keypad.angular.z = 0

    pubtw.publish(twist)
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
    global publ1
    global pubr1
    global publ3
    global pubr3
    global pubopt
    global pubps
    global pubpad

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
    publ1 = rospy.Publisher("button_L1",
                            Bool,
                            queue_size = 1)
    pubr1 = rospy.Publisher("button_R1",
                            Bool,
			                queue_size = 1)
    publ3 = rospy.Publisher("button_L3",
                            Bool,
                            queue_size = 1)
    pubr3 = rospy.Publisher("button_R3",
                            Bool,
			                queue_size = 1)
    pubkey = rospy.Publisher("button_keypad",
                             Twist,
                             tcp_nodelay = True,
                             queue_size = 1)
    pubopt = rospy.Publisher("button_opt",
                            Bool,
                            queue_size = 1)
    pubps = rospy.Publisher("button_ps",
                            Bool,
                            queue_size = 1)
    pubpad = rospy.Publisher("button_pad",
                            Bool,
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
