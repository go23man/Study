import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('apple.jpg')

# 행과 열 정보만 저장
height, width = image.shape[:2]

# 이미지 회전을 위한 변환 행렬 생성
M = cv2.getRotationMatrix2D((width / 2, height / 2), 90, 0.5)
# (width / 2, height / 2): 회전 중심
# 90: 회전 각도
# 0.5: Scale Factor
print(M)
dst = cv2.warpAffine(image, M, (width, height))

plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.show()