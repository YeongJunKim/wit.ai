# autor : colson (Yeong Jun Kim)
# https://www.github.com/YeongJunKim

import logging
import log_manager
import json_manager
import signal

class Timeout:
    class Timeout(Exception):
        pass
    def __init__(self, sec):
        self.sec = sec
    def __enter__(self):
        signal.signal(signal.SIGALRM, self.raise_timeout)
        signal.alarm(self.sec)
    def __exit__(self, *args):
        signal.alarm(0)
    def raise_timeout(self, *args):
        raise Timeout.Timeout()

from wit import Wit

def main():
    logger = log_manager.MyLogger(level = logging.INFO, get = "MAIN")
    logger.add_file_stream_handler('logging.log')
    while True:
        access_token = 'access_token'
        client = Wit(access_token)
        logger.logger.info('Listening.....')
        text = input()
        if text:
            try:
                with Timeout(4):
                    resp = client.message(text)
                    json = json_manager.ManageJson()
                    json.save_json(resp)
                    json.decode_json()
                    logger.logger.info('%s ',text)
                    logger.logger.info(resp)

            except Timeout.Timeout:
                logger.logger.info('timeout')
            except:
                logger.logger.info('error')



if __name__ == '__main__':
    main()