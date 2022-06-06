from matplotlib import pyplot as plt

""" Ofiicial Website:- https://matplotlib.org/ """


title = "Title of Table"
x_label = "X-Axis"
y_label = "Y-Axis"

x = [0,3,4,6,7,9]
y = [0,2,1,6,5,8]

plt.plot(x,y)
plt.title(title)
plt.xlabel(x_label)
plt.ylabel(y_label)
plt.show()