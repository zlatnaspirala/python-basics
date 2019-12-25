
# Syntax: cv2.blur(src, ksize[, dst[, anchor[, borderType]]])
# Parameters:
# src: It is the image whose is to be blurred.
# ksize: A tuple representing the blurring kernel size.
# dst: It is the output image of the same size and type as src.
# anchor: It is a variable of type integer representing anchor point and it’s default value Point is (-1, -1) which means that the anchor is at the kernel center.
# borderType: It depicts what kind of border to be added. It is defined by flags like cv2.BORDER_CONSTANT, cv2.BORDER_REFLECT, etc
# Return Value: It returns an image.

# Python program to explain cv2.blur() method

# importing cv2
import cv2

# path
path = r'/Volumes/POMOCNI/WWW-HTDOCS/cpp/test-nidza-ai/test2/working-basics-examples/draws-cv/nidza.jpg'

# Reading an image in default mode
image = cv2.imread(path)

# Window name in which image is displayed
window_name = 'Image'

# ksize
ksize = (30, 30)

# Using cv2.blur() method
image = cv2.blur(image, ksize, cv2.BORDER_DEFAULT)

# Displaying the image
cv2.imshow(window_name, image)

cv2.waitKey(0)
