import cv2

# 카메라캡처 객체 생성('output.avi'라는 파일이 인자로 들어감)
cap = cv2.VideoCapture('output.avi')

# XVID는 사용할 코덱의 이름
fourcc = cv2.VideoWriter_fourcc(*'XVID')

while(True):
    # 객체로부터 이미지를 가져옴
    ret, img_color = cap.read()

    # 동영상을 끝까지 재생하면 무한루프 탈출
    if ret == False:
        break

    img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

    # 캡처된 이미지를 화면에 출력
    cv2.imshow("Color", img_color)
    cv2.imshow("Gray", img_gray)

    # ESC입력을 받으면 무한루프 탈출
    if cv2.waitKey(1)&0xFF == 27:   # 키보드 입력을 받기 위해 1초 대기시간
        break

# 비디오 캡처객체와 윈도우를 위한 자원을 메모리 해제
cap.release()   # 비디오를 닫거나 캡처활동 중단
cv2.destroyAllWindows()