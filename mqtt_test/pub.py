import paho.mqtt.client as mqtt

mqttc = mqtt.Client("python_pub")
mqttc.connect("192.168.0.5", 1883)
mqttc.publish("home/light/set", "OFF")
mqttc.loop(2)