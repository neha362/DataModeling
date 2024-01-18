import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

numpy.random.seed(2)
x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100)/x
colors = numpy.random.uniform(0, 100, 100)
plt.scatter(x, y, c = colors, s = colors, cmap = "magma")
plt.colorbar()
plt.grid()
plt.show()

train_x = x[:80] #the first 80% of the original data
train_y = y[:80]
test_x = x[80:] #the last 20% of the original data
test_y = y[80:]
plt.subplot(2, 1, 1)
plt.scatter(train_x, train_y, c = colors[:80], cmap = "autumn")
plt.subplot(2, 1, 2)
plt.scatter(test_x, test_y, c = colors[:20], cmap = "summer")
mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4)) #4-degree polynomial
myline = numpy.linspace(0, 6, 100)
plt.subplot(2, 1, 1)
plt.plot(myline, mymodel(myline))
plt.subplot(2, 1, 2)
plt.plot(myline, mymodel(myline)) #draw data model
plt.show()
print(r2_score(train_y, mymodel(train_x))) #calculates r^2 value
print(r2_score(test_y, mymodel(test_x)))
print("5 -> " + str(mymodel(5)))

#confusion matrix
actual = numpy.random.binomial(1, .9, size = 1000)
predicted = numpy.random.binomial(1, .9, size = 1000)
from sklearn import metrics
confusion_matrix = metrics.confusion_matrix(actual, predicted) #constructs the matrix
cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels = [False, True])
cm_display.plot()
plt.show()

#accuracy = (true positive + true negative)/total
print(metrics.accuracy_score(actual, predicted))
#precision = true positive/(all determined positive)
print(metrics.precision_score(actual, predicted))
#sensitivity = true positive/(all actual positive)
print(metrics.recall_score(actual, predicted))
#specificity = true negative/(all actual negative)
print(metrics.recall_score(actual, predicted, pos_label = 0))
#f-score = 2 * precision * sensitivity/(precision + sensitivity) --> harmonic mean of precision and sensitivity
print(metrics.f1_score(actual, predicted))