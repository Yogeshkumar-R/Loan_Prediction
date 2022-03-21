import pandas as pd
import numpy as np
import matplotlib.pyplot
from sklearn.linear_model import LinearRegression

X = pd.read_csv("D:\college\Virtusa\california_housing_test.csv")
Y = pd.read_csv("D:\college\Virtusa\california_housing_train.csv")

X = X.values
Y = Y.values

model=LinearRegression()

model.fit(X,Y)
house_value=2
X_test=np.array()
X_test=X_test.reshape((1,-1))

model.predict(X_test)
