from Device import Device

class SmartLight(Device):
    def __init__(self, kind, ipAddress, brand, currentState, availableMEM, availableCPU, availableDISK):
        super().__init__(kind, ipAddress, brand, currentState, availableMEM, availableCPU, availableDISK)
        self.__lightLevels        = ["weak", "medium", "strong"]
        self.__colorsKind         = ["yellow", "blue", "red", "green", "pink", "grey"]
        self.__temperatures       = [list(range(-10, 41))]
        self.__currentLightLevel  = "medium"
        self.__currentColorKind   = "blue"
        self.__currentTemperature = 20
    
    def getColorsKind(self):
        return self.__colorsKind
    
    def getColorKind(self):
        return self.__currentColorKind
    
    def getLightLevel(self):
        return self.__currentLightLevel
    
    def getLightLevels(self):
        return self.__lightLevels
    
    def getTemperature(self):
        return self.__currentTemperature
    
    def getTemperatures(self):
        return self.__temperatures 
    
    def adjustColor(self, desiredColor:str):
        if self.getColorKind() == desiredColor:
            return "Still same color..."
        if desiredColor not in self.getColorsKind():
            return "Desired color is not in list!"
        self.__currentColorKind = desiredColor
        return f"Color adjusted to {desiredColor}!"

    def adjustTemperature(self, desiredTemperature:int):
        if self.getTemperature() == desiredTemperature:
            return "Still same temperature..."
        if desiredTemperature not in self.getTemperatures():
            return "Desired temperature is not available!"
        self.__currentTemperature == desiredTemperature
        return f"Adjusting SmartLight temperature to {desiredTemperature}!"

    def adjustLightLevel(self, desiredLightLevel:str):
        if self.getLightLevel() == desiredLightLevel:
            return "Still same level..."
        if desiredLightLevel not in self.getLightLevels():
            return "Desired light level is not available..." 
        self.__currentLightLevel == desiredLightLevel
        return f"Light level set up to {desiredLightLevel}!"