import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

df = pd.read_csv("https://raw.githubusercontent.com/sharmaroshan/Churn-Modelling-Dataset/master/Churn_Modelling.csv")
df = df.drop(["RowNumber", "CustomerId", "Surname"], axis=1)
df = pd.get_dummies(df, drop_first=True)   # encode Geography and Gender

X = df.drop("Exited", axis=1)
y = df["Exited"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# normalize features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# build neural network and optimize it by searching hyperparameters
params = {"hidden_layer_sizes": [(8,), (16, 8)], "alpha": [0.0001, 0.01]}
model = GridSearchCV(MLPClassifier(max_iter=300, random_state=0), params, cv=3)
model.fit(X_train, y_train)
print("Best parameters:", model.best_params_)

pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, pred))
print(confusion_matrix(y_test, pred))
