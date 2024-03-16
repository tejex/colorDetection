import cv2
from util import getLimits
from PIL import Image
#First Computer Vision Project, Detecting the color yellow in the webcam, any object with the 
#color yellow will have its bounding box highlighted

webCam = cv2.VideoCapture(0)
yellow = [0,255,255] # yellow
while True:
    ret, frame = webCam.read()
    
    hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerLimit, upperLimit = getLimits(yellow)

    mask = cv2.inRange(hsvFrame,lowerLimit,upperLimit)

    #using the Pillow Library here we are converting the image from being a numpy Array into Pillow
    #just changing the format, because we will call another function below
    mask_ = Image.fromarray(mask)
    #we need to use pillow because we gotta grab the bounding box
    bbox = mask_.getbbox()
    print(bbox)
    if bbox is not None:
        x1,y1,x2,y2 = bbox
        cv2.rectangle(frame,(x1, y1),(x2,y2), (0,255,0),5)
        
    cv2.imshow("Frame", frame)

    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break
webCam.release()
cv2.destroyAllWindows()