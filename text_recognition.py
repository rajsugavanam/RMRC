from cgi import test
from math import sqrt
import pytesseract
import cv2 as cv
import numpy
import imutils

def main():
	# -------------------------------- Image Read -------------------------------- #
	testHazard = cv.imread("hazards/non_flammable_gas.jpg")
	# print(testHazard.shape)
	rgb = cv.cvtColor(testHazard, cv.COLOR_BGR2RGB) # convert image to rgb
	#results = pytesseract.pytesseract.image_to_osd(r"hazards/infectious_substance.jpg")

	# ----------------------------- Width & Rotation ----------------------------- #
	originalWidth = rgb.shape[1] # could be substituted for height here, does not matter
	# will be a diamond-like shape; switching width like a triangle
	rotated = imutils.rotate_bound(rgb, -45)
	rotatedWidth = sqrt(originalWidth)

	scale = 1.414#originalWidth/rotatedWidth

	print("original width: ", originalWidth)
	print("rotated width: ", rotatedWidth)

	scaleFactor = (int(originalWidth*scale), int(originalWidth*scale))
	#print(scaleFactor)
	rotated = cv.resize(rotated, scaleFactor)

	cropLength = int(originalWidth/2.828)

	rotated = rotated[cropLength:-cropLength, cropLength:-cropLength]	

	cv.imshow("test", rotated)
	cv.waitKey(0)
	print(pytesseract.pytesseract.image_to_string(rotated))
	# print(pytesseract.pytesseract.image_to_string(rgb))

main()
