import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([5, 6, 7, 10, 15, 2])
x2 = np.array([12, 34, 54, 67, 89, 100])
x3 = np.array([77, 66, 55, 44, 33, 22])
x4 = np.array([23, 45, 78, 86, 87, 95])
x5 = np.array([12, 24, 36, 48, 60, 72])
x6 = np.array([15, 30, 45, 60, 75, 90])


y1 = np.array([10, 20, 30, 40, 50, 60])

plt.subplot(2,3,1)
plt.scatter(x1, y1)

plt.subplot(2,3,2)
plt.scatter(x2, y1)

plt.subplot(2,3,3)
plt.scatter(x3, y1)

plt.subplot(2,3,4)
plt.scatter(x4, y1)

plt.subplot(2,3,5)
plt.scatter(x5, y1)

plt.subplot(2,3,6)
plt.scatter(x6, y1)

plt.show()