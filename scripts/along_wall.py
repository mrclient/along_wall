#!/usr/bin/python

import rospy
from math import cos, pi

if __name__=="__main__":

    rospy.init_node("along_wall_node)

    forw_vel = rospy.get_param("~forward_velocity", 1.0)
    kp = rospy.get_param("~controller_coefficient", 1.0)
    need_dist = rospy.get_param("~needed_distance", 2.0)
    need_dist /= cos(pi/4)
