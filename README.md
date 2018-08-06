# wit + mqtt + voice-kit
###### support raspberry pi zero w board with AIY kit.

![image](http://cdn.shopify.com/s/files/1/0176/3274/products/together-16_1024x1024_28d6a279-1133-4974-ba1a-03ea6e735a66_grande.jpg?v=1506698675)

### install
#### 1. install AIY-Voice-kit.
###### ```AIY-Voice-kit``` img download.
https://aiyprojects.withgoogle.com/voice/
#### 2. install pywit.
###### ```pywit``` is the Python SDK for wit.ai.
https://github.com/wit-ai/pywit

#### 3. install paho-mqtt.
```
1. ~ $ apt-get install python3-pip
2. ~ $ pip3 install mqtt-paho
```

#### 4. install this.
```
1. ~ $ pip3 install urllib3
2. ~ $ pip3 install pyopenssl
3. ~ $ pip3 install ndg-httpsclient
4. ~ $ pip3 install pyasn1
5. ~ $ pip3 install requests[security]
```

#### when you run script at startup.
```
1. ~ $ cd /etc/profile.d
2. ~ $ nano {$FILE_NAME}.sh
```
```
#!/bin/bash 

python3.5 {$FILE PATH}.{$FILE_NAME}.py
```
 
###### reboot
```
~ $ reboot
```


#### access token.
#####- you can validate token in https://api.wit.ai

check **access_token.**
```python
def main():
    while True:
        access_token = "access_token"
        client = Wit(access_token)
        logger.info('Listening.....')
        text = input()

        if text:
            logger.info('recognize text is : %s ',text)
            try:
                with Timeout(3):
                    resp = client.message(text)
                    logger.info(resp)
                    json_manager.saveJson(resp)
                    json_manager.decodeJson()
            except Timeout.Timeout:
                print('timeout')
            except:
                print('error resp')

if __name__ == '__main__':
    main()
```


#### examples :
**example : wit_mqtt_controller.py**  
or  
**wit_mqtt_controller_voice.py**


