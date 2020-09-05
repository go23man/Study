import numpy as np

# 단일 객체 저장 및 불러오기
array = np.arange(0, 10)
np.save('saved.npy', array)

result = np.load('saved.npy')
print(result)