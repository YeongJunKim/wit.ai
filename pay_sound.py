import sys
sys.path.insert(0, './home/pi/AIY-projects-python/src/aiy')
import aiy.audio

def playAudioPath(path):
    with aiy.audio.get_recorder():
        aiy.audio.play_wave(path)

def playAudioText(text):
    with aiy.audio.get_recorder():
        aiy.audio.say(text)



