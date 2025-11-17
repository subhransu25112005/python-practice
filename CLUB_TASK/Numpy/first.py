import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([[1, 2], [3, 4]])
arr = np.array([[1, 2, 3], [4, 5, 6]])

print(a)
print(b)
print(arr.shape)
print(arr.ndim)
print(arr.size)
print(arr.dtype)
print(arr[0])
print(arr[1:4])
print(arr[0,0])


arr = np.zeros((2, 3))
print(arr)

