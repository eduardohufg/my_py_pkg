import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64
from my_interfaces.srv import ComputeRectangleArea
import random

class ComputeRectangleClient(Node):
    def __init__(self):
        super().__init__('computeRectangle_client')
        
        self.create_timer(3.0, self.send_request)

    def send_request(self):

        a, b = float(random.randint(1, 9)), float(random.randint(1, 9))
        self.call_compute(a, b)

    def call_compute(self, a, b):
        client = self.create_client(ComputeRectangleArea, 'compRec')
        while not client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        request = ComputeRectangleArea.Request()
        request.length = a
        request.width = b
        future = client.call_async(request)
        future.add_done_callback(self.future_callback)

    def future_callback(self, future):
        try:
            response = future.result()
        except Exception as e:
            self.get_logger().info('Service call failed %r' % (e,))
        else:
            self.get_logger().info('Result of compute rectangle areaS: %d' % (response.area))

def main(args=None):
    rclpy.init(args=args)
    add2ints_server = ComputeRectangleClient()
    rclpy.spin(add2ints_server)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
    