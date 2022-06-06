from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
from scipy.interpolate import make_interp_spline

style.use('ggplot')

title = "Equation Representation"
x_label = "X-Axis"
y_label = "Y-Axis"

x_coordinates = []
y_coordinates = []

inp = input(str("Enter equation: "))
min_input = int(input("Enter Minimum Value ="))
max_input = int(input("Enter Maximum Value ="))
for i in range(min_input, max_input):
    x = i
    x_coordinates.append(i)
    y_coordinates.append(eval(inp))


x_array = np.array(x_coordinates)
x_y_spline = make_interp_spline(x_coordinates, y_coordinates)
x = np.linspace(x_array.min(), x_array.max(), 500)
y = x_y_spline(x)

ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')

print(x_coordinates)
print(y_coordinates)
plt.plot(x,y, label="Line 1", linewidth=3)

plt.title(title)
plt.xlabel(x_label)
plt.ylabel(y_label)
plt.legend()
plt.show()