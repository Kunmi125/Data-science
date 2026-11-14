import matplotlib.pyplot as plt
import numpy as np

x = np.array([5, 10, 25, 30, 44, 57, 63, 76, 80, 90])
y = np.array([100, 90, 80, 70, 60, 50, 40, 30, 20, 10])

#Line graph

plt.plot(x,y, marker = "o", mec = "b", ms = 10)  # ms = marker size  mec = marker
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Test Data")
plt.grid()
plt.show()

#Scatter graph
plt.scatter(x, y)
plt.show()

#Bar graph

plt.bar(x,y)
plt.show()
plt.barh(x, y)
plt.show()

#Histograms

plt.hist(x)
plt.show()

x = np.random.normal(150, 5, 200)
print(x)
plt.hist(x)
plt.show()


# Piechart
array2 = np.array([17.9, 17.2, 4.2, 3.5, 3.1, 2.9, 2.6, 2.1, 1.8])
labels1 = ["India", "China", "US", "Indonesia", "Pakistan", "Nigeria", "Brazil", "Bangladesh", "Rushia" ]
plt.pie(array2, labels = labels1)
plt.legend()
plt.show()