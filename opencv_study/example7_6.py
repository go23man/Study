# 배열 나누기
import numpy as np

array = np.arange(8).reshape(2, 4)
# 좌우로 분할하는 함수
left, right = np.split(array, [2], axis=1)
# [2]: 분할 기준이되는 인덱스
# axis: 분할을 행 혹은 열 기준으로 할 것인가를 정함(여기서는 열)

print(left.shape)
print(right.shape)
print(array)
print(left)