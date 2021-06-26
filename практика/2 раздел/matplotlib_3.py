import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig, ax = plt.subplots()

N = 50

x = np.random.rand(N)
y = np.random.rand(N)

colors = np.random.rand(N)
area = (30 * np.random.rand(N))**2

fig = plt.figure(figsize=(10,6))

ax = fig.add_subplot(111, projection='3d')

ax.scatter(x, y, s=area, c=colors, alpha=0.5, marker='*', cmap='viridis')


plt.show()
