import cv2
import matplotlib.pyplot as plt

image = cv2.imread('gray_image.jpg')
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(image_gray, 127, 255, 0)

plt.imshow(cv2.cvtColor(thresh, cv2.COLOR_GRAY2RGB))
plt.show()

# Contour 발견
contours = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0]
# cv2.RETR_TREE: mode(여기서는 모든 선을 찾으며, 모든 Hierarchy를 구성)
# cv2.CHAIN_APPROX_SIMPLE: method(여기서는 Contour Line을 그릴 수 있는 포인트만 저장)

# Contours 그리기
image = cv2.drawContours(image, contours, -1, (0, 255, 0), 4)
# -1: contour index(여기서는 모든 Contour 다 그림)
# (0, 255, 0): 색깔
# 4: thickness

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()