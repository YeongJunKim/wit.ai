#!/usr/bin/python3.5
import os
import sys

sys.path.insert(0, './home/pi/AIY-projects-python/src/aiy')


import logging
import aiy.assistant.grpc
import aiy.audio
import aiy.voicehat
import aiy._drivers._led

from wit import Wit

from aiy._drivers._led import LED


LED_RED = LED(17)

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
)


def main():
    status_ui = aiy.voicehat.get_status_ui()
    status_ui.status('starting')
    assistant = aiy.assistant.grpc.get_assistant()
    led = aiy.voicehat.get_led()
    button = aiy.voicehat.get_button()

    access_token = 'XVV53YJBHIOA3ELM2ZPBPFX5LI7PJQFY'
    client = Wit(access_token)
    print(".....check client........OK")



    with aiy.audio.get_recorder():
        while True:
            led.set_state(aiy.voicehat.LED.BLINK)
            LED_RED.set_state(aiy.voicehat.LED.BLINK)

            #print(led)
            #print(LED_RED)

            status_ui.status('ready')
            print('Press the button and text input')
            button.wait_for_press()
            status_ui.status('listening')
            print('Listening...')
            text = input()

            if text:
                print("recognize text is :" + text)

                resp = client.message(text)

                print(resp)


if __name__ == '__main__':
    main()