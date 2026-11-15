import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, ConfusionMatrixDisplay

df = pd.read_csv("https://raw.githubusercontent.com/sharmaroshan/Churn-Modelling-Dataset/master/Churn_Modelling.csv")

# explore the data
print(df.shape)
print(df.head())
print(df.info())
print("Missing values:\n", df.isnull().sum())
print(df["Exited"].value_counts())

# drop columns that do not help prediction
df = df.drop(["RowNumber", "CustomerId", "Surname"], axis=1)

# encode text columns Geography and Gender as numbers
df = pd.get_dummies(df, columns=["Geography", "Gender"], drop_first=True)
print(df.head())

# split into features and target
X = df.drop("Exited", axis=1)
y = df["Exited"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
print("Train size:", X_train.shape, "Test size:", X_test.shape)

# normalize features so all are on the same scale
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# build a basic neural network: 2 hidden layers
model = MLPClassifier(hidden_layer_sizes=(16, 8), activation="relu", max_iter=300, random_state=0)
model.fit(X_train, y_train)
pred = model.predict(X_test)
print("\nBasic model accuracy:", accuracy_score(y_test, pred))

# training loss curve
plt.plot(model.loss_curve_)
plt.xlabel("Iteration")
plt.ylabel("Loss")
plt.title("Training loss")
plt.show()

# optimize the model: try different sizes and learning rates
params = {"hidden_layer_sizes": [(8,), (16, 8), (32, 16)],
          "alpha": [0.0001, 0.001, 0.01],
          "learning_rate_init": [0.001, 0.01]}
grid = GridSearchCV(MLPClassifier(max_iter=300, random_state=0), params, cv=3)
grid.fit(X_train, y_train)
print("\nBest parameters:", grid.best_params_)

# evaluate the optimized model
best = grid.best_estimator_
pred = best.predict(X_test)
print("Optimized model accuracy:", accuracy_score(y_test, pred))
print("Confusion matrix:\n", confusion_matrix(y_test, pred))
print(classification_report(y_test, pred))
ConfusionMatrixDisplay(confusion_matrix(y_test, pred)).plot()
plt.show()