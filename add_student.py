import cv2                                                                      # openCV
import numpy as np                                                              # for numpy arrays
import sqlite3
import cognitive_face as CF
import dlib
import os
import time                                                                # for creating folders
import urllib, sys
cap = cv2.VideoCapture(0)
detector = dlib.get_frontal_face_detector()
def getId() :
    connect = sqlite3.connect("Face-DataBase")                                  # connecting to the database
    cmd = "SELECT ID FROM Students"
    cursor = connect.execute(cmd).fetchall()
    array = []
    for i in cursor:
        array.append(i[0])
    array.sort()
    l = 0
    ID = 0
    for r in array:
        if (l + 1 != r):
            ID = l + 1
            break
        l = r
    if (ID == 0):
        ID = len(array) + 1
    connect.close()                                                             # closing the connection
    return ID
def insertOrUpdate(Id, Name) :                                            # this function is for database
    connect = sqlite3.connect("Face-DataBase")                                  # connecting to the database
    cmd = "SELECT * FROM Students WHERE ID = " + str(Id)                             # selecting the row of an id into consideration
    cursor = connect.execute(cmd)
    isRecordExist = 0
    for row in cursor:                                                          # checking wheather the id exist or not
        isRecordExist = 1
    if isRecordExist == 1:                                                      # updating name and roll no
        connect.execute("UPDATE Students SET Name = ? WHERE ID = ?",(Name, Id))
    else:
    	params = (Id, Name)                                               # insering a new student data
    	connect.execute("INSERT INTO Students(ID, Name) VALUES(?, ?)", params)
    connect.commit()                                                            # commiting into the database
    connect.close()                                                             # closing the connection
connect = sqlite3.connect("Face-DataBase")                                  # connecting to the database
Id = getId()
insertOrUpdate(Id, str(sys.argv[1]))                                                  # calling the sqlite3 database


folderName = "user" + str(Id)                                                        # creating the person or user folder
folderPath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "dataset/"+folderName)
if not os.path.exists(folderPath):
    os.makedirs(folderPath)
sampleNum = 0
while(True):
    ret, img = cap.read()                                                       # reading the camera input
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                                # Converting to GrayScale
    if (cv2.waitKey(1) == ord('q')):
        dets = detector(img, 1)
        for i, d in enumerate(dets):                                                # loop will run for each face detected
            sampleNum += 1
            cv2.imwrite(folderPath + "/User." + str(Id) + "." + str(sampleNum) + ".jpg",
                        img[d.top():d.bottom(), d.left():d.right()])                                                # Saving the faces
            cv2.rectangle(img, (d.left(), d.top())  ,(d.right(), d.bottom()),(0,255,0) ,2) # Forming the rectangle
        time.sleep(0.5)
    cv2.imshow('frame', img)                                                    # showing the video input from camera on window
    if(sampleNum >= 1):                                                        # will take 20 faces
        break

cap.release()                                                                   # turning the webcam off
cv2.destroyAllWindows()                                                         # Closing all the opened windows

Key = "d45ebcdf3bb8479980a4224f0944a24d"
CF.Key.set(Key)
BASE_URL = 'https://westeurope.api.cognitive.microsoft.com/face/v1.0/'  # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)
res = CF.person.create("test1", "user" + str(Id))
connect = sqlite3.connect("Face-DataBase")
cmd = "SELECT * FROM Students WHERE ID = " + str(Id)
cursor = connect.execute(cmd)
isRecordExist = 0
for row in cursor:                                                          # checking wheather the id exist or not
    isRecordExist = 1
if isRecordExist == 1:                                                      # updating name and roll no
    connect.execute("UPDATE Students SET personID = ? WHERE ID = ?",(res['personId'], Id))
connect.commit()                                                            # commiting into the database
connect.close()
currentDir = os.path.dirname(os.path.abspath(__file__))
imageFolder = os.path.join(currentDir, "dataset/" + "user" + str(Id))
person_id = res['personId']
for filename in os.listdir(imageFolder):
    if filename.endswith(".jpg"):
        imgurl = urllib.pathname2url(os.path.join(imageFolder, filename))
        print(imgurl)
        print("------------")
        res = CF.face.detect(imgurl)
        if len(res) != 1:
            print ("No face detected in image")
        else:
            res = CF.person.add_face(imgurl, "test1", person_id)
            print(res)
