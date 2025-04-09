import matplotlib.pyplot as plt
import numpy as np

# Scatter Plot displays points based on x and y values. Just dots not lines

x = np.random.randint(0,100, 60)
y = np.random.randint(0, 100, 60)

colors = np.random.rand(60)


plt.scatter(x, y, c=colors)

plt.show()
