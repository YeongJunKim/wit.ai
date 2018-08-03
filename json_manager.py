import json
import iot_manager
from pprint import pprint

def saveJson(resp):
    with open('react.json', 'w', encoding="utf-8") as make_file:
        json.dump(resp, make_file, ensure_ascii=False, indent="\t")

def openJson():
    with open('react.json') as data_file:
        data = json.load(data_file)
        pprint(data)

def decodeJson():
    with open('react.json') as data_file:
        data = json.load(data_file)

        try:
            data["entities"]["intent"] = data["entities"]["intent"][0]
        except:
            print('wanning : 0x0001')
        try:
            data["entities"]["things"] = data["entities"]["things"][0]
        except:
            print('wanning : 0x0002')
        try:
            data["entities"]["number"] = data["entities"]["number"][0]
        except:
            print('wanning : 0x0003')
        try:
            data["entities"]["things_action"] = data["entities"]["things_action"][0]
        except:
            print('wanning : 0x0004')
        try:
            data["entities"]["things_what"] = data["entities"]["things_what"][0]
        except:
            print('wanning : 0x0005')
        try:
            data["entities"]["things_level"] = data["entities"]["things_level"][0]
        except:
            print('wanning : 0x0006')

        #pprint(data)

        getintent = "none"
        getthings = "none"
        getthings_what = "none"
        getthings_action = "none"
        getthings_level = "none"
        getnumber = -1

        try:
            print("1 :",data["entities"]["intent"]["value"])
            getintent = data["entities"]["intent"]["value"]
        except (TypeError, KeyError):
            print('1 : wanning : no intent value')
        try:
            print("2 :",data["entities"]["things"]["value"])
            getthings = data["entities"]["things"]["value"]
        except (TypeError, KeyError):
            print('2: wanning : no things value')
        try:
            print("3 :",data["entities"]["things_what"]["value"])
            getthings_what = data["entities"]["things_what"]["value"]
        except (TypeError, KeyError):
            print('3: wanning : no things_what value')
        try:
            print("4 :",data["entities"]["things_action"]["value"])
            getthings_action = data["entities"]["things_action"]["value"]
        except (TypeError, KeyError):
            print('4: wanning : no things_action value')
        try:
            print("5 :",data["entities"]["number"]["value"])
            getnumber = data["entities"]["number"]["value"]
        except (TypeError, KeyError):
            print('5 : wanning : no number_value')
        try:
            print("6 :",data["entities"]["things_level"]["value"])
            getthings_level = data["entities"]["things_level"]["value"]
        except (TypeError, KeyError):
            print("6 : wanning : no things_level")

        iot_manager.taskManager(getintent,getthings,getthings_what,getthings_action,getthings_level,getnumber)

    #print(data.get("entities", 0))
    #print(data.keys())
def main():
    decodeJson()


if __name__ == '__main__':
    main()