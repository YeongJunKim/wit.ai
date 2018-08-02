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
sample_rate = 44100.0



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

            db_range = -60.0 -(-60.0 * (50 / 100.0))
            db_scaler = 10 ** (db_range / 20)

            datatext = np.multiply(np.frombuffer(
                audio, dtype=np.int16), db_scaler).astype(np.int16).tobytes()

            save_audio = audio

            print('audio data is ', datatext)

            if text:
                print("recognize text is :" + text)
                resp = client.message(text)
                print(resp)

            if text:
                if text == 'goodbye':
                    status_ui.status('stopping')
                    print('Bye!')
                    break
                print('You said "', text, '"')
            if audio:
                aiy.audio.play_audio(audio, assistant.get_volume())
                path = '/home/pi/Pycham/0000_test/output.wav'
                aiy.audio.play_wave(path)

def append_silence(duration_milliseconds=500):
    """
    Adding silence is easy - we add zeros to the end of our array
    """
    num_samples = duration_milliseconds * (sample_rate / 1000.0)

    for x in range(int(num_samples)):
        audio.append(0.0)

    return

def append_sinewave(
        freq=440.0,
        duration_milliseconds=500,
        volume=1.0):
    """
    The sine wave generated here is the standard beep.  If you want something
    more aggresive you could try a square or saw tooth waveform.   Though there
    are some rather complicated issues with making high quality square and
    sawtooth waves... which we won't address here :)
    """

    global audio # using global variables isn't cool.

    num_samples = duration_milliseconds * (sample_rate / 1000.0)

    for x in range(int(num_samples)):
        audio.append(volume * math.sin(2 * math.pi * freq * ( x / sample_rate )))

    return

def save_wav(file_name):
    # Open up a wav file
    wav_file=wave.open(file_name,"w")

    # wav params
    nchannels = 1

    sampwidth = 2

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
        wav_file.writeframes(struct.pack('h', int( sample * 32767.0 )))

    wav_file.close()

    return



if __name__ == '__main__':
    # append_sinewave(volume=0.25)
    # append_silence()
    # append_sinewave(volume=0.5)
    # append_silence()
    # append_sinewave()
    # save_wav("output.wav")



    main()