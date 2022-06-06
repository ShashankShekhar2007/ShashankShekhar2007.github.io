from matplotlib import pyplot as plt
import random
title = "Histogram"
x_label = "X-Axis"
y_label = "Y-Axis"
data = []
for i in range(0,50):
    num = random.randint(0,100)
    data.append(num)
ranges = [0,10,20,30,40,50,60,70,80,90,100]
print(data)
plt.hist(data, ranges, edgecolor = 'white')
plt.title(title)
plt.xlabel(x_label)
plt.ylabel(y_label)
plt.show()