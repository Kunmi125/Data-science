import matplotlib.pyplot as plt
import numpy as np

x = np.array([2020, 2021, 2022, 2023, 2024, 2025])
y = np.array([83.8, 204.8, 443.1, 42.1, 3.3, 1.7])

plt.bar(x,y)
plt.show()



yy = np.array([102.0, 93.8, 72.4, 60.6, 57.7, 45.0, 41.8, 37.5, 36.9, 36.0])
labels1 = ["France", "Spain", "US", "China", "Italy", "Turkey", "Mexico", "UK", "Japan", "Germany" ]
plt.pie(yy, labels = labels1)
plt.show()