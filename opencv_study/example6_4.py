import cv2
import numpy as np
import matplotlib.pyplot as plt

image = np.full((512, 512, 3), 255, np.uint8)
image = cv2.putText(image, "Hello World", (0, 200), cv2.FONT_ITALIC, 2, (255, 0, 0))
# (0, 200): 텍스트 위치
# cv2.FONT_ITALIC: 글꼴
# 2: 폰트 스케일
# (255, 0, 0): 색깔

plt.imshow(image)
plt.show()