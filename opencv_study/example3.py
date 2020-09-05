# 오브젝트를 배경으로부터 분리하기 위해 이진화를 사용하는 코드
import cv2

# 범위함수 정의(필요하지 않지만 트랙바 정의시 필요)
def nothing(x): 
    pass

cv2.namedWindow('Binary')
cv2.createTrackbar('threshold', 'Binary', 0, 255, nothing)
# 'threshold': 트랙바의 이름
# 'Binary': 적용할 윈도우의 이름
# 0, 255: 트랙바 범위
# nothing: 콜백함수(여기서는 없음)

# 초기값은 203으로 설정
cv2.setTrackbarPos('threshold', 'Binary', 203)

img_color = cv2.imread('red_ball.jpg', cv2.IMREAD_COLOR)

cv2.imshow('Color', img_color)
cv2.waitKey(0)

img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

cv2.imshow('Gray', img_gray)
cv2.waitKey(0)

while(True):
    # 현재 트랙바의 위치를 구해서 low에 저장
    low = cv2.getTrackbarPos('threshold', 'Binary')
    ret, img_binary = cv2.threshold(img_gray, low, 255, cv2.THRESH_BINARY_INV)
    # 'img_gray': 적용 파일
    # low: 임계값. 이 값을 기준으로 결과 이미지의 픽셀이 검은색 혹은 흰색이 됨
    # 255: 임계값 초과시 적용할 값
    # cv2.THRESH_BINARY_INV: thresholding 타입(현재는 반전형태)
    # low라는 임계값을 초과하면 흰색으로 보이고(255적용) 그 반대면 검정색으로 보임(0 적용)

    cv2.imshow("Binary", img_binary)
    # ESC키를 누르면 루프 탈출

    img_result = cv2.bitwise_and(img_color, img_color, mask = img_binary)
    # img_color: 첫번째 입력
    # img_color: 두번째 입력
    # img_binary: mask로 사용
    # img_color와 img_binary끼리 AND 연산
    cv2.imshow('Result', img_result)

    if cv2.waitKey(1)&0xFF == 27:
        break

cv2.destroyAllWindows()