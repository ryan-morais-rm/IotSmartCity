import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("/home/ryan-correia/Área de trabalho/projetos/repositorios/github/IotSmartCity/jupyter/iot_metrics.csv")

df_tv = df[df["device"] == "light"].reset_index(drop=True)

df_tv["time"] = range(1, len(df_tv) + 1)

plt.figure(figsize=(12, 6))
plt.plot(df_tv["time"], df_tv["cpu_usage"], label="CPU Usage (%)", color="blue")
plt.plot(df_tv["time"], df_tv["mem_usage"], label="Memory Usage (MB)", color="red")
plt.plot(df_tv["time"], df_tv["net_usage"], label="Network Usage (Mbps)", color="green")

plt.title("Smart Light Metrics Over Time")
plt.xlabel("Time (simulated)")
plt.ylabel("Usage")
plt.legend()
plt.grid(True)
plt.show()