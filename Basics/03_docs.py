import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)

x = np.linspace(0, 10)
with plt.style.context('ggplot'):
    plt.plot(x, np.tan(x) + x + np.random.randn(50))
    plt.plot(x, np.tanh(x) + 2 * x + np.random.randn(50))
    plt.plot(x, np.tanh(x) + 3 * x + np.random.randn(50))
    plt.plot(x, np.tanh(x) + 4 * x + np.random.randn(50))
    plt.plot(x, np.tanh(x) + 5 * x + np.random.randn(50))
    plt.plot(x, np.tanh(x) + 6 * x + np.random.randn(50))
    plt.plot(x, np.tanh(x) + 7 * x + np.random.randn(50))
    plt.plot(x, np.tanh(x) + 8 * x + np.random.randn(50))
    # Number of accent colors in the color scheme
    plt.title('8 Random Lines - Line')
    plt.xlabel('x label', fontsize=14)
    plt.ylabel('y label', fontsize=14)

plt.show()