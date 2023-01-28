# use : $ python opencv_getting_setting.py -i adrian.png
# In OpenCV, pixels are accessed by their (x, y)-coordinates.

# import the necessary packages
import argparse
import cv2
import sys

print(f"Python ver = {sys.version}")


#-----------------------------------------
#         MAIN()      
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="adrian.png", help="path to the input image")
args = vars(ap.parse_args())

# load the image, in spatial dimensions (width and height),
image = cv2.imread(args["image"])

# read Properties
print(f"type = {type(image)}")                                            # <class 'numpy.ndarray'>
print(f"item size = {image.itemsize}")                                    # item size = 1
print(f"shape = {image.shape}")                                           # = (450, 600, 3) --> (450=rows/height, 600=cols/width, 3=RGB/channels)  nota: 3 x c/8bits = 24bits color.
print(f"ndim = {image.ndim}")                                             # ndim = 3
print(f"tipo var = {image.dtype}")                                        # tipo var = uint8

(h, w) = image.shape[:2] 																								  # image-->3D :. return Rows[0] & Row[1] :.  h=rowm, w=cols  :. es como sigue;
                                                                          #  h = image.shape[0].....450
                                                                          #  w = image.shape[1].....600
print(f"Pixel at (0, 0) - height: {h}, width: {w}")											  # Pixel at (0, 0) - height: 450, width: 600
cv2.imshow("Original", image)																						  # and then display the original image to our screen

# images are simply NumPy arrays -- with the origin (0, 0) located at
# the top-left of the image
print("image[0, 0]=", image[0, 0])
(b, g, r) = image[0, 0]																										# image[0, 0]= [246 240 233] :.
print(f"Read Pixel at (0, 0) - Red: {r}, Green: {g}, Blue: {b}")					# Pixel at (0, 0) - Red: 233, Green: 240, Blue: 246


# access the pixel located at x=50, y=20 :. x=Cols / y=Rows
(b, g, r) = image[20, 50]
print(f"Read Pixel at (50, 20) - Red: {r}, Green: {g}, Blue: {b}")        #  Red: 229, Green: 238, Blue: 245

# update the pixel at (50, 20) and set it to red
#                B  G   R ------>  RGB(estandar pero en progrmacion BGR)
image[20, 50] = (0, 0, 255)
(b, g, r) = image[20, 50]
print(f"Set Pixel at (50, 20) - Red: {r}, Green: {g}, Blue: {b}")

# compute the center of the image, which is simply the width and height
# divided by two
(cX, cY) = (w // 2, h // 2)

# since we are using NumPy arrays, we can apply array slicing to grab
# large chunks/regions of interest from the image -- here we grab the
# top-left corner of the image
tl = image[0:cY, 0:cX]
cv2.imshow("Top-Left Corner", tl)

# in a similar fashion, we can crop the top-right, bottom-right, and
# bottom-left corners of the image and then display them to our
# screen
tr = image[0:cY, cX:w]
br = image[cY:h, cX:w]
bl = image[cY:h, 0:cX]
cv2.imshow("Top-Right Corner", tr)
cv2.imshow("Bottom-Right Corner", br)
cv2.imshow("Bottom-Left Corner", bl)

# set the top-left corner of the original image to be green
#                     B  G   R ------>  RGB(estandar pero en progrmacion BGR)
image[0:cY, 0:cX] = (0, 255, 0)

# Show our updated image
cv2.imshow("Updated", image)


cv2.waitKey(0)