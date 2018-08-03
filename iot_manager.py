import mqtt_manager

def tvManager(things_what, things_action, number):
    print("--------------------tv manager on")
    if things_action == "turn on":
        mqtt_manager.mqtt("home/tv/set","ON")
    elif things_action == "turn on":
        mqtt_manager.mqtt("home/tv/set","OFF")


    print("--------------------tv manager off")

def lightManager(things_what, things_action, number):
    print("--------------------light manager on")
    if things_action == "turn on":
        mqtt_manager.mqtt("home/light/set", "ON")
    elif things_action == "turn off":
        mqtt_manager.mqtt("home/light/set", "OFF")
    print("--------------------light manager off")

def humidifierManager(things_what, things_action,things_level, number):
    print("--------------------humidifier manager on")

    if things_what == "level":
        mqtt_manager.mqtt("home/humidifier/level/set",things_level)
    elif things_action == "turn on":
        mqtt_manager.mqtt("home/humidifier/set","ON")
    elif things_action == "turn off":
        mqtt_manager.mqtt("home/humidifier/set","OFF")

    print("--------------------humidifier manager off")

def fanManager(things_what, things_action, things_level, number):
    print("--------------------fan manager on")


    if things_what == "speed" and number != -1:
        mqtt_manager.mqtt("home/fan/speed/set", number)
    elif things_what == "oscillate" and (things_action == "turn on" or things_action == "start" or things_action == "set"):
        mqtt_manager.mqtt("home/fan/oscillate/set", "ON")
    elif things_what == "oscillate" and (things_action == "turn off" or things_action == "stop"):
        mqtt_manager.mqtt("home/fan/oscillate/set", "OFF")
    elif things_action == "turn on":
        mqtt_manager.mqtt('home/fan/set','ON')
    elif things_action == "turn off" or things_action == "stop":
        mqtt_manager.mqtt("home/fan/set", "OFF")



    print("--------------------fan manager off")

def homeApplianceManager(things, things_what,things_action ,things_level, number):
    print("---------------home appliance manager on")
    if things == "TV":
        tvManager(things_what, things_action, number)
    elif things == "light":
        lightManager(things_what, things_action, number)
    elif things == "humidifier":
        humidifierManager(things_what, things_action,things_level, number)
    elif things == "fan":
        fanManager(things_what, things_action, things_level, number)

    print("---------------home appliance manager off")

def taskManager(intent="none", things="none", things_what="none", things_action = "none",things_level = "none", number=-1):
    print("----------task manager on")
    if intent == "home appliance":
        homeApplianceManager(things, things_what,things_action ,things_level, number)
    elif things != "none":
        homeApplianceManager(things, things_what, things_action, things_level, number)
    else:
        print("nothing to do!")
    print("----------task manager off")
