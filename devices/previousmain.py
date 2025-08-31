import time
from flask import Flask, jsonify 
from SmartTv import SmartTv
from SmartLight import SmartLight
from SmartWashingMachine import SmartWashingMachine 

app = Flask(__name__) 

DeviceSmartTv        = SmartTv(kind="CrystalUHD", ipAddress="192.168.10.100", brand="Apple",
                                currentState=True, availableMEM=2048, availableCPU=100, availableDISK=128)
DeviceSmartLight     = SmartLight(kind="FullShine", ipAddress="192.168.10.200", brand="DecorHome",
                                  currentState=True, availableMEM=64, availableCPU=100,availableDISK=4)
DeviceWashingMachine = SmartWashingMachine(kind="UltraWash", ipAddress="192.168.10.50", brand="Samsung",
                                           currentState=True, availableMEM=256, availableCPU=100, availableDISK=20)
devices = {
    "tv": DeviceSmartTv,
    "light": DeviceSmartLight,
    "washer": DeviceWashingMachine
}

print("Welcome to your Home IoT controller!")
print("Available devices: ")
print("Smart TV: ", DeviceSmartTv.describeDevice())
print("Smart Light:", DeviceSmartLight.describeDevice())
print("Smart Washing Machine:", DeviceWashingMachine.describeDevice())
print("Which device would you like to use?")
time.sleep(1)

execucao = True
while execucao:
    time.sleep(1)

    choice = str(input("Choose device: "))
    if not choice or choice not in devices:
        execucao = False

    if choice == "tv":
        time.sleep(1)
        print("You chose your SmartTV!")
        time.sleep(1)
        print("What would you like to do with your tv?")
        print("Device general options or specific options?")
        option = str(input(": ")) 
        if option in ["general", "specific"]:
            if option == "general":
                print("General options: ")
                print("1. Current State: ")
                print(DeviceSmartTv.getCurrentState())
                print("2. Network Usage: ")
                print(DeviceSmartTv.getNetworkUsage())
                print("3. Memory Usage: ")
                print(DeviceSmartTv.getMemUsage())
                print("4. CPU Usage: ")
                print(DeviceSmartTv.getCpuUsage())
                print("5. Brand: ")
                print(DeviceSmartTv.getBrand())
                print("6. IP Address: ")
                print(DeviceSmartTv.getIpAddress())
                print("7. Kind: ")
                print(DeviceSmartTv.getKind())
            elif option == "specific":
                print("1. Available Numbers")
                print(DeviceSmartTv.getAvailableNumbers())
                print("2. Connected Apps: ")
                print(DeviceSmartTv.getConnectedApps()) 
                print("3. Disconnected Apps: ")
                print(DeviceSmartTv.getDisconnectedApps())
                print("Would you like to use your tv?")
                option1 = bool(input(": "))
                if option1:
                    print("Options: Change channel, connect app, disconnect app, call someone")
                    option2 = str(input(": "))
                    if option2 == "change":
                        channel = input("Channel: ")
                        DeviceSmartTv.changeChannel(desiredChannel=channel)
                    elif option2 == "connect":
                        app = input("App: ")
                        DeviceSmartTv.connectApp(desiredApp=app)
                    elif option2 == "disconnect":
                        app = input("App: ")
                        DeviceSmartTv.disconnectApp(desiredApp=app)
                    elif option2 == "call":
                        number = int(input("Number: "))
                        DeviceSmartTv.callSomeone(desiredNumber=number)
        time.sleep(1)

    elif choice == "light":
        time.sleep(1)
        print("You chose your SmartLight!")
        time.sleep(1)
        print("What would you like to do with your light?")
        print("Device general options or specific options?")
        option = str(input(": ")) 
        if option in ["general", "specific"]:
            if option == "general":
                print("General options: ")
                print("1. Current State: ")
                print(DeviceSmartLight.getCurrentState())
                print("2. Network Usage: ")
                print(DeviceSmartLight.getNetworkUsage())
                print("3. Memory Usage: ")
                print(DeviceSmartLight.getMemUsage())
                print("4. CPU Usage: ")
                print(DeviceSmartLight.getCpuUsage())
                print("5. Brand: ")
                print(DeviceSmartLight.getBrand())
                print("6. IP Address: ")
                print(DeviceSmartLight.getIpAddress())
                print("7. Kind: ")
                print(DeviceSmartLight.getKind())
            elif option == "specific":
                print("1. Colors kind: ")
                print(DeviceSmartLight.getColorsKind())
                print("2. Current color kind: ")
                print(DeviceSmartLight.getColorKind()) 
                print("3. Light levels: ")
                print(DeviceSmartLight.getLightLevels()) 
                print("4. Current light level: ")
                print(DeviceSmartLight.getLightLevel())
                print("5. Temperature: ")
                print(DeviceSmartLight.getTemperature()) 
                print("6. Temperatures: ")
                print(DeviceSmartLight.getTemperatures())
                print("Would you like to use your Lamp?")
                option1 = bool(input(": "))
                if option1:
                    print("Options: Adjust color, Adjust temperature, Adjust light level")
                    option2 = str(input(": "))
                    if option2 == "color":
                        color = input("color: ")
                        DeviceSmartLight.adjustColor(desiredColor=color)
                    elif option2 == "temperature":
                        temperature = input("Celsius desired: ")
                        DeviceSmartLight.adjustTemperature(desiredTemperature=temperature)
                    elif option2 == "light":
                        lightlevel = input("Level: ")
                        DeviceSmartLight.adjustLightLevel(desiredLightLevel=lightlevel)
        time.sleep(1)

    elif choice == "washer":
        time.sleep(1)
        print("You chose your SmartWasher!")
        print("What would you like to do with your Washer?")
        print("Device general options or specific options?")
        option = str(input(": ")) 
        if option in ["general", "specific"]:
            if option == "general":
                print("General options: ")
                print("1. Current State: ")
                print(DeviceWashingMachine.getCurrentState())
                print("2. Network Usage: ")
                print(DeviceWashingMachine.getNetworkUsage())
                print("3. Memory Usage: ")
                print(DeviceWashingMachine.getMemUsage())
                print("4. CPU Usage: ")
                print(DeviceWashingMachine.getCpuUsage())
                print("5. Brand: ")
                print(DeviceWashingMachine.getBrand())
                print("6. IP Address: ")
                print(DeviceWashingMachine.getIpAddress())
                print("7. Kind: ")
                print(DeviceWashingMachine.getKind())
            elif option == "specific":
                print("1. Capacity: ")
                print(DeviceWashingMachine.getCapacity())
                print("2. Wash State: ")
                print(DeviceWashingMachine.getWashState())
                print("3. Clothes: ") 
                print(DeviceWashingMachine.getClothes())
                print("Would you like to use your washer?")
                option1 = bool(input(": "))
                if option1:
                    print("Options: Put clothes, retrieve clothes, wash clothes")
                    option2 = str(input(": "))
                    if option2 == "put":
                        print("How many clothes? ")
                        qtd = int(input(": "))
                        DeviceWashingMachine.putClothes(quantity=qtd)
                    elif option2 == "retrieve":
                        DeviceWashingMachine.retrieveClothes()
                    elif option2 == "wash":
                        DeviceWashingMachine.wash() 
        time.sleep(1)