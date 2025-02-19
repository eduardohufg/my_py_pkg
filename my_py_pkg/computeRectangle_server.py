import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64
from my_interfaces.srv import ComputeRectangleArea

class ComputeRectangle(Node):
    def __init__(self):
        super().__init__('computeRectangle_server')
        self.server = self.create_service(ComputeRectangleArea, 'compRec', self.service_callback)

    def service_callback(self, request, response):
        response.area = request.length * request.width

        self.get_logger().info('Incoming request\na: %d b: %d' % (request.length, request.width))
        return response


def main(args=None):
    rclpy.init(args=args)
    add2ints_server = ComputeRectangle()
    rclpy.spin(add2ints_server)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
    