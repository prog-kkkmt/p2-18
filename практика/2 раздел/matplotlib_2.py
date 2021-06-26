import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

x = np.array([-3, -2, -1, 0.1, 1, 2, 3])
y = np.array([9, 4, 1, 0.1, 1, 4, 9])

ax.plot(x, y)

ax.plot(x, np.sin(x), color=(1.0,0.2,0.3), linestyle='-', marker='o')

ax.plot(x, x +5, color='blue', linestyle='--')

ax.plot(x, x + 3, color='g', linestyle=':', marker='^')

ax.plot(x, np.cos(x), color='0.75', linestyle='-.')

ax.plot(x, x, color='#FFDD44', linestyle='--', marker='*')

plt.show()
