import cv2
import matplotlib.pyplot as plt

image = cv2.imread('apple.jpg')

# Numpy Slicing: ROI 처리 기능
roi = image[350:500, 600:750]    # ROI: Region of Interest

# ROI 단위로 이미지 복사
image[0:150, 0:150] = roi

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()