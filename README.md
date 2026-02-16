Smart Turtle – My First ROS 2 Project

Hi! This is my very first ROS 2 project 

In this project, I created a custom ROS 2 node that makes the turtle in turtlesim move in a square pattern.

It was my first hands-on experience with ROS 2, Docker, and robotic node communication
What This Project Does
	•	Launches the turtlesim simulator
	•	Runs a custom Python ROS 2 node
	•	Publishes velocity commands
	•	Makes the turtle draw a square

Simple idea — but huge learning step for me.

What I Used
	•	ROS 2 Humble Hawksbill
	•	Python (rclpy)
	•	turtlesim package
	•	colcon build system
	•	Docker (VNC-based ROS container)
	•	macOS
 How to Run
After building the workspace: ros2 run turtlesim turtlesim_node
ros2 run smart_turtle square_mover
The turtle will start moving in a square inside the simulator window.

 What I Learned
	•	How ROS 2 nodes communicate using topics
	•	How to publish velocity commands
	•	How to structure a ROS 2 Python package
	•	How to build using colcon
	•	How to run multiple ROS nodes at once

This project helped me understand the basics of robotics software architecture.
