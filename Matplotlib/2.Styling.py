from matplotlib import pyplot as plt


title = "Coloured Lines"
x_label = "X-Axis"
y_label = "Y-Axis"

x = [0,3,7,9]
y = [0,2,1,8]

x2 = [1,3,5,9]
y2 = [9,6,4,3]

plt.plot(x,y, label="Line 1", linewidth=5)
plt.plot(x2,y2, label="Line 2", linewidth=5)
plt.title(title)
plt.xlabel(x_label)
plt.ylabel(y_label)
plt.legend()
plt.show()