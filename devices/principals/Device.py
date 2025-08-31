
class Device:
    def __init__(self, kind:str, ipAddress:str, brand:str, currentState:bool, availableMEM:int, availableCPU:int, availableDISK:int):
        self.__kind              = kind # SmartLight, SmartTv, SmartWashing...
        self.__brand             = brand # Dell, Asus, Apple...
        self.__ipAddress         = ipAddress # Network address 192.168.0.10...
        self.__currentState      = currentState # bool
        self.__availableMEM      = availableMEM # 512, 1024...
        self.__availableCPU      = availableCPU # 80%, 10%...
        self.__availableDISK     = availableDISK
        self.__cpuUsageList = []
        self.__memUsageList = []
        self.__netUsageList = []
        cpu_start, cpu_max = 10, 80
        mem_start, mem_max = 128, 1024
        net_start, net_max = 50, 500
        
        for i in range(cpu_start, cpu_max+1, 2):
            self.__cpuUsageList.append(i)
        for i in range(cpu_max, cpu_start-2, -4):
            self.__cpuUsageList.append(i)

        for i in range(mem_start, mem_max+1, 64):
            self.__memUsageList.append(i)
        for i in range(mem_max, mem_start-2, -64):
            self.__memUsageList.append(i)

        for i in range(net_start, net_max+2, 10):
            self.__netUsageList.append(i)
        for i in range(net_max, net_start-1, -20):
            self.__netUsageList.append(i)
    
    def describeDevice(self):
        return {
            "Kind": self.getKind(),
            "Brand": self.getBrand(),
            "IpAddress": self.getIpAddress(),
            "CurrentState": self.getCurrentState(),
        }
    
    def getKind(self):
        return self.__kind
    
    def getBrand(self):
        return self.__brand

    def getIpAddress(self):
        return self.__ipAddress
    
    def getAvailableMem(self):
        return self.__availableMEM 
    
    def getAvailableCPU(self):
        return self.__availableCPU
    
    def getAvailableDisk(self):
        return self.__availableDISK

    def getCpuUsage(self):
        return self.__cpuUsageList

    def getMemUsage(self):
        return self.__memUsageList
    
    def getNetworkUsage(self):
        return self.__netUsageList
    
    def getCurrentState(self):
        if self.__currentState == True:
            return "Powered On"
        return "Powered off"

    def connectDevice(self, ipAddress:str):
        if self.getIpAddress() != ipAddress:
            return False
        return True 

    def disconnectDevice(self, ipAddress:str):
        if self.getIpAddress() != ipAddress:
            return False
        return True 

    def powerOn(self, desiredState:bool):
        if self.getCurrentState() == desiredState:
            return f"Cant modify the state {self.__currentState}, please select another!"
        self.__currentState = desiredState
        return True 

    def shutdown(self, desiredState:bool):
        if self.getCurrentState() == desiredState:
            return f"Cant modify the state {self.__currentState}, please select another!"
        self.__currentState = desiredState
        return True 