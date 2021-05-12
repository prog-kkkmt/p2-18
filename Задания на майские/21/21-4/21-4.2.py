# Выполнил Кузнецов М. С. П2-18.

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

x = np.arange(8)
y = np.random.randint(0, 10, 8)
y2 = y + np.random.randint(0, 3, 8)
y3 = y2 + np.random.randint(0, 3, 8)
y4 = y3 + np.random.randint(0, 3, 8)
y5 = y4 + np.random.randint(0, 3, 8)
clr = ['#4bb2c5', '#c5b47f', '#EAA228', '#579575', '#839557', '#958c12', '#953579', '#4b5de4']
fig = plt.figure()
ax = Axes3D(fig)
ax.bar(x, y, 0, zdir='y', color=clr)
ax.bar(x, y2, 10, zdir='y', color=clr)
ax.bar(x, y3, 20, zdir='y', color=clr)
ax.bar(x, y4, 30, zdir='y', color=clr)
ax.bar(x, y5, 40, zdir='y', color=clr)
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
ax.view_init(elev=40)
plt.show()
