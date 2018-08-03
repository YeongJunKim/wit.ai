import aiy.audio

def playAudio(type):
    with aiy.audio.get_recorder():
        path = '/home/pi/Pycham/0000_test/voice_files/voice_power.wav'
        aiy.audio.play_wave(path)





