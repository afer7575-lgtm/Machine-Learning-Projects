import pandas as pd
import matplotlib.pyplot as plt
from visualization import  Visualizaton

def check_anomaly(row):
    if row['temperature'] > 50:
        return True
    elif row['angular_velocity'] > 1.25:
        return True
    elif row['voltage'] < 26:
        return True
    elif row['current'] > 7:
        return True
    return False

df = pd.read_csv("telemetry_dzz_sem1.csv")
print(df.describe())

df["anomaly"] = df.apply(check_anomaly, axis=1)

print(df.head())

print(df[df["anomaly"] == True])


v = Visualizaton(df)
v.visual("timestamp","temperature")
v.visual("timestamp","voltage")
v.visual("timestamp","current")
v.visual("timestamp","angular_velocity")

df_an = df[df["anomaly"] == True]

v_an = Visualizaton(df_an)
v.visual("timestamp","anomaly")