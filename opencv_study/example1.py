import cv2

# 'phone.jpg'라는 사진파일을 컬러모드(투명한 부분 무시)로 읽어옴
img_basic = cv2.imread('apple.jpg', cv2.IMREAD_COLOR)
# 윈도우 창의 제목을 'Image Basic'으로 설정한 다음 img_basic을 출력
cv2.imshow('Image Basic', img_basic)
# 괄호 안에 0이 들어가서 무한 대기
cv2.waitKey(0)
# 'result1.png'라는 이름과 형식으로 img_basic을 파일형식으로 저장
cv2.imwrite('result1.png', img_basic)

# 선행 이미지창이 닫힌 후 회색계열 이미지창이 팝업됨
cv2.destroyAllWindows()

# img_basic을 GRAY 형태로 변환하겠다(cvt: convert)
img_gray = cv2.cvtColor(img_basic, cv2.COLOR_BGR2GRAY)
# 윈도우 창의 제목을 'Image Basic'으로 설정한 다음 img_gray을 출력
cv2.imshow('Image Basic', img_gray)
# 괄호 안에 0이 들어가서 무한 대기
cv2.waitKey(0)
# 'result1.png'라는 이름과 형식으로 img_basic을 파일형식으로 저장
cv2.imwrite('result2.png', img_gray)