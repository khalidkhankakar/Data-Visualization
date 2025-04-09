import matplotlib.pyplot as plt

x = [2,3,5,6]
x1 = [2,3,5,6]
x2 = [4,9,25,36]
x3 = [8,27,125,216]

plt.plot(x, x, 'r--', label='y = x')         # Red dashed line
plt.plot(x, x2, 'b:', label='y = x²')        # Blue dotted line
plt.plot(x, x3, 'go-', label='y = x³')       # Green line with circles

# plt.plot(x, x, 'r--', x,x2, 'b:', x,x3, 'o')

plt.title('Excerise')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.legend()

plt.show()