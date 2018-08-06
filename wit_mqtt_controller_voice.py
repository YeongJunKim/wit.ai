import sys
sys.path.insert(0, './home/pi/AIY-projects-python/src/aiy')
import logging
import json_manager
import aiy.assistant.grpc
import aiy.audio
import aiy.voicehat
import play_sound

from wit import Wit

import signal

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

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
)
logger = logging.getLogger('INFO')

def main():
    status_ui = aiy.voicehat.get_status_ui()
    status_ui.status('starting')
    assistant = aiy.assistant.grpc.get_assistant()
    button = aiy.voicehat.get_button()

    with aiy.audio.get_recorder():
        play_sound.playAudioText('power on')
        while True:
            access_token = '66665YBMQQL64GNF6PJV7OGWBFBQGI56'
            client = Wit(access_token)

            play_sound.playAudioText('press button and speak')
            button.wait_for_press()

            text, audio = assistant.recognize()

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