# ROS2 Obstacle Avoidance

TurtleBot3 Burger avoiding obstacles in Gazebo using LaserScan data, built with ROS2 Humble.

## How it works
- Subscribes to /scan (LaserScan)
- Checks the front-facing readings
- Obstacle closer than 0.5 m: stops and turns
- Path clear: moves forward at 0.2 m/s
- Publishes velocity commands on /cmd_vel

## Demo
<img width="889" height="574" alt="terminal_output" src="https://github.com/user-attachments/assets/e7c9b37c-7e2d-43b3-a06c-36300b43bd2f" />
<img width="798" height="390" alt="gazebo_demo" src="https://github.com/user-attachments/assets/8031ee20-f5c2-4a4f-96e2-254d9852e022" />

## How to run
Terminal 1:
export TURTLEBOT3_MODEL=burger
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py gui:=false

Terminal 2:
ros2 run obstacle_avoidance obstacle_avoidance

## Environment
- Ubuntu 22.04, ROS2 Humble, Gazebo, TurtleBot3 Burger
