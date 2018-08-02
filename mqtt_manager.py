import sys

sys.path.insert(0, './home/pi/AIY-projects-python/src/aiy')

import aiy.audio

def mqtt(topic,msg):
    print("-------------------------mqtt manager on")
    path = '/home/pi/Pycham/0000_test/mp3_files/voice_ok.wav'
    aiy.audio.play_wave(path)
    import paho.mqtt.client as mqtt

    mqttc = mqtt.Client("python_pub")
    mqttc.connect("192.168.0.5", 1883)
    mqttc.publish(topic, msg)
    mqttc.loop(2)
    print("-------------------------mqtt manager off")