# 201520853 유승형 edge detection
# Revised by 강윤호
import numpy as np
import cv2
import os
from matplotlib import pyplot as plt
from scipy import ndimage
from datetime import datetime

# 카메라캡처 객체 생성(두 대의 카메라를 사용하고 싶은 경우 인자가 다른 추가 객체 생성)
cap = cv2.VideoCapture(0)

# XVID는 사용할 코덱의 이름
fourcc = cv2.VideoWriter_fourcc(*'XVID')
# 동영상파일을 'output.avi'라는 파일이름으로 저장
# 코덱은 fourcc 사용, 초당 30프레임, 해상도는 int(cap.get(3)) * int(cap.get(4))
writer = cv2.VideoWriter('C:/Users/go23m/Documents/Hanium/output_files/output.avi', fourcc, 30.0, (int(cap.get(3)), int(cap.get(4))))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    now = datetime.now()
    snow = str(now.year) + '_' + str(now.month) + '_' + str(now.day) + '_' + str(now.hour) + '_' + str(now.minute) + '_' + str(now.second)
    cv2.imshow("Gray", img_gray)
    cv2.imwrite('C:/Users/go23m/Documents/Hanium/output_files/images/' + snow + '.png',img_gray)
    cv2.imwrite('C:/Users/go23m/Documents/Hanium/output_files/color_images/' + snow + '(2).png',frame)

    # 카메라로부터 받은 이미지를 반복적으로 저장하여 동영상 생성
    writer.write(frame)

    # ESC입력을 받으면 무한루프 탈출
    if cv2.waitKey(1)&0xFF == 27:   # 키보드 입력을 받기 위해 1초 대기시간
        break    

# 비디오 캡처객체와 윈도우를 위한 자원을 메모리 해제
cap.release()   # 비디오를 닫거나 캡처활동 중단
writer.release()
cv2.destroyAllWindows()

# set directories and video file name into current date
now = datetime.now()
snow = str(now.year) + '_' + str(now.month) + '_' + str(now.day) + '_' + str(now.hour) + '_' + str(now.minute)
image_folder = 'C:/Users/go23m/Documents/Hanium/output_files/images'
image_folder2 = 'C:/Users/go23m/Documents/Hanium/output_files/ed_images'
video_name = 'C:/Users/go23m/Documents/Hanium/output_files/' + snow + '.avi'

images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
num = 0

# input image (gray)
for image in images:
    inimg = plt.imread(os.path.join(image_folder, image))
    inimg = np.uint8(255*inimg)
    # plt.imshow(inimg, 'gray', vmin=0, vmax=255)
    # plt.show()

    # =============================================================================
    # # edge detection
    # =============================================================================
    x,y = inimg.shape
    edge = np.zeros(256)
    sobel1 = 1/4*np.array([[1,0,-1],
                           [2,0,-2],
                           [1,0,-1]])

    sobel2 = 1/4*np.array([[-1,-2,-1],
                           [0,0,0],
                           [1,2,1]])

    inimg_x = ndimage.convolve(inimg[:,:], sobel1)
    inimg_y = ndimage.convolve(inimg[:,:], sobel2)

    #x gradient 
    inimg_x = np.uint8(inimg_x)
    # plt.imshow(inimg_x, 'gray', vmin=0, vmax=255)
    # plt.show()

    #y gradient 
    inimg_y = np.uint8(inimg_y)
    # plt.imshow(inimg_y, 'gray', vmin=0, vmax=255)
    # plt.show()

    # sobel_inimg = abs(inimg_x) + abs(inimg_y)
    sobel_inimg = (inimg_x**2 + inimg_y**2)**0.5
    sobel_outimg = np.zeros([x,y])
    threshold = 5   

    for i in range(x):
        for j in range(y):
            if (sobel_inimg[i,j] >= threshold):
                sobel_outimg[i,j] = 0
            else:
                sobel_outimg[i,j] = 255

    sobel_outimg = np.float32(sobel_outimg)
    # plt.imshow(sobel_outimg, 'gray', vmin=0, vmax=255)
    # plt.show()
    cv2.imwrite(image_folder2 + '/' + str(num) + '.png', sobel_outimg)
    num += 1

images2 = [img for img in os.listdir(image_folder2) if img.endswith(".png")]
frame = cv2.imread(os.path.join(image_folder2, images2[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'XVID'), 1, (width,height))

for image in images2:
    video.write(cv2.imread(os.path.join(image_folder2, image)))

cv2.destroyAllWindows()
video.release()