import paho.mqtt.client as mqtt



def on_connect(client, userdata, rc):
  print ("Connected with result coe " + str(rc))
  client.subscribe("hello/world")

def on_message(client, userdata, msg):
  print ("Topic: ", msg.topic + '\nMessage: ' + str(msg.payload))


def main():
    client = mqtt.Client()  # MQTT Client 오브젝트 생성
    client.on_connect = on_connect  # on_connect callback 설정
    client.on_message = on_message  # on_message callback 설정

    client.connect("test.mosquitto.org", 1883, 60)  # MQTT 서버에 연결

    client.loop_forever()

if __name__ == '__main__':
    main()

import paho.mqtt.client as mqtt

