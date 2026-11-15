import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error

df = pd.read_csv("https://raw.githubusercontent.com/HUSSAIN-004/cl1/2c7ac4db1afcacc82fd9b4afd95b489bcd039b88/data/uber.csv")
df = df.drop(["Unnamed: 0", "key"], axis=1, errors="ignore")

# preprocessing: remove missing values and extract time features
df = df.dropna()
df["pickup_datetime"] = pd.to_datetime(df["pickup_datetime"])
df["hour"] = df["pickup_datetime"].dt.hour
df["year"] = df["pickup_datetime"].dt.year
df = df.drop("pickup_datetime", axis=1)

# distance feature from coordinates (haversine)
lat1, lon1 = np.radians(df["pickup_latitude"]), np.radians(df["pickup_longitude"])
lat2, lon2 = np.radians(df["dropoff_latitude"]), np.radians(df["dropoff_longitude"])
a = np.sin((lat2 - lat1) / 2) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin((lon2 - lon1) / 2) ** 2
df["distance"] = 6371 * 2 * np.arcsin(np.sqrt(a))

# outlier removal using IQR on fare and distance, plus invalid coordinates
df = df[df["pickup_latitude"].between(-90, 90) & df["dropoff_latitude"].between(-90, 90)]
for col in ["fare_amount", "distance"]:
    q1, q3 = df[col].quantile(0.25), df[col].quantile(0.75)
    iqr = q3 - q1
    df = df[df[col].between(q1 - 1.5 * iqr, q3 + 1.5 * iqr)]

# correlation analysis
print(df.corr()["fare_amount"].sort_values(ascending=False))

X = df.drop("fare_amount", axis=1)
y = df["fare_amount"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

for name, model in [("Linear Regression", LinearRegression()),
                    ("Random Forest", RandomForestRegressor(n_estimators=50, n_jobs=-1))]:
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    print(name, "R2:", r2_score(y_test, pred),
          "RMSE:", np.sqrt(mean_squared_error(y_test, pred)))
