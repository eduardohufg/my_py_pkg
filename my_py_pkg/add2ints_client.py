import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64
from example_interfaces.srv import AddTwoInts
import random

class Add2IntsClient(Node):
    def __init__(self):
        super().__init__('add2ints_client')
        
        self.create_timer(3.0, self.send_request)

    def send_request(self):

        a, b = random.randint(1, 9), random.randint(1, 9)
        self.call_add2ints(a, b)

    def call_add2ints(self, a, b):
        client = self.create_client(AddTwoInts, 'add2ints')
        while not client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        request = AddTwoInts.Request()
        request.a = a
        request.b = b
        future = client.call_async(request)
        future.add_done_callback(self.future_callback)

    def future_callback(self, future):
        try:
            response = future.result()
        except Exception as e:
            self.get_logger().info('Service call failed %r' % (e,))
        else:
            self.get_logger().info('Result of add two ints: %d' % (response.sum))

def main(args=None):
    rclpy.init(args=args)
    add2ints_server = Add2IntsClient()
    rclpy.spin(add2ints_server)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
    