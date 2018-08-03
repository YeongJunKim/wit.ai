import sys
sys.path.insert(0, './home/pi/AIY-projects-python/src/aiy')
import aiy.audio

def playAudioPath(path):
        aiy.audio.play_wave(path)

def playAudioText(text):
        aiy.audio.say(text)



