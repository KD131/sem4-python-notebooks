import random as rnd

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


def generate_babies(n):
    babies = []
    for i in range(n):
        height = rnd.randint(45,80)
        weight = rnd.randint(2500,13000)
        age = rnd.randint(0,12) # months
        babies.append((height, weight, age))

    return babies

def plot_babies(babies):
    np_babies = np.array(babies)
    x, y, z = np_babies[:,0], np_babies[:,1], np_babies[:,2]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.scatter(x, y, z, linewidth=0.2)

    plt.title("Babies")
    ax.set_xlabel("Height (cm)")
    ax.set_ylabel("Weight (g)")
    ax.set_zlabel("Age (months)")

    plt.show()

babies = generate_babies(20)
print(babies)
plot_babies(babies)
