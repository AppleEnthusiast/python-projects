import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,50,100)
y1 = np.sqrt(x)
y2 = 1/200 * x**2

plt.plot(x,y1,label="f(x) = √x")
plt.plot(x,y2,label="g(x) = 1/200 * x^2")

plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.title("Square Root and Quadratic Function")
plt.grid(True)
plt.legend()
plt.show()

