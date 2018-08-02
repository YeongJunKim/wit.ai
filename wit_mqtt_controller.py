#!/usr/bin/env python3.5
import logging
import json_manager

from wit import Wit

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
)
logger = logging.getLogger('INFO')

def main():


    while True:
        access_token = '66665YBMQQL64GNF6PJV7OGWBFBQGI56'
        client = Wit(access_token)
        logger.info('Listening.....')
        text = input()

        if text:
            logger.info('recognize text is : %s ',text)
            try:
                resp = client.message(text)
                logger.info(resp)
                json_manager.saveJson(resp)
                json_manager.decodeJson()
            except:
                print('error resp')

if __name__ == '__main__':
    main()