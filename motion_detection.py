import cv2 as cv
import imutils
from imutils.video import WebcamVideoStream
import time

def main():

	# streamFrame = cv.VideoCapture("video.mp4")
	streamFrame = WebcamVideoStream().start()

	previousFrame = streamFrame.read()
	frame = streamFrame.read()

	while True:
		previousFrame = frame
		frame = streamFrame.read()
		
		grayPrev = cv.cvtColor(previousFrame, cv.COLOR_BGR2GRAY)
		grayCurrent = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

		imgDiff = cv.absdiff(grayPrev, grayCurrent)

		threshold = cv.threshold(imgDiff, 40, 255, cv.THRESH_BINARY)[1]

		dilated = cv.dilate(threshold, None, iterations=2)

		cnts = cv.findContours(dilated.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
		cnts = imutils.grab_contours(cnts)

		# cv.imshow("diff", dilated)
		
		resultImg = frame.copy()
		for c in cnts:
			if cv.contourArea(c) > 4500:
				(x,y,w,h) = cv.boundingRect(c)
				cv.rectangle(resultImg, (x, y), (x + w, y + h), (0, 255, 0), 2)

		cv.imshow("grayscale", dilated)
		cv.imshow("frame", resultImg)
		cv.waitKey()
main()
