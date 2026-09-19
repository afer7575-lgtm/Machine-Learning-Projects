from utils.visualization import Visualizaton
import pandas as pd
from pathlib import Path

csv_path_data = Path(__file__).parent.parent / "data" / "telemetry_dzz_sem1.csv"
df = pd.read_csv(csv_path_data)

#print(df["mode"].unique()) ['standby', 'imaging', 'downlink', 'attitude_control']
#print(df[df["mode"]=='standby'].describe())
#print(df.groupby('mode')['temperature'].describe())
#print(df.groupby('mode').describe())

def analysis(df, column_for_analysis, sigma_value):
    mean = df[column_for_analysis].mean()
    std = df[column_for_analysis].std()
    new_series = (
            abs(df[column_for_analysis] - mean) > sigma_value * std
    )
    return new_series

df_s1 = df
df_s1["anomaly"] = (analysis(df, "temperature", 1)|
                    analysis(df, "voltage", 1)|
                    analysis(df, "current", 1)|
                    analysis(df, "angular_velocity", 1))

print(len(df_s1[df_s1['anomaly'] == True]))

df_s2 = df
df_s2["anomaly"] = (analysis(df, "temperature", 2)|
                    analysis(df, "voltage", 2)|
                    analysis(df, "current", 2)|
                    analysis(df, "angular_velocity", 2))

print(len(df_s2[df_s2['anomaly'] == True]))

df_s3 = df
df_s3["anomaly"] = (analysis(df, "temperature", 3)|
                    analysis(df, "voltage", 3)|
                    analysis(df, "current", 3)|
                    analysis(df, "angular_velocity", 3))

print(len(df_s3[df_s3['anomaly'] == True]))
