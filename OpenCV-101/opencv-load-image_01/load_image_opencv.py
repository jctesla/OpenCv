# we use:
# argparse : read images from OpenCV.
# display image parameters: h, w ,c
# show images and save in to other formats.

# Example of USAGE:
# c:\> python load_image_opencv.py --image 30th_birthday.png
import argparse
import cv2
import sys
print(f"Python ver = {sys.version}")

# ------------Input Img------------------------
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,	help="path to input image/ruta de la imagen")
args = vars(ap.parse_args())                                            # sustraigo el argumento colocado, en el comando de ejecucion: 
                                                                        # c:\> python load_image_opencv.py --image 30th_birthday.png
# ------------OpenCV------------------------
# image = spatial dimensions, including width, height, and number of channels
image = cv2.imread(args["image"])                                       # load the image from disk via "cv2.imread" 
print(f"type = {type(image)}")                                          # type = <class 'numpy.ndarray'>
print(f"item size = {image.itemsize}")                                  # item size = 1
print(f"shape = {image.shape}")                                         # shape entrega la matriz = (433, 577, 3)  esto es: (433=rows/height, 577=cols/width, 3=RGB)  nota: 3 x c/8bits = 24bits color.
print(f"ndim = {image.ndim}")                                           # ndim = 3
print(f"tipo var = {image.dtype}")                                      # tipo var = uint8
(h, w, c) = image.shape                                                 # crea un Tupla de varios rows = height / varios cols = width             ó    
#(h, w, c) = image.shape[:3]                                            # de esta forma es p validar x siacaso haya mas dimension
# nota:
# si tenemos una imagen: w=600 x h=400
# esto se ref a: 600=width ^ 400=height

# display the image width, height, and number of channels to our
# terminal
print(f"height: {h}  pixels")                                           # height: 433  pixels
print(f"width: {w} pixels")                                             # width: 577 pixels
print(f"channels: {c}")                                                 # channels: 3

# show the image and wait for a keypress
cv2.imshow("Mi titulo de Image", image)
cv2.waitKey(0)

# save the image back to disk (OpenCV handles converting image          # .bmp <sin comprimir>, jpg <comprimido>, png <comprimidio> etc
# filetypes automatically)
cv2.imwrite("newimage.bmp", image)