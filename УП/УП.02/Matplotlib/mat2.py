import matplotlib.pyplot as plt
import numpy as np
n = np.linspace(0, 2, 100) # 100 чисел в интервале [0, 2]
fig, ax = plt.subplots()
ax.plot(n, n, label="linear") # 1 график
ax.plot(n, n**2, label="quadratic") # 2 график
ax.plot(n, n**3, label="cubic") # 3 график
ax.set_xlabel("x label")
ax.set_ylabel("y label")
ax.set_title("Simple Plot")
ax.legend()
plt.show()