import matplotlib.pyplot as plt
import numpy as np
plt.style.use('ggplot')
# Scatter Plot displays points based on x and y values. Just dots not lines

x = np.random.randint(0,1000, 60)
y = np.random.randint(0, 1000, 60)

colors = np.random.randint(0,1000,60)

area = (30 * np.random.rand(60))**2 

plt.scatter(x, y,s=area, c=colors, alpha=0.5)

plt.show()
