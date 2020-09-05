import numpy as np

array1 = np.arange(0, 8).reshape(2, 4)
array2 = np.arange(0, 8).reshape(2, 4)
array3 = np.concatenate([array1, array2], axis=0)
array4 = np.arange(0, 4).reshape(4, 1)              # (4 * 1)

print(array3 + array4)