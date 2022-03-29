from itertools import cycle
import matplotlib.pyplot as plt
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

plotTargetIris()
