from flask import Flask, jsonify
from SmartTv import SmartTv
from SmartLight import SmartLight
from SmartWashingMachine import SmartWashingMachine

app = Flask(__name__)

DeviceSmartTv = SmartTv(kind="CrystalUHD", ipAddress="192.168.10.100", brand="Apple",
                        currentState=True, availableMEM=2048, availableCPU=100, availableDISK=128)
DeviceSmartLight = SmartLight(kind="FullShine", ipAddress="192.168.10.200", brand="DecorHome",
                              currentState=True, availableMEM=64, availableCPU=100, availableDISK=4)
DeviceWashingMachine = SmartWashingMachine(kind="UltraWash", ipAddress="192.168.10.50", brand="Samsung",
                                           currentState=True, availableMEM=256, availableCPU=100, availableDISK=20)

devices = {
    "tv": DeviceSmartTv,
    "light": DeviceSmartLight,
    "washer": DeviceWashingMachine
}

@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to your Home IoT controller!",
        "available_devices": list(devices.keys())
    })

@app.route("/devices")
def list_devices():
    return jsonify({
        "tv": DeviceSmartTv.describeDevice(),
        "light": DeviceSmartLight.describeDevice(),
        "washer": DeviceWashingMachine.describeDevice()
    })

@app.route("/metrics")
def metrics():
    return jsonify({
        "tv": {
            "state": DeviceSmartTv.getCurrentState(),
            "cpu": DeviceSmartTv.getCpuUsage(),
            "memory": DeviceSmartTv.getMemUsage(),
            "network": DeviceSmartTv.getNetworkUsage()
        },
        "light": {
            "state": DeviceSmartLight.getCurrentState(),
            "cpu": DeviceSmartLight.getCpuUsage(),
            "memory": DeviceSmartLight.getMemUsage(),
            "network": DeviceSmartLight.getNetworkUsage()
        },
        "washer": {
            "state": DeviceWashingMachine.getCurrentState(),
            "cpu": DeviceWashingMachine.getCpuUsage(),
            "memory": DeviceWashingMachine.getMemUsage(),
            "network": DeviceWashingMachine.getNetworkUsage()
        }
    })

@app.route("/tv")
def tv_info():
    return jsonify({
        "general": DeviceSmartTv.describeDevice(),
        "apps_connected": DeviceSmartTv.getConnectedApps(),
        "apps_disconnected": DeviceSmartTv.getDisconnectedApps(),
        "available_numbers": DeviceSmartTv.getAvailableNumbers()
    })

@app.route("/light")
def light_info():
    return jsonify({
        "general": DeviceSmartLight.describeDevice(),
        "colors": DeviceSmartLight.getColorsKind(),
        "current_color": DeviceSmartLight.getColorKind(),
        "light_levels": DeviceSmartLight.getLightLevels(),
        "current_light": DeviceSmartLight.getLightLevel(),
        "temperature": DeviceSmartLight.getTemperature()
    })

@app.route("/washer")
def washer_info():
    return jsonify({
        "general": DeviceWashingMachine.describeDevice(),
        "capacity": DeviceWashingMachine.getCapacity(),
        "clothes": DeviceWashingMachine.getClothes(),
        "wash_state": DeviceWashingMachine.getWashState()
    })

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
