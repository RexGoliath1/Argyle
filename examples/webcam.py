import cv2
import os

#Initialize camera
cam = cv2.VideoCapture(0);
ret, image = cam.read();

if ret:
  os.system('mkdir ./pics/')
  cv2.imwrite("./pics/ex1.jpg", image)
cam.release()