# autor : colson (Yeong Jun Kim)
# https://www.github.com/YeongJunKim

import sys
import log_manager
import logging
import time
sys.path.insert(0, './home/pi/AIY-projects-python/src/aiy')

class Mqtt:
    def __init__(self, level = logging.INFO):
        self.mqtt_c = 0
        self.logger = log_manager.MyLogger(level, get = 'MQTT')
        self.logger.add_file_stream_handler('logging.log')

    def send_mqtt(self,topic,msg):
        self.logger.logger.info("mqtt manager on")
        import paho.mqtt.client as mqtt

        self.mqtt_c = mqtt.Client("python_pub")
        self.mqtt_c.connect("192.168.0.5", 1883)
        self.mqtt_c.publish(topic, msg)
        self.mqtt_c.loop(2)
        self.logger.logger.info("mqtt manager off")


if __name__ == '__main__':
    a = Mqtt(level = logging.DEBUG)
    a.send_mqtt("home/fan/set", "ON")
    a.send_mqtt("home/fan/set", "OFF")