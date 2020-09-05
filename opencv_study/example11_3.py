# Gaussian Blur

import matplotlib.pyplot as plt
import cv2

image = cv2.imread('gray_image.jpg')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()

# kernel_size: 홀수
dst = cv2.GaussianBlur(image, (5, 5), 0)        # 홀수 크기의 배열
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.show()

# 블러링의 강도를 높이고 싶으면 size를 키우면 됨