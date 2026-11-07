import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class ObstacleAvoidance(Node):
    def __init__(self):
        super().__init__('obstacle_avoidance')
        
        self.scan_sub = self.create_subscription(
            LaserScan, '/scan',
            self.scan_callback, 10)
        
        self.cmd_pub = self.create_publisher(
            Twist, '/cmd_vel', 10)
        
        self.get_logger().info('Obstacle avoidance started!')

    def scan_callback(self, msg):
        twist = Twist()
        
        front = msg.ranges[0:10] + msg.ranges[350:360]
        valid = [r for r in front 
                 if r > 0.1 and r < float('inf')]
        
        if len(valid) == 0:
            twist.linear.x = 0.0
            twist.angular.z = 0.0
        elif min(valid) < 0.5:
            twist.linear.x = 0.0
            twist.angular.z = 0.5
            self.get_logger().info(
                f'Obstacle at {min(valid):.2f}m — turning')
        else:
            twist.linear.x = 0.2
            twist.angular.z = 0.0
            self.get_logger().info('Moving forward')
        
        self.cmd_pub.publish(twist)

def main(args=None):
    rclpy.init(args=args)
    node = ObstacleAvoidance()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
    