# 블러처리
import cv2
import numpy as np
import matplotlib.pyplot as plt

# 이미지 불러옴
image = cv2.imread('gray_image.jpg')
# 이미지를 RGB로 변환
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
# 이미지 출력
plt.show()

"""
1/16 1/16 1/16 1/16
1/16 1/16 1/16 1/16
1/16 1/16 1/16 1/16
1/16 1/16 1/16 1/16
"""

size = 4
# 1로 이루어진 float32객체의 4*4 배열을 생성한 다음에 16으로 나누어줌
kernel = np.ones((size, size), np.float32) / (size ** 2)
print(kernel)

# 간단히 이미지 모든 픽셀에 대해서 필터를 처리하는 함수라고 보면됨
dst = cv2.filter2D(image, -1, kernel)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.show()