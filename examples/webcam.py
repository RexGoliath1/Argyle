import cv2
import os

#Initialize camera
cam1 = cv2.VideoCapture(0);
cam2 = cv2.VideoCapture(0);

ret1, image1 = cam1.read();
ret2, image2 = cam2.read();

if ret1:
  os.system('mkdir ./pics/')
  cv2.imwrite("./pics/ex1.jpg", image1)

if ret2:
  os.system('mkdir ./pics/')
  cv2.imwrite("./pics/ex2.jpg", image2)

cam1.release()
cam2.release()