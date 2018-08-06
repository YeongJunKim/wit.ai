# autor : colson (Yeong Jun Kim)
# https://www.github.com/YeongJunKim

import logging

class MyLogger:

    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    )

    def __init__(self, level, get = 'system'):
        self.file_handler = 0
        self.logger = logging.getLogger(get)
        self.logger.setLevel(level)
        self.logger.debug('logger name : '+get+' is setup')

    def set_propagate(self, propagate):
        self.logger.propagate = propagate

    def set_level(self, level):
        self.logger.setLevel(level)

    def add_stream_handler(self, formatter = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"):
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        self.logger.addHandler(stream_handler)
        self.logger.debug("create stream handler complete")

    def add_file_stream_handler(self, name = 'system.log', formatter = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"):
        self.file_handler = logging.FileHandler(name)
        self.file_handler.setFormatter(logging.Formatter(formatter))
        self.logger.addHandler(self.file_handler)
        self.logger.debug("create file handler complete")

    def test_stream(self):
        self.logger.debug("this is debug")
        self.logger.info("this is info")
        self.logger.warning("this is warning")
        self.logger.error("this is error")
        self.logger.critical("this is critical")

if __name__ == '__main__':
    c = MyLogger(logging.DEBUG)

    c.add_file_stream_handler('logger.log')
    c.logger.debug("this is debug")
    c.logger.info("this is info")
    c.logger.warning("this is warning")
    c.logger.error("this is error")
    c.logger.critical("this is critical")