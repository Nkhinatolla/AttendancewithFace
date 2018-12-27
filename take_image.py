import cv2                                                                      # openCV
import os
import time                                                                # for creating folders

cap = cv2.VideoCapture(0)


sampleNum = 0
folderName = "test1"                                                       # creating the person or user folder
folderPath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "pics/")
print(folderPath)
while(True):
    ret, img = cap.read()                                                       # reading the camera input
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                                # Converting to GrayScale
    if (cv2.waitKey(1) == ord('q')):
        sampleNum += 1
        cv2.imwrite(folderPath + folderName + ".jpg", img)                                                # Saving the faces
        time.sleep(0.5)
    cv2.imshow('frame', img)                                                    # showing the video input from camera on window
    if(sampleNum >= 1):                                                        # will take 20 faces
        break

cap.release()                                                                   # turning the webcam off
cv2.destroyAllWindows()                                                         # Closing all the opened windows
