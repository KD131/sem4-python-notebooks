import random as rnd

import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from mpl_toolkits.mplot3d import Axes3D


def generate_babies(n):
    babies = []
    for i in range(n):
        height = rnd.randint(45,80)
        weight = rnd.randint(2500,13000)
        age = rnd.randint(0,12) # months
        babies.append((height, weight, age))

    return babies

def gen_babies_realistic(n):
    # Uses sklearn.preprocessing.MinMaxScaler to normalise and scale.
    # It would've been easier to just define my own norm and denorm functions.
    # All the needless matrices would be replaces by just a min-max pair.
    babies = []
    age_min = 0
    age_max = 12
    scaler_age = MinMaxScaler()
    scaler_age.fit([[age_min], [age_max]])  # an np.array can also use .reshape(-1, 1) to infer rows and transform to 1 column
                                            # i.e. np.arange(age_min, age_max).reshape(-1, 1),
                                            # or just np.array([age_min, age_max]).reshape(-1 ,1)
    scaler_height = MinMaxScaler()
    scaler_height.fit([[45], [80]])
    scaler_weight = MinMaxScaler().fit([[2500], [13000]]) # chain to save space

    for i in range(n):
        age = rnd.randint(age_min, age_max) # months
                                            # could've packed min,max as a tuple or list, and then used randint(*age_range) (the * unpacks)
        age_nrm = scaler_age.transform([[age]])[0][0]   # this is so clunky because it has to take and return a matrix
        variance = rnd.uniform(0.85, 1.15)
        height = scaler_height.inverse_transform([[age_nrm]])[0][0] * variance
        weight = scaler_weight.inverse_transform([[age_nrm]])[0][0] * variance
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

# babies = generate_babies(20)
babies = gen_babies_realistic(20)
print(babies)
plot_babies(babies)
