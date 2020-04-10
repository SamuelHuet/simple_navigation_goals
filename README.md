# [Simple Navigation Goal](https://github.com/SamuelHuet/simple_navigation_goals)

_[![ROS Melodic](https://img.shields.io/badge/ROS-Melodic-red)](http://wiki.ros.org/melodic/Installation/Ubuntu)_ _[![TurtleBot3](https://img.shields.io/badge/TurtleBot-3-brightgreen)](http://emanual.robotis.com/docs/en/platform/turtlebot3/pc_setup/)_ ![LICENSE](https://img.shields.io/badge/LICENSE-Apache%202.0-informational)

![MelodicTurtle](https://raw.githubusercontent.com/ros/ros_tutorials/melodic-devel/turtlesim/images/melodic.png)

>The goal of this projet is to succeed a simplified version of the "Carry my luggage" test, imagined by the [RobotCup@Home](https://athome.robocup.org) contest.

>For more information about rules and regulations, please refer to [this document](https://robocupathome.github.io/RuleBook/rulebook/master.pdf).

- [Simple Navigation Goal](#simple-navigation-goal)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [How To](#how-to)
  - [Usage](#usage)
  - [Meta](#meta)
  - [Contributing](#contributing)

## Prerequisites

- [Ubuntu 18.0.4 recommended](https://ubuntu.com/download/desktop)
- [ROS Melodic](http://wiki.ros.org/melodic/Installation/Ubuntu)
- [TurtleBot3](http://emanual.robotis.com/docs/en/platform/turtlebot3/pc_setup/)
- [Git](https://git-scm.com/)

## Installation

Simply clone this repository on your computer and catkin_make:
```
$ cd ~/catkin_ws/src
$ git clone https://github.com/SamuelHuet/simple_navigation_goals.git
$ cd ..
$ catkin_make
```

## How To

Patrol points tested and working on turtlebot3_world
```
$ rosrun simple_navigation_goals patrouille.py
```
Or you can run in your own python script
```
import simple_navigation_goals
rospy.init_node("test_scenario")
nav_goals = simple_navigation_goals.SimpleNavigationGoals()

nav_goals.go_to(x, y, rad)

rospy.on_shutdown(nav_goals._shutdown)
rospy.spin()
```
## Usage

The project contains a complete ROS Melodic package with several python scripts. The ``simple_navigation_goals.py`` script is executed with the ``patrouille.py`` script in order to realize all necessary tests required to pass the challenge.

In order to pass the test, the TurtleBot have to patrol with three checkpoints. The checkpoints will be drawn randomly but can be modified in order to approach the simulation towards the physical reality.

## Meta

Distributed under the Apache 2.0 license. See ``LICENSE`` for more information.

## Contributing

1. Fork it (<https://github.com/SamuelHuet/simple_navigation_goals/fork>)
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request
