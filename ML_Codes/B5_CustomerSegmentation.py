import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.metrics import silhouette_score
from scipy.cluster.hierarchy import dendrogram, linkage

df = pd.read_csv("https://raw.githubusercontent.com/echu-vb/manufacturing-sales-analysis/d5d9296d41f1e43d0335b7c0f3dbcd87e88fe2fc/sales_data_sample.csv", encoding="latin1")

# explore the data
print(df.shape)
print(df.head())
print(df.info())
print("Missing values:\n", df.isnull().sum())

# choose numeric columns for clustering
features = ["QUANTITYORDERED", "PRICEEACH", "SALES"]
X = df[features]
print(X.describe())

# scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# elbow method: inertia (within-cluster sum of squares) for k = 1 to 10
inertia = []
for k in range(1, 11):
    km = KMeans(n_clusters=k, n_init=10, random_state=0)
    km.fit(X_scaled)
    inertia.append(km.inertia_)
    print("k =", k, "inertia =", round(km.inertia_, 2))
plt.plot(range(1, 11), inertia, marker="o")
plt.xlabel("Number of clusters (k)")
plt.ylabel("Inertia")
plt.title("Elbow method")
plt.show()

# silhouette score as a second check for the best k
for k in range(2, 8):
    labels = KMeans(n_clusters=k, n_init=10, random_state=0).fit_predict(X_scaled)
    print("k =", k, "silhouette =", round(silhouette_score(X_scaled, labels), 3))

# final K-Means with the k chosen from the elbow (change if your elbow is elsewhere)
k = 3
kmeans = KMeans(n_clusters=k, n_init=10, random_state=0)
df["Cluster"] = kmeans.fit_predict(X_scaled)
print("\nCustomers per cluster:\n", df["Cluster"].value_counts())
print("\nAverage values per cluster:\n", df.groupby("Cluster")[features].mean())

# plot the clusters
plt.scatter(df["QUANTITYORDERED"], df["SALES"], c=df["Cluster"])
plt.xlabel("Quantity ordered")
plt.ylabel("Sales")
plt.title("K-Means clusters")
plt.show()

# hierarchical clustering for comparison
plt.figure(figsize=(10, 5))
dendrogram(linkage(X_scaled[:100], method="ward"))
plt.title("Dendrogram (first 100 rows)")
plt.show()
hier = AgglomerativeClustering(n_clusters=k, linkage="ward")
df["HierCluster"] = hier.fit_predict(X_scaled)
print("\nHierarchical clusters:\n", df["HierCluster"].value_counts())