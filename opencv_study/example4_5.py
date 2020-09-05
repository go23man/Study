import cv2
import matplotlib.pyplot as plt

image = cv2.imread('apple.jpg')
#BGR에서 R에 해당하는 부분에 대해 모두 0으로 처리함(빨간색 소멸)
image[:,:,2] = 0

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()