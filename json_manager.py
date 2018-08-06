# autor : colson (Yeong Jun Kim)
# https://www.github.com/YeongJunKim

import json
import logging
import iot_manager
import log_manager
from pprint import pprint

class ManageJson:
    def __init__(self, level = logging.INFO):
        self.getIntent = "none"
        self.getThings = "none"
        self.getThings_what = "none"
        self.getThings_action = "none"
        self.getThings_level = "none"
        self.getNumber = -1

        self.data = 0
        self.data_file = 0

        self.logger = log_manager.MyLogger(level, get = 'JSON')
        self.logger.add_file_stream_handler('logging.log')

    def save_json(self, resp):
        with open('react.json','w',encoding="utf-8") as make_file:
            json.dump(resp, make_file, ensure_ascii=False, indent="\t")
            self.logger.logger.debug('json file saved')

    def open_json(self, path = 'react.json'):
        with open(path) as data_file:
            data = json.load(data_file)
            pprint(data)
            self.logger.logger.debug('json file opened')

    def decode_json(self, path = 'react.json'):
        with open(path) as self.data_file:
            self.data = json.load(self.data_file)

            try:
                self.data["entities"]["intent"] = self.data["entities"]["intent"][0]
                self.logger.logger.debug(self.data["entities"]["intent"]["value"])
                self.getIntent = self.data["entities"]["intent"]["value"]
            except (TypeError, KeyError):
                self.logger.logger.debug('warn : 0x0001')
            try:
                self.data["entities"]["things"] = self.data["entities"]["things"][0]
                self.logger.logger.debug(self.data["entities"]["things"]["value"])
                self.getThings = self.data["entities"]["things"]["value"]
            except (TypeError, KeyError):
                self.logger.logger.debug('warn : 0x0002')
            try:
                self.data["entities"]["number"] = self.data["entities"]["number"][0]
                self.logger.logger.debug(self.data["entities"]["things_what"]["value"])
                self.getThings_what = self.data["entities"]["things_what"]["value"]
            except (TypeError, KeyError):
                self.logger.logger.debug('warn : 0x0003')
            try:
                self.data["entities"]["things_action"] = self.data["entities"]["things_action"][0]
                self.logger.logger.debug(self.data["entities"]["things_action"]["value"])
                self.getThings_action = self.data["entities"]["things_action"]["value"]
            except (TypeError, KeyError):
                self.logger.logger.debug('warn : 0x0004')
            try:
                self.data["entities"]["things_what"] = self.data["entities"]["things_what"][0]
                self.logger.logger.debug(self.data["entities"]["number"]["value"])
                self.getNumber = self.data["entities"]["number"]["value"]
            except (TypeError, KeyError):
                self.logger.logger.debug('warn : 0x0005')
            try:
                self.data["entities"]["things_level"] = self.data["entities"]["things_level"][0]
                self.logger.logger.debug(self.data["entities"]["things_level"]["value"])
                self.getThings_level = self.data["entities"]["things_level"]["value"]
            except (TypeError, KeyError):
                self.logger.logger.debug('warn : 0x0006')

            iot = iot_manager.IoT()
            iot.task_manager(self.getIntent, self.getThings, self.getThings_what, self.getThings_action, self.getThings_level, self.getNumber)

def main():
    #decodeJson()
    a = ManageJson()
    a.decode_json()

if __name__ == '__main__':
    main()