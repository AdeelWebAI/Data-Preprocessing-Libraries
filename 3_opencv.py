import cv2
import numpy as np

image =cv2.imread("apple.jpg")
img= cv2.resize(image, (500,500)) # resize the image but not the current one 
gry_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # change the color to bray scale 
cv2.imshow("apple image",gry_img) # show the image but make sure to add waitkey
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()

