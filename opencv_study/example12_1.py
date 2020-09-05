# KNN 알고리즘
# KNN은 비지도학습의 가장 간단한 예시중 하나로
# 다양한 레이블의 데이터 중에서 자신과 가장 근접한 데이터를 찾아
# 자신의 레이블을 결정하는 방식
import cv2
import numpy as np
from matplotlib import pyplot as plt

# 각 데이터의 위치: 25 * 2 크기에 각각 0 ~ 99
trainData = np.random.randint(0, 100, (25, 2)).astype(np.float32)
# 각 데이터는 0 or 1
response = np.random.randint(0, 2, (25, 1)).astype(np.float32)

# 값이 0인 데이터를 각각 (x, y) 위치에 빨간색으로 칠함
red = trainData[response.ravel() == 0]
plt.scatter(red[:, 0], red[:, 1], 80, 'r', '^')
# 값이 1인 데이터를 각각 (x, y) 위치에 파란색으로 칠함
blue = trainData[response.ravel() == 1]
plt.scatter(blue[:, 0], blue[:, 1], 80, 'b', 's')

# (0 ~ 99, 0 ~ 99) 위치의 데이터를 하나 생성해 칠함
newcomer = np.random.randint(0, 100, (1, 2)).astype(np.float32)
plt.scatter(newcomer[:, 0], newcomer[:, 1], 80, 'g', 'o')

# 객체 초기화
knn = cv2.ml.KNearest_create()
knn.train(trainData, cv2.ml.ROW_SAMPLE, response)       # 좌표와 레이블을 전달하여 모델을 훈련시킴
# trainData: 훈련시킬 모델
# cv2.ml.ROW_SAMPLE: 좌표
# response: 레이블
ret, results, neighbours, dist = knn.findNearest(newcomer, 3)

# 가까운 3개를 찾고, 거리를 고려하여 자신을 정함
print("result : ", results)         # 새로운 데이터가 1(파란색)으로 분류됨
print("neighbours :", neighbours)   # 근접한 데이터 3개의 색깔을 알려줌
print("distance: ", dist)           # 근접한 데이터의 거리

plt.show()