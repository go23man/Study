import numpy as np

array1 = np.arange(4).reshape(2, 2)     # (2 * 2)
array2 = np.arange(2)                   # (1 * 2)

array3 = array1 + array2
# 브로드캐스팅: 형태가 다른 배열을 연산할 수 있도록 배열의 형태를 동적으로 변환

print(array3)