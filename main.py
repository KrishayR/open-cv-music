import cv2
import numpy as np
import pyttsx3
import pygame
voice = pyttsx3.init()
pygame.mixer.init()
pygame.mixer.music.load('alarm.mp3')
cap = cv2.VideoCapture(0)

re_lower = np.array([0,120,70])
re_upper = np.array([10,255,255])

lower_red = np.array([170,120,70])
upper_red = np.array([180,255,255])

prev_y = 0
while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask1 = cv2.inRange(hsv,re_lower,re_upper)
    mask2 = cv2.inRange(hsv,lower_red,upper_red)
    mask = mask1+mask2
    contours, hierarchy = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for i in contours:
        area = cv2.contourArea(i)
        if area > 1000:
            pygame.mixer.music.play()
            x,y,w,h = cv2.boundingRect(i)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),5)

    cv2.imshow('camera',frame)
    cv2.imshow('mask',mask)
    if cv2.waitKey(10) == ord('x'):
        break
cap.release()
cv2.destroyAllWindows()
