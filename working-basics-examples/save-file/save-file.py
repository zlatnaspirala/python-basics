import sys
import os
import cv2

print(cv2.__version__)

# Syntax: cv2.putText(image, text, org, font, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]])
# Parameters:
# image: It is the image on which text is to be drawn.
# text: Text string to be drawn.
# org: It is the coordinates of the bottom-left corner of the text string in the image. The coordinates are represented as tuples of two values i.e. (X coordinate value, Y coordinate value).
# font: It denotes the font type. Some of font types are FONT_HERSHEY_SIMPLEX, FONT_HERSHEY_PLAIN, , etc.
# fontScale: Font scale factor that is multiplied by the font-specific base size.
# color: It is the color of text string to be drawn. For BGR, we pass a tuple. eg: (255, 0, 0) for blue color.
# thickness: It is the thickness of the line in px.
# lineType: This is an optional parameter.It gives the type of the line to be used.
# bottomLeftOrigin: This is an optional parameter. When it is true, the image data origin is at the bottom-left corner. Otherwise, it is at the top-left corner.

# Image path
image_path = r'/Volumes/POMOCNI/WWW-HTDOCS/cpp/test-nidza-ai/test2/working-basics-examples/save-file/nidza.jpg'

# Image directory
directory = r'/Volumes/POMOCNI/WWW-HTDOCS/cpp/test-nidza-ai/test2/working-basics-examples/save-file/'

# Using cv2.imread() method
# to read the image
img = cv2.imread(image_path)

# Change the current directory
# to specified directory
os.chdir(directory)

# List files and directories
# in 'C:/Users/Rajnish/Desktop/GeeksforGeeks'
print("Before saving image:")
print(os.listdir(directory))

# Filename
filename = 'savedImage.jpg'

# Using cv2.imwrite() method
# Saving the image
cv2.imwrite(filename, img)

# List files and directories
# in 'C:/Users / Rajnish / Desktop / GeeksforGeeks'
print("After saving image:")
print(os.listdir(directory))

print('Successfully saved')
