import cv2

#Initialize camera
cam = cv2.VideoCapture(0);
ret, image = cam.read();

if ret:
  cv2.imwrite("./pics/ex1.jpg", image)
cam.release()