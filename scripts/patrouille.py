#! /usr/bin/python
import rospy
import math

import traceback
import sys
import simple_navigation_goals

if __name__ == "__main__":
  try:
    rospy.init_node("test_scenario")
    rospy.loginfo("SimpleNavigationGoals Initialization")
    nav_goals = simple_navigation_goals.SimpleNavigationGoals()
    rospy.loginfo("Initializations done")

    # What to do if shut down (e.g. ctrl + C or failure)
    rospy.on_shutdown(nav_goals._shutdown)

    while True:
      rospy.loginfo("Go to -2, 0, 0")
      if not (nav_goals.go_to(-2, 0, 0)):
        break
      rospy.loginfo("Go to 0.5, 0.5, PI/2")
      if not (nav_goals.go_to(0.5, 0.5, math.pi/2)):
        break
      rospy.loginfo("Go to 1.6, -1.6, 0")
      if not (nav_goals.go_to(1.6, -1.6, 0)):
        break

    rospy.spin()
  except rospy.ROSInterruptException:
    rospy.logerr(traceback.format_exc())

  rospy.loginfo("test terminated.")
