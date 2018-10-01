# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 14:14:02 2018

@author: lloyd
"""


import numpy as np
import cv2

img = cv2.imread('testcar.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
laplacian = cv2.Laplacian(gray, cv2.CV_64F)
sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=5)
edges = cv2.Canny(gray, 75, 100, apertureSize = 3)
lines = cv2.HoughLines(edges, 2, np.pi/180, 50)
# =============================================================================
#     cv2.imshow('gray',gray)
#     cv2.imshow('laplacian', laplacian)
#     cv2.imshow('sobelx', sobelx)
#     cv2.imshow('sobely', sobely)
# =============================================================================
for rho,theta in lines[0]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
    cv2.line(img,(x1,y1),(x2,y2),(0,0,200),2)

cv2.imwrite('houghlines3.jpg', edges)

img2 = cv2.imread('testcar.jpg')
gray2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
edges2 = cv2.Canny(gray2,50,150,apertureSize = 3)
minLineLength = 1
maxLineGap = 10
lines = cv2.HoughLinesP(edges2,1,np.pi/180,100,minLineLength,maxLineGap)
for x1,y1,x2,y2 in lines[0]:
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

cv2.imwrite('houghlines5.jpg',img)
