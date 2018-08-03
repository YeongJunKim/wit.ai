import aiy.audio

def playAudioPath(path):
    with aiy.audio.get_recorder():
        aiy.audio.play_wave(path)

def playAudioText(text):
    with aiy.audio.get_recorder():
        aiy.audio.say(text)



