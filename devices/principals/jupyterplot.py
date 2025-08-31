import csv
import os
import time
from datetime import datetime

from SmartTv import SmartTv
from SmartLight import SmartLight
from SmartWashingMachine import SmartWashingMachine

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

OUTPUT_DIR = "csv"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def save_metrics_to_csv():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(OUTPUT_DIR, f"metrics_{timestamp}.csv")

    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["timestamp", "device", "cpu_usage", "mem_usage", "net_usage"])

        for name, device in devices.items():
            cpu = device.getCpuUsage()[-1] if device.getCpuUsage() else 0
            mem = device.getMemUsage()[-1] if device.getMemUsage() else 0
            net = device.getNetworkUsage()[-1] if device.getNetworkUsage() else 0
            writer.writerow([timestamp, name, cpu, mem, net])

    print(f"✅ Métricas salvas em {filename}")

if __name__ == "__main__":
    INTERVAL = 5 
    print(f"Iniciando coleta de métricas... (intervalo {INTERVAL}s)")
    while True:
        save_metrics_to_csv()
        time.sleep(INTERVAL)
