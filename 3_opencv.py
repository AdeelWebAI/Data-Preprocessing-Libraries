import cv2
import numpy as np

# 1. Reading and Displaying Images

image =cv2.imread("apple.jpg")
img= cv2.resize(image, (500,500)) # resize the image but not the current one 
# print(img.shape)
# gry_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # change the color to bray scale 
# print(img)
# cv2.imshow("apple image",img) # show the image but make sure to add waitkey
# if cv2.waitKey(0) == 27:
#     cv2.destroyAllWindows()

# cv2.imwrite("new.png",img) 

# 2. Drawing Shapes on Images

# rectangle on image

cv2.rectangle(img, (50,50), (400,400), (255,0,0), 3)

# circle on image

cv2.circle(img, (150,150), (100), (0,255,0), 4)

# line on image

cv2.line(img, (50,50),(450,450),(0,0,255), 3)

cv2.imwrite("edited.png",img)

# cv2.imshow("apple image",img) # show the image but make sure to add waitkey
# if cv2.waitKey(0) == 27:
#     cv2.destroyAllWindows()
    

import numpy as np

# Create a blank image
canvas = np.zeros((500, 500, 3), dtype="uint8")

# Draw a rectangle
cv2.rectangle(canvas, (50, 50), (200, 200), (0, 255, 0), 3)

# Draw a circle
cv2.circle(canvas, (300, 300), 50, (255, 0, 0), -1)

# Draw a line
cv2.line(canvas, (100, 100), (400, 400), (0, 0, 255), 5)

cv2.imshow("Shapes", canvas)
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()