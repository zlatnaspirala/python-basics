
# importing cv2
import cv2

print(cv2.__version__)
# path
path = r'/Volumes/POMOCNI/WWW-HTDOCS/cpp/test-nidza-ai/test2/working-basics-examples/draws-cv/nidza.jpg'

# Reading an image in default mode
image = cv2.imread(path)

# Window name in which image is displayed
window_name = 'Image'

# Start coordinate, here (0, 0)
# represents the top left corner of image
start_point = (0, 0)

# End coordinate
end_point = (200, 200)

# Green color in BGR
color = (0, 255, 0)

# Line thickness of 9 px
thickness = 9

# Using cv2.arrowedLine() method
# Draw a diagonal green arrow line
# with thickness of 9 px
image = cv2.arrowedLine(image, start_point, end_point,
                        color, thickness)

# Displaying the image
cv2.imshow(window_name, image)

cv2.waitKey(0)
