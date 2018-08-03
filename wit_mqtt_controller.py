import logging
import json_manager
import signal
import time

class Timeout():
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

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
)
logger = logging.getLogger('INFO')

def main():
    while True:
        access_token = 'access_token'
        client = Wit(access_token)
        logger.info('Listening.....')
        text = input()

        if text:
            logger.info('recognize text is : %s ',text)
            try:
                with Timeout(3):
                    resp = client.message(text)
                    logger.info(resp)
                    json_manager.saveJson(resp)
                    json_manager.decodeJson()
            except Timeout.Timeout:
                print('timeout')
            except:
                print('error resp')

if __name__ == '__main__':
    main()