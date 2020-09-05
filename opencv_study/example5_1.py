# 이미지 확대/축소
import cv2
import matplotlib.pyplot as plt

image = cv2.imread('apple.jpg')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()

expand = cv2.resize(image, None, fx=2.0, fy=2.0, interpolation=cv2.INTER_CUBIC)
# None: Manual Size
# fx: 가로 비율
# fy: 세로 비율
# interpolation: 보간법
# -INTER_CUBIC: 사이즈를 크게 할 때 주로 사용
# -INTER_AREA: 사이즈를 작게 할 때 주로 사용
plt.imshow(cv2.cvtColor(expand, cv2.COLOR_BGR2RGB))
plt.show()

shrink = cv2.resize(image, None, fx=0.8, fy=0.8, interpolation=cv2.INTER_AREA)
plt.imshow(cv2.cvtColor(shrink, cv2.COLOR_BGR2RGB))
plt.show()