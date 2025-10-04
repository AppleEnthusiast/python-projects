import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(0,101,50)
y = np.random.randint(0,101,50)

plt.scatter(x,y,color="blue",label="Random Points")

plt.title("Scatter Plot with Random Points")
plt.xlabel("x-values")
plt.ylabel("y-values")
plt.grid(True)
plt.legend()
plt.show()
