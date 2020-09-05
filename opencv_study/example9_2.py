import numpy as np

# 복수 객체 저장 및 불러오기
array1 = np.arange(0, 10)
array2 = np.arange(10, 20)
np.savez('saved.npz', array1=array1, array2=array2)

data = np.load('saved.npz')
result1 = data['array1']        # 이름 인덱스로 접근
result2 = data['array2']
print(result1)
print(result2)