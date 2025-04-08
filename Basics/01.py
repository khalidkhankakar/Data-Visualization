import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [1, 4, 9, 16]

# line plot
plt.plot(x, y)
plt.title("Square Numbers")
plt.xlabel("Value")
plt.ylabel("Square of Value")
plt.show()

plt.plot(x, y, linewidth=5, linestyle='dashed', color='green')
plt.show()