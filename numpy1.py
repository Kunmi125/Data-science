import numpy as np

array1 = np.array([56, 6, 12, 98, 4, 6])
print(array1)
print(array1.ndim)

array2 = np.array([[56, 6, 12], [98, 4, 6]])
array5 = np.array([[54, 76, 94], [73, 19, 53]])

print(array2)
print(array2.ndim)
array3 = array2.reshape((6, 1))
print(array3)

array4 = array2.reshape((3, 2, 1))
print(array4)
print(array4.ndim)
print(array4.shape)

print(array1[2])

print(array2[0, 0])

print(array4[2, 1, 0])

combined_array = np.concatenate((array2, array5), axis = 0)
print(combined_array)