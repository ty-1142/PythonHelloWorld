import numpy as np
import matplotlib.pyplot as plt


x = np.array([0,1,2,3,4,5,6])
y = np.array([10, -1, 2, 4, 6, 7, 8])

fig, ax = plt.subplot()

ax.plot(x,y, 'ro')
ax.set_title("Example scatter plot")
ax.set_xlabel("x")
ax.set_ylabel("x")

plt.show()

