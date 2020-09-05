# 특정 범위 픽셀 변경
import cv2
import time

image = cv2.imread('apple.jpg')

# 개별적인 픽셀 일일히 접근해서 수정(수행이 느릴 수도 있음)
start_time = time.time()
for i in range(0, 100):         # 행
    for j in range(0, 100):     # 열
        image[i, j] = [255, 255, 255]
print("--- %s seconds ---" % (time.time() - start_time))

# 범위를 지정한 다음, 범위를 동일한 값으로 채워넣음(처리속도가 더 월등)
# Numpy Slicing
start_time = time.time()
image[0:100, 0:100] = [0, 0, 0]
print("--- %s seconds ---" % (time.time() - start_time))