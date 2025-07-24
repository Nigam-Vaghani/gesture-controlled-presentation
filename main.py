import cv2
import os
from cvzone.HandTrackingModule import HandDetector
import numpy as np
# Set frame size
width, height = 1280, 720
folderPath = "Presentation"

# Setup camera
# "http://192.168.164.74:8080/video"
cap = cv2.VideoCapture(0)

cap.set(3, width)
cap.set(4, height)

# Load slide images
pathImages = sorted(os.listdir(folderPath), key=len)
# print(pathImages)

# Webcam preview size (small box)
ws, hs = int(213 * 1.2), int(120 * 1.2)

# Variables
# Index of current slide
imgNumber = 0
gestureThreshoold = 300
buttonCounter = 0
buttonPress = False
buttonDelay = 20    #change value how much delay you want to acatuoally change slide
# hand detector
detector = HandDetector(detectionCon=0.8, maxHands=1)
annotations = [[]]
annotationsNumber = 0
annotationsStart = False

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    

    # Read and resize the slide
    pathFullImage = os.path.join(folderPath, pathImages[imgNumber])
    imgCurrent = cv2.imread(pathFullImage)
    imgCurrent = cv2.resize(imgCurrent, (width, height))  # resize slide to screen

    hands, img = detector.findHands(img)
    cv2.line(img, (0, gestureThreshoold), (width, gestureThreshoold), (0, 255, 0), 10)
    
    if hands and buttonPress is False:
        hand = hands[0]
        fingers = detector.fingersUp(hand)
        cx, cy = hand['center']
        # print(fingers)
        lmList = hand['lmList']
        
        # constrain Value For Easy Drawing 
        xVal = int(np.interp(lmList[8][0], [width // 2, width], [0, width]))
        yVal = int(np.interp(lmList[8][1], [150 , height - 150], [0, height]))
        indexFinger = xVal, yVal
        
        # if hands are at heighto fo the fave then only acept
        if cy <  gestureThreshoold:
            annotationsStart = False
            # gesture - 1 left
            if fingers == [1, 0 , 0 , 0, 0]:  # index finger up
                # print("left")
                annotationsStart = False
                if imgNumber > 0:
                    buttonPress = True  
                    annotations = [[]]
                    annotationsNumber = 0
                    imgNumber -=1   
            # gesture - 2 right
            if fingers == [0, 0 ,0, 0, 1]:  # pinky finger up
                # print("right")
                annotationsStart = False
                if imgNumber < len(pathImages) - 1:
                    buttonPress = True
                    annotations = [[]]
                    annotationsNumber = 0
                    imgNumber += 1

        # gesture - 3 show pointer
        if fingers == [0 , 1, 1, 0, 0]:
            cv2.circle(imgCurrent, indexFinger, 12, (0, 0, 255), cv2.FILLED)
            annotationsStart = False
            
        # Gesture - 4 DRAW
        if fingers == [0 , 1, 0, 0, 0]:
            if annotationsStart is False:
                annotationsStart = True
                annotationsNumber += 1
                annotations.append([])
            cv2.circle(imgCurrent, indexFinger, 12, (0, 0, 255), cv2.FILLED)
            annotations[annotationsNumber].append(indexFinger)
        else:
            annotationsStart = False
        
        # Gesture - 5 Erase
        if fingers == [0, 1, 1, 1, 0]:
            if annotations:
                if annotationsNumber >= 0:
                    annotations.pop(-1)
                    annotationsNumber -= 1
                    buttonPress = True
                
    else:
        annotationsStart = False
    # button press iteration
    if buttonPress:
        buttonCounter += 1
        if buttonCounter > buttonDelay:
            buttonCounter = 0
            buttonPress = False

    # Draw annotations
    for i in range (len(annotations)):
        for j in range(len(annotations[i])):
            if j != 0:
                # Draw line between previous and current annotation
                cv2.line(imgCurrent, annotations[i][j-1], annotations[i][j], (0, 0, 200), 12)
       
    # Resize webcam image and place it top-right
    imgSmall = cv2.resize(img, (ws, hs))
    imgCurrent[0:hs, width - ws:width] = imgSmall  # top-right placement

    # Show both
    cv2.imshow("Slides", imgCurrent)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

