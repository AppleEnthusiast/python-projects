import matplotlib.pyplot as plt
import numpy as np

N = 50

x = np.random.randint(0,100,N)
y = np.random.randint(0,100,N)

colors = np.random.rand(N)
sizes = np.random.randint(20,100,N)

plt.scatter(x,y,c=colors,s=sizes,cmap="viridis",alpha=0.8,edgecolors=None)

plt.title("Scatter Plot with Random Colors and Sizes")
plt.xlabel("x-values")
plt.ylabel("y-values")
plt.grid(True)
plt.colorbar(label="viridis")
plt.show()

