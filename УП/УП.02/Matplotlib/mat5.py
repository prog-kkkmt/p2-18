from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
fig = plt.figure()
ax = Axes3D(fig)
triangle = [((0.8,0.5,0), (0.5,0,0), (0.5, 0.5, 1))]
ax.add_collection(Poly3DCollection(triangle))
plt.show()