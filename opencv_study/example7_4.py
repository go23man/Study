# 배열 형태 바꾸기
import numpy as np

array1 = np.array([1, 2, 3, 4])
# 2 * 2 행렬로 바뀜
array2 = array1.reshape((2, 2))

print(array2)