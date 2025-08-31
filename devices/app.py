import random
from flask import Flask, jsonify, Response
from prometheus_client import generate_latest, Gauge, CollectorRegistry
from devices.principals.SmartTv import SmartTv
from devices.principals.SmartLight import SmartLight
from devices.principals.SmartWashingMachine import SmartWashingMachine


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

registry = CollectorRegistry()

cpu_gauges = {}
mem_gauges = {}
net_gauges = {}

for name, device in devices.items():
    cpu_gauges[name] = Gauge(f"{name}_cpu_usage", f"CPU usage for {name}", registry=registry)
    mem_gauges[name] = Gauge(f"{name}_memory_usage", f"Memory usage for {name}", registry=registry)
    net_gauges[name] = Gauge(f"{name}_network_usage", f"Network usage for {name}", registry=registry)

def update_metrics():
    for name, device in devices.items():
        if not hasattr(device, "_cpu_direction"):
            device._cpu_direction = 2
        if not hasattr(device, "_cpu_value"):
            device._cpu_value = random.randint(0, 100)
        
        device._cpu_value += device._cpu_direction
        if device._cpu_value >= 100 or device._cpu_value <= 0:
            device._cpu_direction *= -1 
            device._cpu_value = max(0, min(100, device._cpu_value))

        if not hasattr(device, "_mem_direction"):
            device._mem_direction = 2
        if not hasattr(device, "_mem_value"):
            device._mem_value = random.randint(0, 100)

        device._mem_value += device._mem_direction
        if device._mem_value >= 100 or device._mem_value <= 0:
            device._mem_direction *= -1
            device._mem_value = max(0, min(100, device._mem_value))

        if not hasattr(device, "_net_direction"):
            device._net_direction = 20
        if not hasattr(device, "_net_value"):
            device._net_value = random.randint(0, 1000)

        device._net_value += device._net_direction
        if device._net_value >= 1000 or device._net_value <= 0:
            device._net_direction *= -1
            device._net_value = max(0, min(1000, device._net_value))

        device._cpuUsageList = [device._cpu_value]
        device._memUsageList = [device._mem_value]
        device._netUsageList = [device._net_value]

        cpu_gauges[name].set(device._cpu_value)
        mem_gauges[name].set(device._mem_value)
        net_gauges[name].set(device._net_value)

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
    update_metrics()
    return Response(generate_latest(registry), mimetype="text/plain")

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
