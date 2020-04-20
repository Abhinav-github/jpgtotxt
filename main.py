# Python program to read image using OpenCV
import cv2
import imread
import numpy
import time
# Save image in set directory
# Read RGB image
txt_parts = {}
i = 0
with open('pic.jpg', 'rb') as pic:
    BRG = cv2.imread('pic.jpg')
#    print(BRG)
#    time.sleep(3)
#    lower = numpy.array([242, 242, 242])
#    upper = numpy.array([255, 255, 255])
#    shapeMask = cv2.inRange(BRG, lower, upper)
#    cv2.imshow("Mask", shapeMask)
#    time.sleep(3)
    for i in range(len(BRG)):
        for j in range(len(BRG[0])):
            if BRG[i][j][0] == 0 and BRG[i][j][1] == 0 and BRG[i][j][2] == 0:
                txt_parts[(i,j)] = True;
print(txt_parts)
