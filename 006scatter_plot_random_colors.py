import matplotlib.pyplot as plt
import numpy as np

N = 50

x = np.random.randint(0,100,N)
y = np.random.randint(0,100,N)

colors = np.random.rand(N)

plt.scatter(x,y,c=colors,cmap="viridis")

plt.title("Scatter Plot with Colors")
plt.xlabel("x-values")
plt.ylabel("y-values")
plt.colorbar(label="Color Bar")
plt.show()

