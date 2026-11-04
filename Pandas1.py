import pandas as pd

data1 = pd.read_csv("data.csv")
'''print(data1.shape)
print(data1.head())
print(data1.tail())
data1 = data1.drop(columns = ["Calories"])
print(data1)
print(data1.dtypes)
data1 = data1.dropna()
print(data1)
data1 = data1.fillna(value = 0)
print(data1)'''

sum1= data1["Maxpulse"].sum()
print(sum1)

all_sums = data1.sum(numeric_only=True)
print(all_sums)