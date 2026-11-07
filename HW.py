import pandas as pd

data = pd.read_csv("Iris.csv")
print(data)

print(data.head())

data = data.dropna()
print(data)

sum1 = data["SepalLengthCm"].sum()
print(sum1)


mean_answer = data["SepalLengthCm"].mean()
print(mean_answer)

median_answer = data["SepalLengthCm"].median()
print(median_answer)

mode_answer = data["SepalLengthCm"].mode()[0]
print(mode_answer)

print(data[data.duplicated(subset=['Id'])])

data = data.drop("Id", axis = 1)
print(data.head())

y = data["Species"]
print(y.head())

x = data.drop("Species", axis = 1)
print(x.head())

x.loc[1, "SepalWidthCm"] = 2.0
print(x.head())

for i in x.index:
    if x.loc[i, "PetalLengthCm"] < 1.4:
        x.loc[i, "PetalLengthCm"] = 1.4

print(x.head())

print(data.duplicated())


 
print(data[data.duplicated()])

print(data[data.duplicated(subset=['Species'])])