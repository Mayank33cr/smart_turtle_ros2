import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class SquareMover(Node):
    """A ROS 2 node that moves the turtle in a square."""

    def __init__(self):
        super().__init__('square_mover')  # Node name
        # Publisher to the turtle velocity topic
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.timer = self.create_timer(2.0, self.move)  # Call move() every 2 seconds
        self.step = 0  # Keep track of which part of square we're in

    def move(self):
        msg = Twist()

        if self.step % 2 == 0:
            # Move forward
            msg.linear.x = 2.0
            msg.angular.z = 0.0
            self.get_logger().info('Moving forward')
        else:
            # Turn 90 degrees
            msg.linear.x = 0.0
            msg.angular.z = 1.57  # 90 degrees in radians
            self.get_logger().info('Turning 90 degrees')

        self.publisher_.publish(msg)
        self.step += 1

        if self.step == 8:  # 4 sides of square, forward + turn each = 8 steps
            self.get_logger().info('Square completed!')
            rclpy.shutdown()  # Stop ROS 2

def main(args=None):
    rclpy.init(args=args)
    node = SquareMover()
    rclpy.spin(node)

if __name__ == '__main__':
    main()