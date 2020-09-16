# 201520853 유승형 edge detection
import numpy as np
import cv2
import os
from matplotlib import pyplot as plt
from scipy import ndimage
from datetime import datetime

# set directories and video file name into current date
now = datetime.now()
snow = str(now.year) + '_' + str(now.month) + '_' + str(now.day) + '_' + str(now.hour) + '_' + str(now.minute)
image_folder = 'C:/Users/go23m/Documents/Hanium/output_files/images'
image_folder2 = 'C:/Users/go23m/Documents/Hanium/output_files/ed_images'
video_name = 'C:/Users/go23m/Documents/Hanium/output_files/' + snow + '.avi'

images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
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
    cv2.imwrite(image_folder2 + '/' + str(num) + '.jpg', sobel_outimg)
    num += 1

images2 = [img for img in os.listdir(image_folder2) if img.endswith(".jpg")]
frame = cv2.imread(os.path.join(image_folder2, images2[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'XVID'), 1, (width,height))

for image in images2:
    video.write(cv2.imread(os.path.join(image_folder2, image)))

cv2.destroyAllWindows()
video.release()