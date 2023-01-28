
# move translate/move the smallBox dentro del mainBox
import numpy as np
import argparse
import imutils
import cv2

mainBox = np.zeros((300, 300, 3), dtype="uint8")											# crea un canvas con fondo de color 0 = Black
smallBox = (0,255,0)                                                  # cre una matriz de color RGB = verde
mainBox[100:300-100,100:300-100] = smallBox
cv2.imshow("Original", mainBox)

# shift(move) the image 20 pixels to the right and 40 pixels down
# La posicion de 20, indica cuantos pixeles debe moverse la imgn en eje= 'X' / Cols
# La posicion de 40, indica cuantos pixeles debe moverse la imgn en eje= 'Y' / Rows
M = np.float32([
                [1, 0, 20],
                [0, 1, 40]
              ])
#                                           x         ,       y
shifted = cv2.warpAffine(mainBox, M, (mainBox.shape[1], mainBox.shape[0]))	# consolution: tranform the source image, using the specific Matrix.
cv2.imshow("Shifted Down and Right", shifted)

# now, let's shift the image 30 pixels to the left and 60 pixels
# up by specifying negative values for the x and y directions,
# respectively
M = np.float32([[1, 0, -30], [0, 1, -60]])
shifted = cv2.warpAffine(mainBox, M, (mainBox.shape[1], mainBox.shape[0]))  
cv2.imshow("Shifted Up and Left", shifted)

# use the imutils helper function to translate the image 50 pixels
# down in a single function call
shifted = imutils.translate(mainBox, 0, 50)
cv2.imshow("Shifted Down", shifted)
cv2.waitKey(0)


