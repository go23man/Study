from imageai import Detection
import cv2

modelpath = "C:/Users/go23m/Documents/Hanium/yolo.h5"

yolo = Detection.ObjectDetection()
yolo.setModelTypeAsYOLOv3()
yolo.setModelPath(modelpath)
yolo.loadModel()

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)

while True:
    ## read frames
    ret, img = cam.read()
    ## predict yolo
    img, preds = yolo.detectCustomObjectsFromImage(input_image=img, 
                      custom_objects=None, input_type="array",
                      output_type="array",
                      minimum_percentage_probability=70,
                      display_percentage_probability=False,
                      display_object_name=True)
    ## display predictions
    cv2.imshow("", img)
    ## press q or Esc to quit    
    if (cv2.waitKey(1) & 0xFF == ord("q")) or (cv2.waitKey(1)==27):
        break
## close camera
cam.release()
cv2.destroyAllWindows()