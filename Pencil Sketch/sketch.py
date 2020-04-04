import cv2
import numpy as np

read = cv2.imread("pk.jpg")

scale_per = 0.60

width = int(read.shape[1]*scale_per)
height = int(read.shape[0]*scale_per)

dim = (width,height)
resiz = cv2.resize(read,dim,interpolation = cv2.INTER_AREA)

kernel_sharpe = np.array([[-1,-1,-1],[-1, 9,-1],[-1,-1,-1]])
sharpened = cv2.filter2D(resiz,-1,kernel_sharpe)

gray_scale = cv2.cvtColor(sharpened , cv2.COLOR_BGR2GRAY)
inv = 255-gray_scale
gauss = cv2.GaussianBlur(inv,ksize=(15,15),sigmaX=0,sigmaY=0)

def dodge(image,mask):
    return cv2.divide(image,255-mask,scale=256)

pencil = dodge(gray_scale,gauss)
pencil = cv2.resize(pencil,(1360,760))
#cv2.imshow('resized',resiz)
#cv2.imshow('sharp',sharpened)
#cv2.imshow('gray_scale',gray_scale)
#cv2.imshow('inv',inv)
#cv2.imshow('gauss',gauss)
cv2.imshow('Final_Result',pencil)
cv2.waitKey(0)
cv2.destroyAllWindows()

