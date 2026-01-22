# topic_watchdog

A ROS 2 package that monitors whether a specified topic is alive.


## Nodes

- `watchdog`  
  A node that runs continuously and reports its startup status.


## Usage

```bash
ros2 run topic_watchdog watchdog


### Topics

- `/watchdog/heartbeat` (`std_msgs/Bool`)  
  Publishes `True` periodically as a heartbeat signal.

