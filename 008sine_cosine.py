import matplotlib.pyplot as plt
import numpy as np

N = 200

x = np.linspace(0,2*np.pi,N)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x,y1,label="sin(x)",color="blue")
plt.plot(x,y2,label="cos(x)",color="red")

plt.title("Sine and Cosine Curves")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid(True)
plt.legend()
plt.show()

