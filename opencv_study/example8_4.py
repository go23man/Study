import numpy as np

array1 = np.arange(16).reshape(4, 4)
print(array1)

# 10보다 작은 원소값들만 True가 삽입돼있음
array2 = array1 < 10
print(array2)

# True가 나온 원소들에 대해서만 100으로 대체함
array1[array2] = 100
print(array1)