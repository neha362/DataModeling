import pandas as pd
#multiple regression
df = pd.read_csv("C:/Users/nehas/Downloads/data.csv")
X = df[["Weight", "Volume"]] #list of independent variables
y = df["CO2"] #list of dependent variables

from sklearn import linear_model
regr = linear_model.LinearRegression()
regr.fit(X, y) #fills regression object with data fitting the relationship
print(regr.predict([[2300, 1300]])) #for weight, volume
print(regr.coef_) #coefficient of the regression object) --> partial derivatives evaluated at the point

from sklearn.preprocessing import StandardScaler
scaledX = StandardScaler().fit_transform(X) #standardizes through z-scores
print(scaledX)

#logistic regression
