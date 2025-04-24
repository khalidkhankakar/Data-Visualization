import numpy as np
import matplotlib.pyplot as plt

# Generate 100 random points
np.random.seed(42)  # for consistent results
x = np.random.rand(100)
y = np.random.rand(100)

# Size of points (scaled randomly)
sizes = 500 * np.random.rand(100)

# Colors based on y values (gradient effect)
colors = y

# Create scatter plot
plt.figure(figsize=(10, 6))

scatter = plt.scatter(x, y, 
                      c=colors,         # color map values
                      cmap='viridis',   # colormap style
                      s=sizes,          # size of points
                      alpha=0.6,        # transparency
                      edgecolors='purple', 
                      linewidths=0.8)

# Add title and axis labels
plt.title("Advanced Scatter Plot using NumPy", fontsize=14)
plt.xlabel("Random X")
plt.ylabel("Random Y")

# Add color bar to explain the color map
plt.colorbar(scatter, label='Color scale based on Y')

# Add grid
plt.grid(True, linestyle='--', alpha=0.5)

# Save the plot as an image
plt.savefig("scatter_advanced.png")

# Show the plot
plt.show()
