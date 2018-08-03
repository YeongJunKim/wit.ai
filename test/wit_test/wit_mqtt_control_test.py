import os
import sys
sys.path.insert(0, './home/pi/AIY-projects-python/src/aiy')
sys.path.insert(1, './home/pi/pywit/wit')

import logging
import json
from collections import OrderedDict
from pprint import pprint
import aiy.voicehat
import json_manager
from wit import Wit

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
)
logger = logging.getLogger('INFO')






def mqtt(topic,msg):
    import paho.mqtt.client as mqtt

    mqttc = mqtt.Client("python_pub")
    mqttc.connect("192.168.0.5", 1883)
    mqttc.publish(topic, msg)
    mqttc.loop(2)

def main():
    button = aiy.voicehat.get_button()
    access_token = '66665YBMQQL64GNF6PJV7OGWBFBQGI56'
    client = Wit(access_token)
    print(".....check client........OK")

    while True:
        print('Press the button and input the text')
        logger.info('Press the button and input the text')
        button.wait_for_press()
        logger.info('Listening.....')
        text = input()

        if text:
            logger.info('recognize text is : %s ',text)
            resp = client.message(text)
            logger.info(resp)
            json_manager.saveJson(resp)


if __name__ == '__main__':
    main()