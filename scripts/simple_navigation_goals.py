#!/usr/bin/env python

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

class simple_navigation_goals:

    def go_to(self, x, y, theta):
        rospy.init_node('movebase_client_py')
        client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
        client.wait_for_server()

        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = "map"
        goal.target_pose.header.stamp = rospy.Time.now()

         goal.target_pose.pose.position.x = x
         goal.target_pose.pose.position.y = y
         goal.target_pose.pose.orientation.w = theta

         client.send_goal(goal)
         wait = client.wait_for_result()

         if not wait:
             rospy.logerr("Action server not available!")
             rospy.signal_shutdown("Action server not available!")
         else:
             return client.get_result()

    def _shutdown(self):
        rospy.signal_shutdown("Shutdown!")
