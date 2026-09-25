from utils.visualization import Visualization
import pandas as pd
from pathlib import Path

csv_path_data = Path(__file__).parent.parent / "data" / "telemetry_dzz_sem1.csv"
df = pd.read_csv(csv_path_data)

#print(df["mode"].unique()) ['standby', 'imaging', 'downlink', 'attitude_control']
#print(df[df["mode"]=='standby'].describe())
#print(df.groupby('mode')['temperature'].describe())
#print(df.groupby('mode').describe())

def analysis(df, column_for_analysis, std_value):
    mean = df[column_for_analysis].mean()
    std = df[column_for_analysis].std()
    new_series = (
            abs(df[column_for_analysis] - mean) > std_value * std
    )
    return new_series

df["anomaly_s1"] = (analysis(df, "temperature", 1)|
                    analysis(df, "voltage", 1)|
                    analysis(df, "current", 1)|
                    analysis(df, "angular_velocity", 1))

print(f"Кол-во аномалий в диапазоне от -std до std: {len(df[df['anomaly_s1'] == True])}")

df["anomaly_s2"] = (analysis(df, "temperature", 2)|
                    analysis(df, "voltage", 2)|
                    analysis(df, "current", 2)|
                    analysis(df, "angular_velocity", 2))

print(f"Кол-во аномалий в диапазоне от -2*std до 2*std: {len(df[df['anomaly_s2'] == True])}")

df["anomaly_s3"] = (analysis(df, "temperature", 3)|
                    analysis(df, "voltage", 3)|
                    analysis(df, "current", 3)|
                    analysis(df, "angular_velocity", 3))

print(f"Кол-во аномалий в диапазоне от -3*std до 3*std: {len(df[df['anomaly_s3'] == True])}")

df_diff = pd.DataFrame()
df_diff["timestamp"] = df["timestamp"]
df_diff["temperature_diff"] = df['temperature'].diff()
df_diff["voltage_diff"] = df['voltage'].diff()
df_diff["current_diff"] = df['current'].diff()
df_diff["angular_velocity_diff"] = df['angular_velocity'].diff()

path_to_save = Path(__file__).parent / "image"
v = Visualization(df_diff, path_to_save)
v.visual_all("timestamp")

def check_anomaly(row):
    if abs(row['temperature_diff']) > 5:
        return True
    elif abs(row['angular_velocity_diff'])> 0.5:
        return True
    elif abs(row['voltage_diff']) > 2:
        return True
    elif abs(row['current_diff']) > 1:
        return True
    return False

df["anomaly_diff"] = df_diff.apply(check_anomaly, axis=1)
print(f"Кол-во аномалий выявленных по diff: {len(df[df['anomaly_diff'] == True])}")
#print(df[(df["anomaly_diff"]==True) & (df["anomaly_s1"]==False)])

# Значения аномалий при std не коректно, потому-что не учтены режимы работы спутника mode
# При anomaly_diff нужно тоже учитывать режимы, ведь каждый переход от режима к режиму будет считаться аномалией
# Но при anomaly_diff эти ошибки можно пока что свести к погрешности

def analysis(df, columns_for_analysis, std_value):
    if isinstance(columns_for_analysis,str):columns_for_analysis = [columns_for_analysis]
    mean = df.groupby("mode")[columns_for_analysis].transform("mean")
    std = df.groupby("mode")[columns_for_analysis].transform("std")

    return ( (df[columns_for_analysis]-mean).abs() > (std_value * std) ).any(axis=1)


df["anomaly_s1"] = analysis(df,
                            ["temperature", "voltage", "current", "angular_velocity"],
                            1)

print(f"Кол-во аномалий в диапазоне от -std до std: {len(df[df['anomaly_s1'] == True])}")

df["anomaly_s2"] = analysis(df,
                            ["temperature", "voltage", "current", "angular_velocity"],
                            2)

print(f"Кол-во аномалий в диапазоне от -2*std до 2*std: {len(df[df['anomaly_s2'] == True])}")

df["anomaly_s3"] = analysis(df,
                            ["temperature", "voltage", "current", "angular_velocity"],
                            3)

print(f"Кол-во аномалий в диапазоне от -3*std до 3*std: {len(df[df['anomaly_s3'] == True])}")

print("\nКол-во аномальных строк, если хотя бы 2 и более параметра определенны аномальными:")

def analysis(df, columns_for_analysis, std_value):
    if isinstance(columns_for_analysis,str):columns_for_analysis = [columns_for_analysis]
    mean = df.groupby("mode")[columns_for_analysis].transform("mean")
    std = df.groupby("mode")[columns_for_analysis].transform("std")

    return ( (df[columns_for_analysis]-mean).abs() > (std_value * std) ).sum(axis=1) >= 2


df["anomaly_s1"] = analysis(df,
                            ["temperature", "voltage", "current", "angular_velocity"],
                            1)

print(f"Кол-во аномалий в диапазоне от -std до std: {len(df[df['anomaly_s1'] == True])}")

df["anomaly_s2"] = analysis(df,
                            ["temperature", "voltage", "current", "angular_velocity"],
                            2)

print(f"Кол-во аномалий в диапазоне от -2*std до 2*std: {len(df[df['anomaly_s2'] == True])}")

df["anomaly_s3"] = analysis(df,
                            ["temperature", "voltage", "current", "angular_velocity"],
                            3)

print(f"Кол-во аномалий в диапазоне от -3*std до 3*std: {len(df[df['anomaly_s3'] == True])}")