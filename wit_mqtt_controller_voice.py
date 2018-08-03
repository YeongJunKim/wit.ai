import sys

sys.path.insert(0, './home/pi/AIY-projects-python/src/aiy')

import logging
import json_manager
import aiy.assistant.grpc
import aiy.audio
import aiy.voicehat
import aiy._drivers._led

from wit import Wit

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
        aiy.audio.play_wave('/home/pi/Pycham/0000_test/voice_files/voice_power.wav')
        while True:
            access_token = '66665YBMQQL64GNF6PJV7OGWBFBQGI56'
            client = Wit(access_token)
            print('Press the button and speak')
            button.wait_for_press()

            aiy.audio.play_wave('/home/pi/Pycham/0000_test/voice_files/voice_pre.wav')

            logger.info('Listening.....')
            text, audio = assistant.recognize()

            if audio:
                logger.info('get audio')

            if text:
                logger.info('recognize text is : %s ',text)
                try:
                    resp = client.message(text)
                    logger.info(resp)
                    json_manager.saveJson(resp)
                    json_manager.decodeJson()
                except:
                    aiy.audio.play_wave('/home/pi/Pycham/0000_test/voice_files/voice_don.wav')
                    print('error resp')

if __name__ == '__main__':
    main()