import pandas as pd
import matplotlib.pyplot as plt

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

# Графики
name_x = "timestamp"
name_y = "temperature"
x = df[name_x]
y = df[name_y]

plt.scatter(x,y)
plt.xticks([])
plt.xlabel(name_x)
plt.ylabel(name_y)

plt.savefig(f"{name_y}_image.png")
plt.close()

name_x = "timestamp"
name_y = "voltage"
x = df[name_x]
y = df[name_y]

plt.scatter(x,y)
plt.xticks([])
plt.xlabel(name_x)
plt.ylabel(name_y)

plt.savefig(f"{name_y}_image.png")
plt.close()

name_x = "timestamp"
name_y = "current"
x = df[name_x]
y = df[name_y]

plt.scatter(x,y)
plt.xticks([])
plt.xlabel(name_x)
plt.ylabel(name_y)

plt.savefig(f"{name_y}_image.png")
plt.close()

name_x = "timestamp"
name_y = "angular_velocity"
x = df[name_x]
y = df[name_y]

plt.scatter(x,y)
plt.xticks([])
plt.xlabel(name_x)
plt.ylabel(name_y)

plt.savefig(f"{name_y}_image.png")
plt.close()

df_an = df[df["anomaly"] == True]

name_x = "timestamp"
name_y = "anomaly"
x = df[name_x]
y = df[name_y]

plt.scatter(x,y)
plt.xticks([])
plt.xlabel(name_x)
plt.ylabel(name_y)

plt.savefig(f"{name_y}_image.png")
plt.close()