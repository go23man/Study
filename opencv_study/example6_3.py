import cv2
import numpy as np
import matplotlib.pyplot as plt

image = np.full((512, 512, 3), 255, np.uint8)
# 배열형식으로 꼭지점 선언
points = np.array([[5, 5], [128, 258], [483, 444], [400, 150]])
image = cv2.polylines(image, [points], True, (0, 0, 255), 4)
# points: 꼭지점들
# True: 닫힌 도형 여부(여기서는 사각형이므로 닫힘)
# (0, 0, 255): 색깔
# 4: 두께

plt.imshow(image)
plt.show()