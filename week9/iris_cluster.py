import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.cluster import MeanShift, estimate_bandwidth

path = "../../data/iris_data.csv"

df = pd.read_csv(path, decimal=",")
df.drop(["Petal length", "Petal width"], axis=1, inplace=True)
print(df.head())

def plotTargetIris():
    labels = df["Species"].unique()
    plt.figure()
    for l in labels:
        members = (df["Species"] == l)
        x, y = df[members]["Sepal length"], df[members]["Sepal width"]

        plt.scatter(x, y)
    plt.show()

def plotEstimatedIris():
    df.drop("Species", axis=1, inplace=True)
    ms = MeanShift(bandwidth=estimate_bandwidth(df, quantile=0.2, n_samples=1000)).fit(df)
    labels = ms.labels_
    centers = ms.cluster_centers_
    labels_unique = np.unique(labels)

    plt.figure()
    for l in labels_unique:
        members = (labels == l)
        center = centers[l]
        x, y = df[members]["Sepal length"], df[members]["Sepal width"]

        plt.scatter(x, y)
        plt.scatter(center[0], center[1], c="k", s=100)
    plt.show()

#plotTargetIris()
plotEstimatedIris()
