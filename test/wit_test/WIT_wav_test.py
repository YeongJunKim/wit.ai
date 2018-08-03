#!/usr/bin/python3.5
import os
import sys

sys.path.insert(0, './home/pi/AIY-projects-python/src/aiy')
sys.path.insert(1, './home/pi/pywit/wit')


import math
import wave
import struct

audio = []
save_audio = []



import numpy as np
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
    print("one step is over")

    with aiy.audio.get_recorder():
        while True:
            led.set_state(aiy.voicehat.LED.BLINK)
            LED_RED.set_state(aiy.voicehat.LED.BLINK)

            print(led)
            print(LED_RED)

            status_ui.status('ready')
            print('Press the button and speak')
            button.wait_for_press()
            status_ui.status('listening')
            print('Listening...')

            text, audio = assistant.recognize()


            if audio:
                aiy.audio.play_audio(audio, assistant.get_volume())

            db_range = -60.0 -(-60.0 * (50 / 100.0))
            db_scaler = 10 ** (db_range / 40)

            datatext = np.multiply(np.frombuffer(audio, dtype=np.int16), db_scaler).astype(np.int16).tobytes()
            global save_audio
            save_audio = datatext
            save_wav('output5.wav')
            play_wav()
            print('audio data is ', datatext)

            path = '/home/pi/Pycham/0000_test/output.wav'
            soundPath = '/usr/share/sounds/alsa/Front_Left.wav'

            resp = None

            with open('/usr/share/sounds/alsa/Front_Left.wav', 'rb') as f:
                resp = client.speech(f, None, {'Content-Type' : 'audio/wav'})
            print('what : ' + str(resp))

def save_wav(file_name):
    # Open up a wav file
    wav_file=wave.open(file_name,"w")

    # wav params
    nchannels = 1
    sampwidth = 2
    sample_rate = 24000

    # 44100 is the industry standard sample rate - CD quality.  If you need to
    # save on file size you can adjust it downwards. The stanard for low quality
    # is 8000 or 8kHz.
    nframes = len(save_audio)
    comptype = "NONE"
    compname = "not compressed"
    wav_file.setparams((nchannels, sampwidth, sample_rate, nframes, comptype, compname))

    # WAV files here are using short, 16 bit, signed integers for the
    # sample size.  So we multiply the floating point data we have by 32767, the
    # maximum value for a short integer.  NOTE: It is theortically possible to
    # use the floating point -1.0 to 1.0 data directly in a WAV file but not
    # obvious how to do that using the wave module in python.
    for sample in save_audio:
        wav_file.writeframes(struct.pack('h',   int(sample) ))

    wav_file.close()
    return

def play_wav():
    print('play_wav')
    path = '/home/pi/Pycham/0000_test/output5.wav'
    aiy.audio.play_wave(path)



if __name__ == '__main__':
    play_wav()
    #main()