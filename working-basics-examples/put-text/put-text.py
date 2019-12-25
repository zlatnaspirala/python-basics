
# Python program to explain cv2.putText() method

# importing cv2
import cv2

# path
path = r'/Volumes/POMOCNI/WWW-HTDOCS/cpp/test-nidza-ai/test2/working-basics-examples/put-text/nidza.jpg'

inputtext = 'We are the champions'
# Reading an image in default mode
image = cv2.imread(path)

# Reading an image in grayscale mode
# image = cv2.imread(path, 0)

# Window name in which image is displayed
window_name = 'Image'

# font
font = cv2.FONT_HERSHEY_SIMPLEX

# org
org = (5, 150)

# fontScale
fontScale = 1

# Blue color in BGR
color = (155, 11, 12)

# Line thickness of 2 px
thickness = 2

# Using cv2.putText() method
image = cv2.putText(image, inputtext, org, font,
                    fontScale, color, thickness, cv2.LINE_AA)

cv2.imwrite(path, image)

# Displaying the image
cv2.imshow(window_name, image)

cv2.waitKey(0)
