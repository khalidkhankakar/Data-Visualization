import matplotlib.pyplot as plt

x = [1, 2, 3, 4,5,6]
y = [1, 4, 9, 16, 25,36]

# line plot
# plt.plot(x, y)
# plt.title("Square Numbers")
# plt.xlabel("Value")
# plt.ylabel("Square of Value")
# plt.show()


plt.plot(x, y,'go',marker='+',
         mouseover=True,
           markersize=10, 
           linewidth=5, 
           linestyle=':', 
           color='blue',
           fillstyle='top')
           
plt.title("Square Numbers")
plt.xlabel("Value")
plt.ylabel("Square of Values")
plt.show()
plt.savefig('line_plot.png')