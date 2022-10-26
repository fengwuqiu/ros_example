# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
import json
import base64
import hashlib

from std_msgs.msg import String
from cti_msgs.msg import Data

def main(args=None):
    rclpy.init(args=args)

    node = rclpy.create_node('minimal_publisher')
    # publisher = node.create_publisher(String, '/cti/robot/listen', 10)
    publisher = node.create_publisher(Data, '/cti/robot_wx/wechat_monitor', 10)

    # msg = String()
    msg=Data()
    i = 0

    msg.name="https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=d104edeb-9ac7-40f0-85e7-6918729c9ef7"
    content="国庆快乐！！"
    data_vaule= {"msgtype": "text", "text": {"content": content}}
    data_str=str(json.dumps(data_vaule))
    msg.data=data_str

    image_address="/home/qfw/test.jpeg"
    with open(image_address, 'rb') as file:
        data = file.read()
        image_data = str(base64.b64encode(data), 'utf-8')
    image_md5 = hashlib.md5()
    fp = open(image_address, 'rb')
    while True:
        b = fp.read(8096)
        if not b:
            break
        image_md5.update(b)
    image_md5 = image_md5.hexdigest()
    data_ = {"msgtype": "image", "image": {
            "base64": image_data, "md5": image_md5}}

    data_image=str(json.dumps(data_))
    # msg.data=data_image
    msg.type=0
    # msg.data=content
    # msg.type=1
    # msg.data=image_address

    # msg.type=2
    # print(data_image)
    # msg_dir = {}
    # msg_dir['msg_type'] = "text"
    # msg_dir['msg_value'] = "国庆快乐！！！"
    # msg_dir['key_id'] = 'd104edeb-9ac7-40f0-85e7-6918729c9ef7'

    # _dir['msg_type'] = "image"
    # msg_dir['msg_value'] = "/home/qfw/test.png"
    # msg_dir['key_id'] = 'd104edeb-9ac7-40f0-85e7-6918729c9ef7'
    # data = json.dumps(msg_dir)
    # msg.data = data
    # def timer_callback():
    #     nonlocal i
    #     msg.data = 'Hello World: %d' % i
    #     i += 1
    # node.get_logger().info('Publishing: "%s"' % msg)
    publisher.publish(msg)

    # timer_period = 0.5  # seconds
    # timer = node.create_timer(timer_period, timer_callback)

    rclpy.spin(node)

    # Destroy the timer attached to the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    # node.destroy_timer(timer)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main(i)
