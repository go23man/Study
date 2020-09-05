import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('digits.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 세로로 50줄, 가로로 100줄로 사진을 나눔
cells = [np.hsplit(row, 100) for row in np.vsplit(gray, 50)]
x = np.array(cells)
print(x.shape)
# (50, 100, 20, 20) 출력
# 50 * 100 = 5000개의 이미지 데이터가 각각 (20 * 20) 크기의 데이터로 존재

# 각 (20 * 20) 크기의 사진을 1차원 배열로 나열함
train = x[:, :].reshape(-1, 400).astype(np.float32)
print(train.shape)
# (5000, 400) 출력
# 총 5000개의 데이터가 400이라는 크기를 가짐

# 0이 500개, 1이 500개, ... 로 총 5,000개가 들어가는 (1 * 5000) 배열을 생성
k = np.arange(10)       # k를 0부터 9까지 들어있는 리스트로 생성
train_labels = np.repeat(k, 500)[:, np.newaxis]
print(train_labels.shape)
# (5000, 1) 출력
# 총 5000개의 데이터가 레이블에 대한 정보(0, 1, 혹은 2인지...)를 담는 것을 확인

np.savez('trained.npz', train=train, train_labels=train_labels)

# 다음과 같이 하나씩 글자를 출력할 수 있음
plt.imshow(cv2.cvtColor(x[0, 0], cv2.COLOR_BGR2RGB))     # 첫 번째 행, 첫 번째 열에 대한 이미지 출력(숫자 0 출력)
plt.show()

# 다음과 같이 하나씩 글자를 저장
cv2.imwrite('test_0.png', x[0, 0])
cv2.imwrite('test_1.png', x[5, 0])
cv2.imwrite('test_2.png', x[10, 0])
cv2.imwrite('test_3.png', x[15, 0])
cv2.imwrite('test_4.png', x[20, 0])
cv2.imwrite('test_5.png', x[25, 0])
cv2.imwrite('test_6.png', x[30, 0])
cv2.imwrite('test_7.png', x[35, 0])
cv2.imwrite('test_8.png', x[40, 0])
cv2.imwrite('test_9.png', x[45, 0])
