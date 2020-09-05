import numpy as np

array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
# 배열을 합침
array3 = np.concatenate([array1, array2])

# 배열의 크기 출력
print(array3.shape)
print(array3)