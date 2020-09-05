import cv2
import numpy as np
import matplotlib.pyplot as plt

image = np.full((512, 512, 3), 255, np.uint8)
# (512, 512, 3): 512 * 512크기의 3가지 색깔을 가지는
# 255: 모든값을 255로 초기화
# np.uint8: 8비트로
image = cv2.line(image, (0, 0), (255, 255), (255, 0, 0), 10)
# (0, 0): 시작 좌표
# (255, 255): 종료 좌표
# (255, 0, 0): 색깔(RGB)
# 3: 선의 두께

plt.imshow(image)
plt.show()