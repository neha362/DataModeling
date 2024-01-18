import pandas
df = pandas.read_csv("C:/Users/nehas/OneDrive/Desktop/Important Stuff/Programs/Python/DataModeling/drug200.csv")
print(df)
sex = {"F": 0, "M": 1}
bp = cholesterol = {"HIGH": 1, "LOW": -1, "NORMAL": 0}
drug = {"drugA": 0, "drugB": 1, "drugC": 2, "drugX": 3, "drugY": 4}
df["Sex"] = df["Sex"].map(sex) #replaces categorical with quantitative using dictionaries
df["BP"] = df["BP"].map(bp)
df["Cholesterol"] = df["Cholesterol"].map(cholesterol)
df["Drug"] = df["Drug"].map(drug)
print(df)

features = ["Age", "Sex", "BP", "Cholesterol", "Na_to_K"]
X = df[features]
y = df["Drug"]
print(X)
print(y)

from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y) # creates a data model
tree.plot_tree(dtree, feature_names = features)
plt.show()

print(dtree.predict([[33, 1, -1, 1, 8]]))