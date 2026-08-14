import numpy as np

arr1 = np.arange(0, 52, 2)
arr2 = np.arange(100, 49, -2)

arr = np.concatenate((arr1, arr2))

print(np.sort(arr))
