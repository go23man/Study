import cv2
import numpy as np
import matplotlib.pyplot as plt

image = np.full((512, 512, 3), 255, np.uint8)
image = cv2.rectangle(image, (20, 20), (255, 255), (255, 0, 0), 10)
# (20, 20): 시작 좌표(상단 좌측 꼭지점)
# (255, 255): 종료 좌표(하단 우측 꼭지점)
# (255, 0, 0): 색깔
# 10: 선의 두께(-1이면 안이 채워짐)

plt.imshow(image)
plt.show()