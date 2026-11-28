import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets, model_selection
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics

data = pd.read_csv("Covid_data.csv")

print(data.shape)
print(data.head())

x = data.drop("Last_Update", axis = 1)

x = x.drop("Admin2", axis = 1)

x = x.drop("FIPS", axis = 1)

x = x.drop("Empty", axis = 1)

x = x.drop("OBJECTID", axis = 1)

x = x.drop("Province_State", axis = 1)

x = x.drop("Recovered", axis = 1)

x = x.drop("Combined_Key", axis = 1)

x = x.drop("Country_Region", axis = 1)

x = x.drop("Deaths", axis = 1)

x = x.drop("Active", axis = 1)

y = data["Combined_Key"]


print(x.head())
print(y.head())

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 1)

print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)

model = DecisionTreeClassifier(max_depth = 3, random_state = 1)
model.fit(x_train, y_train)

answers = model.predict([[ 50.0547,	5.4677,	30395]])
print(answers)