import numpy as np

# 각 열을 기준으로 정렬
array = np.array([[5, 9, 10, 3, 1], [8, 3, 4, 2, 5]])
print(array)
array.sort(axis=0)
print(array)