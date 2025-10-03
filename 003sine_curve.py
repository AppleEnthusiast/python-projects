import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,2*np.pi,100)
y = np.sin(x)

plt.plot(x,y,label="f(x) = sin(x)")

plt.title("Sine Curve")
plt.legend()
plt.show()

