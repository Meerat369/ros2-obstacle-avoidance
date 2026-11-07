# ROS2 Obstacle Avoidance

TurtleBot3 Burger avoiding obstacles in Gazebo using LaserScan data, built with ROS2 Humble.

## How it works
- Subscribes to /scan (LaserScan)
- Checks the front-facing readings
- Obstacle closer than 0.5 m: stops and turns
- Path clear: moves forward at 0.2 m/s
- Publishes velocity commands on /cmd_vel

## Demo
![Gazebo demo](gazebo_demo.png)
![Terminal output](terminal_output.png)

## How to run
Terminal 1:
export TURTLEBOT3_MODEL=burger
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py gui:=false

Terminal 2:
ros2 run obstacle_avoidance obstacle_avoidance

## Environment
- Ubuntu 22.04, ROS2 Humble, Gazebo, TurtleBot3 Burger
