import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64
from example_interfaces.srv import AddTwoInts

class Add2IntsServer(Node):
    def __init__(self):
        super().__init__('add2ints_server')
        self.server = self.create_service(AddTwoInts, 'add2ints', self.service_callback)

    def service_callback(self, request, response):
        response.sum = request.a + request.b

        self.get_logger().info('Incoming request\na: %d b: %d' % (request.a, request.b))
        return response


def main(args=None):
    rclpy.init(args=args)
    add2ints_server = Add2IntsServer()
    rclpy.spin(add2ints_server)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
    