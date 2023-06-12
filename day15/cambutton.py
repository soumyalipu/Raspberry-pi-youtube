import RPi.GPIO as GPIO
import cv2
cam = cv2.VideoCapture(0)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(5,GPIO.IN, pull_up_down=GPIO.PUD_UP)
while 1:
    x=GPIO.input(5)
    if x==0:
        print("Button Pressed")
        ret, image = cam.read()
        cv2.imshow('Imagetest',image)
        k = cv2.waitKey(1)
        if k != -1:
            break
cv2.imwrite('/home/pi/Desktop/testimage.jpg', image)
cam.release()
cv2.destroyAllWindows()
   