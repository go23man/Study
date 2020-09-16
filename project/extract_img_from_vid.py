import cv2
from datetime import datetime

# 카메라캡처 객체 생성(두 대의 카메라를 사용하고 싶은 경우 인자가 다른 추가 객체 생성)
cap = cv2.VideoCapture(0)

# XVID는 사용할 코덱의 이름
fourcc = cv2.VideoWriter_fourcc(*'XVID')
# 동영상파일을 'output.avi'라는 파일이름으로 저장
# 코덱은 fourcc 사용, 초당 30프레임, 해상도는 int(cap.get(3)) * int(cap.get(4))
writer = cv2.VideoWriter('C:/Users/go23m/Documents/Hanium/vid_files/output.avi', fourcc, 30.0, (int(cap.get(3)), int(cap.get(4))))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    now = datetime.now()
    snow = str(now.year) + '_' + str(now.month) + '_' + str(now.day) + '_' + str(now.hour) + '_' + str(now.minute) + '_' + str(now.second)
    cv2.imshow("Gray", img_gray)
    cv2.imwrite('C:/Users/go23m/Documents/Hanium/vid_files/' + snow + '.jpg',img_gray)

    # 카메라로부터 받은 이미지를 반복적으로 저장하여 동영상 생성
    writer.write(img_gray)

    # ESC입력을 받으면 무한루프 탈출
    if cv2.waitKey(1)&0xFF == 27:   # 키보드 입력을 받기 위해 1초 대기시간
        break    

# 비디오 캡처객체와 윈도우를 위한 자원을 메모리 해제
cap.release()   # 비디오를 닫거나 캡처활동 중단
writer.release()
cv2.destroyAllWindows()