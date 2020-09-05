import cv2
image = cv2.imread('apple.jpg')

# 픽셀 수 및 이미지 크기 확인
print(image.shape)
print(image.size)

# 이미지 Numpy 객체의 특정 픽셀을 가리킴
# x축 100, y축 100을 가리킴
px = image[100, 100]

# B, G, R 순서로 출력
# (단, Gray Scale인 경우에는 B, G, R로 구분되지 않음)
print(px)

# R 값(2번째 인덱스)만 출력
print(px[2])

"""
    (2192, 2418, 3)     2192는 높이, 2418은 너비
    15900768            이미지의 크기
    [249 245 244]
    244
"""