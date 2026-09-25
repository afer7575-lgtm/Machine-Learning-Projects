import pandas as pd
from pathlib import Path
from utils.visualization import  Visualization

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


csv_path = Path(__file__).parent.parent / "data" / "telemetry_dzz_sem1.csv"
df = pd.read_csv(csv_path)
print(df.describe())

df["anomaly"] = df.apply(check_anomaly, axis=1)

print(df.head())

print(df[df["anomaly"] == True])

path_to_save = Path(__file__).parent / "image"
v = Visualization(df, path_to_save)
v.visual_all("timestamp")