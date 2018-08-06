# autor : colson (Yeong Jun Kim)
# https://www.github.com/YeongJunKim

import mqtt_manager
import log_manager
import logging

class IoT:
    def __init__(self, level = logging.INFO):

        self.logger = log_manager.MyLogger(level, get = 'IOT')
        self.logger.add_file_stream_handler('logging.log')

        self.mqtt = mqtt_manager.Mqtt()

    def tv_manager(self,things_what, things_action, number):
        self.logger.logger.debug("tv manager on")
        if things_action == "turn on":
            self.mqtt.send_mqtt("home/tv/set","ON")
        elif things_action == "turn on":
            self.mqtt.send_mqtt("home/tv/set","OFF")
        self.logger.logger.debug("tv manager off")

    def light_manager(self,things_what, things_action, number):
        self.logger.logger.debug("light manager on")
        if things_action == "turn on":
            self.mqtt.send_mqtt("home/light/set", "ON")
        elif things_action == "turn off":
            self.mqtt.send_mqtt("home/light/set", "OFF")
        self.logger.logger.debug("light manager off")

    def humidifier_manager(self,things_what, things_action, things_level, number):
        self.logger.logger.debug("humidifier manager on")

        if things_what == "level":
            self.mqtt.send_mqtt("home/humidifier/level/set", things_level)
        elif things_action == "turn on":
            self.mqtt.send_mqtt("home/humidifier/set", "ON")
        elif things_action == "turn off":
            self.mqtt.send_mqtt("home/humidifier/set", "OFF")

        self.logger.logger.debug("humidifier manager off")

    def fan_manager(self,things_what, things_action, things_level, number):
        self.logger.logger.debug("fan manager on")

        if things_what == "speed" and number != -1:
            self.mqtt.send_mqtt("home/fan/speed/set", number)
        elif things_what == "oscillate" and (
                things_action == "turn on" or things_action == "start" or things_action == "set"):
            self.mqtt.send_mqtt("home/fan/oscillate/set", "ON")
        elif things_what == "oscillate" and (things_action == "turn off" or things_action == "stop"):
            self.mqtt.send_mqtt("home/fan/oscillate/set", "OFF")
        elif things_action == "turn on":
            self.mqtt.send_mqtt('home/fan/set', 'ON')
        elif things_action == "turn off" or things_action == "stop":
            self.mqtt.send_mqtt("home/fan/set", "OFF")

        self.logger.logger.debug("fan manager off")

    def home_appliance_manager(self,things, things_what, things_action, things_level, number):
        self.logger.logger.debug("home appliance manager on")
        if things == "TV":
            self.tv_manager(things_what, things_action, number)
        elif things == "light":
            self.light_manager(things_what, things_action, number)
        elif things == "humidifier":
            self.humidifier_manager(things_what, things_action, things_level, number)
        elif things == "fan":
            self.fan_manager(things_what, things_action, things_level, number)

        self.logger.logger.debug("home appliance manager off")

    def task_manager(self,intent="none", things="none", things_what="none", things_action="none", things_level="none",
                    number=-1):
        self.logger.logger.debug("task manager on")
        if intent == "home appliance":
            self.home_appliance_manager(things, things_what, things_action, things_level, number)
        elif things != "none":
            self.home_appliance_manager(things, things_what, things_action, things_level, number)
        else:
            self.logger.logger.debug("nothing to do!")
        self.logger.logger.debug("task manager off")

