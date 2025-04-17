import matplotlib.pyplot as plt

# Data for Line 1
x = [1, 2, 3, 4, 5,6]
y1 = [1, 4, 9, 16, 25,36]

# Data for Line 2
y2 = [2, 3, 5, 7, 11]

# Plot both lines

# method1
plt.plot(x, y1, label="Squares", color="red", marker='o')
plt.plot(x, y2, label="Primes", color="purple", linestyle='--', marker='x')

# method2
# plt.plot(x,y1, 'r--', x,y2, 'b:')

# Add labels and title
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Multiple Lines Example")

# Show legend
plt.legend()

# Show the plot
plt.show()
