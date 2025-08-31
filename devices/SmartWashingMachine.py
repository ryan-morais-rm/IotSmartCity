import time 
from Device import Device

class SmartWashingMachine(Device):
    def __init__(self, kind, ipAddress, brand, currentState, availableCPU, availableMEM, availableDISK):
        super().__init__(kind, ipAddress, brand, currentState, availableCPU, availableMEM, availableDISK)
        self.__clothes      = ["shirt", "jeans", "cap", "jacket", "ties"]
        self.__lidState     = True
        self.__capacity     = 100 
        self.__washingState = None
    
    def getCapacity(self):
        return self.__capacity
    
    def getWashState(self):
        return self.__washingState
    
    def getClothes(self):
        return self.__clothes
    
    def openLid(self):
        if self.__lidState:
            return "Lid already open!"
        self.__lidState = True
        return "Opening lid..."

    def closeLid(self):
        if not self.__lidState:
            return "Lid already close!"
        self.__lidState = False
        return "Closing lid..."

    def putClothes(self, quantity:int):
        if quantity > self.getCapacity():
            return "This capacity is too huge for this WashingMachine!"
        for _ in range(quantity):
            clothe = str(input("Put your clothe: "))
            self.__clothes.append(clothe)
        return "Selection has ended!"

    def retrieveClothes(self):
        if len(self.__clothes) == 0:
            return "Clothes already retrivied!"
        for clothe in list(self.__clothes):
            print(f"Retrieving clothe {clothe}")
            self.__clothes.remove(clothe) 
        return "All clothes has been retrieved!"

    def wash(self):
        if self.getWashState():
            return "We are alreay washing your clothes!" 
        if len(self.__clothes) == 0:
            return f"There are no clothes!"
        for clothe in list(self.__clothes):  
            print(f"Washing this clothe: {clothe}")
            self.__clothes.remove(clothe)
            time.sleep(2)
        self.__washingState = False
        return "Wash has ended!"