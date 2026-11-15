import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, ConfusionMatrixDisplay

# download emails.csv from kaggle.com/datasets/balaka18/email-spam-classification-dataset-csv
df = pd.read_csv("emails.csv")

# explore the data
print(df.shape)
print(df.head())
print("Missing values:", df.isnull().sum().sum())
print(df["Prediction"].value_counts())

# features = word counts, target = Prediction (1 = spam, 0 = not spam)
X = df.drop(["Email No.", "Prediction"], axis=1)
y = df["Prediction"]

# split into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# scale features (important for KNN and SVM)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# KNN model
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
knn_pred = knn.predict(X_test)

# SVM model
svm = SVC(kernel="linear")
svm.fit(X_train, y_train)
svm_pred = svm.predict(X_test)

# compare performance of both classifiers
results = []
for name, pred in [("KNN", knn_pred), ("SVM", svm_pred)]:
    print("\n=====", name, "=====")
    print("Accuracy :", accuracy_score(y_test, pred))
    print("Precision:", precision_score(y_test, pred))
    print("Recall   :", recall_score(y_test, pred))
    print("F1 score :", f1_score(y_test, pred))
    print("Confusion matrix:\n", confusion_matrix(y_test, pred))
    results.append([name, accuracy_score(y_test, pred)])
    ConfusionMatrixDisplay(confusion_matrix(y_test, pred)).plot()
    plt.title(name)
    plt.show()

print("\nComparison:\n", pd.DataFrame(results, columns=["Model", "Accuracy"]))