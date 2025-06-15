import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



# Scatter plot
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 3, 5]

plt.scatter(x,y, color='red', s=12, marker='*')
plt.show()

sns.scatterplot(x=x, y=y, color='green', marker='+')
plt.show()

plt.plot(x, y, linestyle='-', color='blue', marker='+')
plt.show()

sns.lineplot(x=x, y=y)
plt.show()


cat = ['A', 'B', 'C', 'D']
val = [12,23,43,13]
colors = ['red', 'blue', 'green', 'yellow']
plt.bar(cat, val, color=colors)
plt.show()

sns.barplot(x=cat, y=val)
plt.show()


# Group chart

x = np.arange(5)
y1 = [23,4,5,1,3]
y2 = [4,5,6,7,8]
y3 = [5,6,7,8,9]

width = 0.2

plt.bar(x-width,y1, width, color='red')
plt.bar(x,y2,width ,color='blue')
plt.bar(x+width,y3,width, color='green')

plt.xticks(x, ['A', 'B', 'C', 'D','E'])
plt.show()


# stacked bar chart

x = np.arange(5)
y1 = np.array([23,4,5,1,3])
y2 = np.array([4,5,6,7,8])
y3 = np.array([5,6,7,8,9])

plt.bar(x, y1, color='red')
plt.bar(x, y2, bottom=y1, color='blue')
plt.bar(x, y3, bottom=y2+y1, color='green')
plt.show()

# box plot
data = np.random.normal(size=50)
plt.boxplot(data)
plt.show()


sns.boxplot(data=data, color='red')
plt.show()

# mutliple histogram

dist1 = np.random.normal(loc=0, scale=1, size=500)
dist2 = np.random.normal(loc=1, scale=1.5, size=500)
dist3 = np.random.normal(loc=2, scale=2, size=500)

plt.hist(dist1, color='red', alpha=0.5, label='dist1',bins=30)
plt.hist(dist2, color='green', alpha=0.5, label='dist2',bins=30)
plt.hist(dist3, color='blue', alpha=0.5, label='dist3',bins=30)

plt.legend()
plt.show()


# Histogram of Data
new_data = np.random.randn(1000)

plt.hist(new_data, bins=50, density=True,histtype='step', cumulative=True, color='red', alpha=0.5, label='Cumulative distribution')
plt.hist(new_data, bins=30, density=True, histtype='bar', color='green', alpha=0.5, label='Histogram')
plt.axvline(new_data.mean(), color='blue', linestyle='--', label='Mean')
plt.legend()
plt.show()

# histogram
hist_data = np.random.randn(100)
plt.hist(hist_data, bins=30)
plt.show()

# Heatmap

heatmap_data = pd.DataFrame({
    "A": np.random.randn(100),
    "B": np.random.randn(100),
    "C": np.random.randn(100),
})

corr = heatmap_data.corr()

sns.heatmap(corr, annot=True, cmap='rainbow')
plt.show()

iris_data = sns.load_dataset('iris')
sns.violinplot(x='species', y='petal_length', data=iris_data)
plt.show()

x1 = np.random.rand(50)
y1 = np.random.rand(50)

x2 = np.random.rand(50)
y2 = np.random.rand(50) + 1

x3 = np.random.rand(50)
y3 = np.random.rand(50) + 2

plt.scatter(x1, y1, marker='*', color='red')
plt.scatter(x2, y2, marker='+', color='green')
plt.scatter(x3, y3, marker='^', color='blue')
plt.show()


# joint plot
new_iris_data = sns.load_dataset('iris')
sns.jointplot(x='sepal_length', y='sepal_width', data=new_iris_data, kind='kde')
plt.show()

sns.pairplot(new_iris_data, hue='species')
plt.show()

# Multiple box plot
box1 = np.array([4,32,11,54,23])
box2 = np.array([3,4,5,2,3])
box3 = np.array([8,6,4,23,1])

all_boxes = [box1, box2, box3]
sns.boxplot(all_boxes)
plt.show()

# Draw the normal distribution histogram
normal_dist = np.random.normal(loc=50, scale=10, size=200)
plt.hist(normal_dist, bins=30)
plt.show()

sns.histplot(normal_dist, bins=30, kde=True)
plt.show()

sns.ecdfplot(normal_dist)
plt.show()

sns.kdeplot(normal_dist, color='red', fill=True)
plt.show()


labels = ['A', 'B', 'C', 'D']
size = [15, 30, 45, 10]

colors = ['red', 'blue', 'green', 'orange']

explode = (0.1, 0, 0, 0)  # only "explode" the 1st slice
plt.pie(size, explode=explode, labels=labels, colors=colors,autopct='%1.1f%%',shadow=True, startangle=140)
plt.show()

# Time series
dates = pd.date_range('2025-01-01', periods=100, freq='D')
values = np.sin(np.linspace(0,1,100)) + np.random.normal(scale=0.3, size=100)
df = pd.DataFrame({'Date': dates, 'Value': values})

plt.figure(figsize=(10, 5))

plt.plot(df['Date'], df['Value'], marker='o', linestyle='-', color='red')
plt.title('Time Series Data')
plt.xlabel('Date')
plt.ylabel('Value')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()


# 3d Square Graph
x = np.linspace(-5, stop=5, num=50)
y = np.linspace(-5, stop=5, num=50)

x, y = np.meshgrid(x, y)


z = np.sin(np.sqrt(x**2 + y**2))


fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')
# ax = fig.

ax.plot_surface(x, y, z, cmap='rainbow')
ax.set_xlabel('X axies')
ax.set_ylabel('Y axies')
ax.set_zlabel('Z axies')
ax.set_title('3d graph')
plt.show()


# Contour Graph
x = np.linspace(-4, stop=4, num=100)
y = np.linspace(-4, stop=4, num=100)

x, y = np.meshgrid(x, y)

z = np.sin(np.sqrt(x**2 + y**2))

plt.contour(x,y,z, levels=20, cmap='rainbow')
plt.colorbar()


plt.xlabel('X axies')
plt.ylabel('Y axies')
plt.title('Contour plot')
plt.show()
