# 이미지 변형
import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('apple.jpg')

# 행과 열 정보만 저장(전체 배열에서 1번째 인덱스까지가 행과 열)
height, width = image.shape[:2]

# x축에 대하여 50, y축에 대하여 10만큼 이동
M = np.float32([[1, 0, 50], [0, 1, 10]])
# 이미지의 위치를 변경하는 함수
dst = cv2.warpAffine(image, M, (width, height))
# M: 변환 행렬
# (width, height): Manual Size

plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.show()