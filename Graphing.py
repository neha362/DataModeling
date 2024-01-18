import math

import matplotlib
print(matplotlib.__version__)

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([x for x in range(-10, 10)])
ypoints = np.array([pow(x, 3) + 3 * x + 5 for x in range(-10, 10)])
x2 = np.array([-10, 10])
y2 = np.array([pow(x, 3) + 3 * x + 5 for x in [-10, 10]])
plt.subplot(2, 2, 1)
plt.plot(xpoints, ypoints) #plots points on the chart
plt.plot(x2, y2)
plt.plot(xpoints, ypoints, "o") #"shortcut string notation, makes rings
plt.plot(ypoints, marker = "*") #default x-points of 0, 1, 2,...
#markers can be "o", "*", ".", ",", "x", "X", "+", "P", "s", "D", "d". "p"...
plt.plot(np.array([pow(x, 2) for x in range(-20, 20)]), "o-m", ms = 2, mec = "y", mfc = "y") #shorthand = marker|line|color, ms = 'marker size"
plt.grid()
plt.title("AABBCC")
plt.suptitle("DDEEFF")
plt.subplot(2, 2, 2)
plt.title("scatter")
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])
plt.scatter(x, y, s = colors, c = colors, cmap = "Pastel1", alpha = .75)
plt.colorbar()
plt.grid()
plt.subplot(2, 2, 3)
plt.title("bar chart")
x = np.array(["A", "B", "C", "D"])
y = np.array([5, 2, 9, 3])
plt.bar(x, y, color = "DarkOrchid", width = .25) #plt.barh(x, y) makes it horizontal
plt.subplot(2, 2, 4)
x = np.random.normal(170, 10, 250) #mean, standard deviation, number of values
y = np.random.normal(160, 15, 250)
print(x, y)
plt.hist([x, y], color = ["Orchid", "Aquamarine"])
plt.title("histogram")
plt.show() #shows the chart
