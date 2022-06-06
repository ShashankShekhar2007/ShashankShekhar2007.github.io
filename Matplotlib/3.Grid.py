from matplotlib import pyplot as plt

# To get a grid
from matplotlib import style
style.use('ggplot')

title = "Grid"
x_label = "X-Axis"
y_label = "Y-Axis"


for n in range(0,7):
    x = []
    y = []

    for i in range(-10,11):
        list = [i, i*i, -i*i, i*i*i, -i*i*i, i*i*i*i, -i*i*i*i]
        x.append(i)
        y.append(list[n])
    plt.plot(x,y, label="Line 1", linewidth=3)

plt.title(title)
plt.xlabel(x_label)
plt.ylabel(y_label)
plt.legend()
plt.show()