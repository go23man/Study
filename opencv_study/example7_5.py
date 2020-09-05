import numpy as np

array1 = np.arange(4).reshape(1, 4)
array2 = np.arange(8).reshape(2, 4)

print(array1)
print(array2)

# 배열 형태 세로축으로 합치기
array3 = np.concatenate([array1, array2], axis=0)
# axis는 0으로 설정함으로써 아래쪽에 행이 합쳐지게 함

print(array3)