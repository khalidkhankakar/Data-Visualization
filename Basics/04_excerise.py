import matplotlib.pyplot as plt

x = [2,3,5,6,7]
x1 = [2,3,5,6,7]
x2 = [4,9,25,36,49]
x3 = [8,27,125,216,349]

plt.plot(x, x, 'r--', label='y = x')         # Red dashed line
plt.plot(x, x2, 'b:', label='y = x²')        # Blue dotted line
plt.plot(x, x3, 'go-', label='y = x³')       # Green line with circles

# plt.plot(x, x, 'r--', x,x2, 'b:', x,x3, 'o')

# Custom y-axis ticks
plt.xticks([0,1,2,3,4,5,6], ['Zero','One', 'Two', 'Three','Four', 'Five', 'Six','Seven'])

plt.title('Excerise of Matplotlib')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.legend()

plt.show()