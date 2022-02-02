from tabnanny import check
import cv2 as cv
import numpy as np
import matplotlib.colors as mcolors
from time import sleep
import timeit


def detectColor(imgArea):
    """ Get the average pixel color of an image region """
    colorTotal = np.array([0,0,0])
    for i in range(imgArea.shape[0]):          # Height (i)
        for j in range(imgArea.shape[1]):      # Width (j)
            # for k in range(img.shape[2]):  # Color Depth (k)
                # img.itemset((i,j,k), randomcolor[k])
            colorTotal = np.add(imgArea[i][j], colorTotal)
    colorAverage = colorTotal / (imgArea.shape[0]*imgArea.shape[1])
    return colorAverage

def getKey(dict, desiredValue):
    for key, value in dict.items():
        if desiredValue == value:
            return key
 
    return None

def main():

    img = cv.imread("color_grid.png")
    sizeX = img.shape[0]
    sizeY = img.shape[1]
    
    quintantTL = img[int(sizeY*0.1):int(sizeY*0.2),int(sizeX*0.1):int(sizeX*0.2)] # check 10-20% of x and y axis for top-left quintant on image
    quintantBL = img[int(sizeY*0.8):int(sizeY*0.9),int(sizeX*0.1):int(sizeX*0.2)]
    quintantTR = img[int(sizeY*0.1):int(sizeY*0.2),int(sizeX*0.8):int(sizeX*0.9)]
    quintantBR = img[int(sizeY*0.8):int(sizeY*0.9),int(sizeX*0.8):int(sizeX*0.9)]
    quintantCT = img[int(sizeY*0.4):int(sizeY*0.6),int(sizeX*0.4):int(sizeX*0.6)]
    colorTL = detectColor(quintantTL)
    colorTR = detectColor(quintantTR)
    colorBL = detectColor(quintantBL)
    colorBR = detectColor(quintantBR)
    colorCT = detectColor(quintantCT)    
    print("BGR Color for quintant TL: %s" % colorTL)    
    print("BGR Color for quintant BL: %s" % colorTR)
    print("BGR Color for quintant TR: %s" % colorBL)
    print("BGR Color for quintant BR: %s" % colorBR)
    print("BGR Color for quintant CT: %s" % colorCT)
    
    cv.imshow("color_grid.png", img)
    cv.waitKey()

main()
