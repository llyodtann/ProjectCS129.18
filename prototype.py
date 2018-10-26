# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 14:14:02 2018

@author: llyod
"""


import numpy as np
import cv2


img = cv2.imread('testcar2.jpg')
#Convert to Grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#Gaussian Filter
blur = cv2.GaussianBlur(gray, (5,5), 0)
#Canny Edge Detector
edges = cv2.Canny(blur, 75, 100, apertureSize = 3)
#hough transform
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 60, maxLineGap= 45)

#drawing lines on img
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img,(x1,y1),(x2,y2),(0,0,255), 2)

cv2.imwrite('houghlines3.jpg', img)
cv2.imwrite('grayscaled.jpg', gray)
cv2.imwrite('blurred edge.jpg', edges)