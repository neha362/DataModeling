import numpy as np
from scipy import stats
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86] #dataset
y = lambda x: [np.mean(x), np.median(x), stats.mode(x), np.std(x), np.var(x), np.percentile(x, 25), np.percentile(x, 50)]
print(y(speed))
import matplotlib.pyplot as plt

plt.subplot(2, 1, 1)
plt.hist([np.random.normal(10, 2, 10000), np.random.uniform(0, 5, 10000)], color = ["orchid", "rebeccapurple"])
plt.subplot(2, 1, 2)
x = np.random.uniform(0, 15, 15)
y = np.random.uniform(80, 110, 15)
slope, intercept, r, p, std_err = stats.linregress(x, y) #assigns values
myfunc = lambda x: slope * x + intercept
plt.scatter(x, y)
plt.plot(x, list(map(myfunc, x)))
plt.show()
print(r)
print(myfunc(10))

#polynomial regression
x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]
plt.scatter(x, y)
mymodel = np.poly1d(np.polyfit(x, y, 3))
myline = np.linspace(1, 22, 100) # start at point 1, end at point 100
plt.plot(myline, mymodel(myline))
plt.show()