import random 
import time
from Device import Device

class SmartTv(Device):
    def __init__(self, kind, ipAddress, brand, currentState, availableMEM, availableCPU, availableDISK):
        super().__init__(kind, ipAddress, brand, currentState, availableMEM, availableCPU, availableDISK)
        self.__channels         = ["globo", "sbt", "redeTV", "record", "band"]
        self.__currentChannel   = None 
        self.__availableNumbers = [int("839" + ''.join(str(random.randint(0,9)) for _ in range(7))) for _ in range(15)]
        self.__connectedApps    = []
        self.__disconnectedApps = ["goatTv", "cartiApp", "MollySavage", "UziLilYou", "Spotify", "eSound", "cazeTv"]
    
    def getAvailableNumbers(self):
        return self.__availableNumbers
    
    def getConnectedApps(self):
        return self.__connectedApps
    
    def getDisconnectedApps(self):
        return self.__disconnectedApps
    
    def changeChannel(self, desiredChannel:str):
        for i in range(len(self.__channels)):
            if desiredChannel == self.__channels[i]:
                self.__currentChannel = desiredChannel
                return f"Channel changed to {self.__currentChannel}!" 
        return f"Could not find channel {desiredChannel}!" 

    def connectApp(self, desiredApp:str):
        if desiredApp in self.getConnectedApps():
            return "Your app is already connected!" 
        print(f"Connecting to {desiredApp}...")
        time.sleep(2) 
        if random.random() < 0.1: 
            return f"Failed to connect to {desiredApp}!"
        self.__connectedApps.append(f"{desiredApp}")
        return f"{desiredApp} is now connected!"
    
    def disconnectApp(self, desiredApp:str):
        if desiredApp in self.getDisconnectedApps():
            return f"Your app is already disconnected!"
        print (f"Disconnecting to {desiredApp}...")
        time.sleep(2)
        if random.random() < 0.1:
            return f"Failed to disconnect to {desiredApp}"
        self.__disconnectedApps.append(f"{desiredApp}")
        return f"{desiredApp} is now disconnected!"

    def callSomeone(self, desiredNumber:str):
        if desiredNumber not in self.__availableNumbers:
            return "Number is not available!"
        print(f"Calling {desiredNumber}...")
        time.sleep(3)
        print("Having conversation...")
        time.sleep(10)
        print("End of conversation")
        time.sleep(3)
        return "Call has been completed!"