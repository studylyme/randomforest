import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score, classification_report, ConfusionMatrixDisplay

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/diabetes.csv")

# explore the data
print(df.shape)
print(df.head())
print(df.describe())
print("Missing values:\n", df.isnull().sum())
print(df["Outcome"].value_counts())

# zero values in these columns are not possible, treat them as missing and fill with mean
for col in ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]:
    df[col] = df[col].replace(0, np.nan)
    df[col] = df[col].fillna(df[col].mean())

X = df.drop("Outcome", axis=1)
y = df["Outcome"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# scale features because KNN uses distance
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# find the best K by testing values from 1 to 20
accuracies = []
for k in range(1, 21):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    accuracies.append(accuracy_score(y_test, knn.predict(X_test)))
plt.plot(range(1, 21), accuracies, marker="o")
plt.xlabel("K")
plt.ylabel("Accuracy")
plt.title("Accuracy for different K")
plt.show()
best_k = accuracies.index(max(accuracies)) + 1
print("Best K:", best_k)

# final model with best K
knn = KNeighborsClassifier(n_neighbors=best_k)
knn.fit(X_train, y_train)
pred = knn.predict(X_test)

# compute all required metrics
cm = confusion_matrix(y_test, pred)
tn, fp, fn, tp = cm.ravel()
acc = accuracy_score(y_test, pred)
print("\nConfusion matrix:\n", cm)
print("TP =", tp, "TN =", tn, "FP =", fp, "FN =", fn)
print("Accuracy  :", acc)
print("Error rate:", 1 - acc)
print("Precision :", precision_score(y_test, pred))
print("Recall    :", recall_score(y_test, pred))
print("F1 score  :", f1_score(y_test, pred))
print(classification_report(y_test, pred))
ConfusionMatrixDisplay(cm).plot()
plt.show()