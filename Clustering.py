#agglomerative clustering = bottom up approach --> start separate, then group
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

df = pd.read_csv("C:/Users/nehas/Downloads/data.csv")
X = df["Weight"]
y = df["CO2"]
z = df["Volume"]/25
plt.scatter(X, y, c = z, cmap = "magma")
plt.colorbar()
plt.show()

#ward linkage = through euclidean distance --> forms cluster based on distance between two points
data = list(zip(X, y))
linkage_data = linkage(data, method = 'ward', metric = 'euclidean')
dendrogram(linkage_data)
plt.show()

#same using sklearn
from sklearn.cluster import AgglomerativeClustering
hierarchical_cluster = AgglomerativeClustering(n_clusters = 2, affinity = "euclidean", linkage = "ward")
labels = hierarchical_cluster.fit_predict(data)
plt.scatter(X, y, c = labels, cmap = "PiYG")
plt.colorbar()
plt.show()
print(labels)
