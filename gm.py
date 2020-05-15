import cv2
import numpy as np 

bg_video = '/Users/varun/documents/green_matting/2.mov'

fg_video = '/Users/varun/documents/green_matting/1.mp4'

lower_green = (0,100,0)
upper_green = (100,255,120)

cam1 = cv2.VideoCapture(bg_video)
cam2 = cv2.VideoCapture(fg_video)

while True:

    _,frame1 = cam1.read()
    # frame1 = cv2.imread(bg_video)
    _,frame2 = cam2.read()

    image = frame2.copy()
    mask = cv2.inRange(frame2,lower_green,upper_green)
    masked_image = image.copy()
    masked_image[mask != 0] = (0, 0, 0)

    bg_image = frame1.copy()
    bg_image = bg_image[0:720, 0:1280]
    bg_image[mask == 0] = (0, 0, 0)


    final_image = bg_image + masked_image


    try:
        cv2.imshow("result",final_image)
        
    except Exception as e:
        break

    if(cv2.waitKey(1) & 0xff == ord('q')):
        break



cv2.destroyAllWindows()
