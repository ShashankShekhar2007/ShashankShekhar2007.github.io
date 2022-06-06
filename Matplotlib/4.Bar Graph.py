from matplotlib import pyplot as plt

title = "Bar Graph"
x_label = "X-Axis"
y_label = "Y-Axis"

x = [1,3,5,7,9,11]
y = [0.5,2,1,6,5,7]

x2 = [2,4,6,8,10,12]
y2 = [1,3,4,5,2,8]

plt.bar(x,y)
plt.bar(x2,y2)

plt.title(title)
plt.xlabel(x_label)
plt.ylabel(y_label)
plt.show()