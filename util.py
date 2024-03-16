import numpy as np
import cv2

def getLimits(color):
    ourColor = np.uint8([[color]])

    hsvColor = cv2.cvtColor(ourColor,cv2.COLOR_BGR2HSV)

    lowerLimit = hsvColor[0][0][0] - 10, 100, 100
    upperLimit = hsvColor[0][0][0] + 10, 255, 255

    lowerLimit = np.array(lowerLimit, dtype=np.uint8)
    upperLimit = np.array(upperLimit, dtype=np.uint8)

    return lowerLimit, upperLimit