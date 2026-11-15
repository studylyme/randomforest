import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

df = pd.read_csv("https://raw.githubusercontent.com/echu-vb/manufacturing-sales-analysis/d5d9296d41f1e43d0335b7c0f3dbcd87e88fe2fc/sales_data_sample.csv", encoding="latin1")
X = df[["QUANTITYORDERED", "PRICEEACH", "SALES"]]
X = StandardScaler().fit_transform(X)

# elbow method: inertia for k = 1 to 10
inertia = []
for k in range(1, 11):
    inertia.append(KMeans(n_clusters=k, n_init=10, random_state=0).fit(X).inertia_)
plt.plot(range(1, 11), inertia, marker="o")
plt.xlabel("Number of clusters")
plt.ylabel("Inertia")
plt.show()

# final clustering with the k chosen from the elbow
kmeans = KMeans(n_clusters=3, n_init=10, random_state=0)
df["Cluster"] = kmeans.fit_predict(X)
print(df["Cluster"].value_counts())
