# SPDX-FileCopyrightText: 2022 Ryuichi Ueda
# SPDX-License-Identifier: BSD-3-Clause
import rclpy
from rclpy.node import Node
from person_msgs.msg import Person

def cb(msg):
    global node
    node.get_logger().info("Listen: %s" % msg)

rclpy.init()
node = Node("listener")
pub = node.create_subscription(Int16, "person", cb, 10)

rclpy.spin(node)

