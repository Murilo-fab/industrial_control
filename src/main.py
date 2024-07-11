#!/usr/bin/env python3

import rclpy
import threading
from rclpy.executors import MultiThreadedExecutor
from ariac_msgs.msg import Order as OrderMsg, KittingTask as KT
from industrial_control.interface import Interface


def main(args=None):
    rclpy.init(args=args)
    interface = Interface()
    executor = MultiThreadedExecutor()
    executor.add_node(interface)

    spin_thread = threading.Thread(target=executor.spin)
    spin_thread.start()
    
    interface.start_competition()
    
    interface.complete_orders()

    interface.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()