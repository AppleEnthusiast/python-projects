import matplotlib.pyplot as plt
import numpy as np

x = np.arange(11)
y = x ** 2

plt.scatter(x,y,label="f(x) = x^2")
plt.title("Scatter Plot")
plt.legend()
plt.show()

