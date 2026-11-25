import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets, model_selection
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics


data = pd.read_csv("Iris.csv")
print(data.head())

x = data["Species"]

y1 = data["SepalLengthCm"]
y2 = data["SepalWidthCm"]
y3 = data["PetalLengthCm"]
y4 = data["PetalWidthCm"]


plt.subplot(2, 2, 1)
plt.scatter(x, y1)

plt.subplot(2, 2, 2)
plt.scatter(x, y2)

plt.subplot(2, 2, 3)
plt.scatter(x, y3)

plt.subplot(2, 2, 4)
plt.scatter(x, y4)

plt.show()

data["Species"] = data["Species"].replace({"setosa" : 0, "versicolor" : 1, "virginica" : 2})

y = data["Species"]

x = data.drop("Species", axis = 1)

x = x.drop("Id", axis = 1)

print(x.head())

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 1)
print(x_train.shape)
print(y_train.shape)

print(x_test.shape)
print(y_test.shape)

model = DecisionTreeClassifier(max_depth = 3, random_state = 1)
model.fit(x_train, y_train)

answers = model.predict( np.array([7.2,	2.8, 6.1, 2]).reshape(1, -1) )
print(answers)

#print("accuracy", metrics.accuracy_score(answers, y_test))