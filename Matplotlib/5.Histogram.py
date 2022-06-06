from matplotlib import pyplot as plt

title = "Histogram"
x_label = "X-Axis"
y_label = "Y-Axis"

data = [0,1,4,5,6,7,8,11,12,15,16,18,9,20]
ranges = [0,5,10,15,20]

plt.hist(data, ranges, edgecolor = 'white')
plt.title(title)
plt.xlabel(x_label)
plt.ylabel(y_label)
plt.show()