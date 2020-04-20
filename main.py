# Python program to read image using OpenCV
import cv2
import imread
import numpy
import time
from PIL import Image


#detect letters from pixels
def detect_letters(txt_parts):
    for key in txt_parts:
    #    print(key)
        i = 0

#detect points in image where text exists
def detect_pixels():
    txt_parts = {}
    i = 0
    with open('pic.jpg', 'rb') as pic:
        BRG = cv2.imread('pic.jpg')
        cv2.imshow("check",BRG)
        time.sleep(3)
    #    print(BRG)
    #    time.sleep(3)
    #    lower = numpy.array([242, 242, 242])
    #    upper = numpy.array([255, 255, 255])
    #    shapeMask = cv2.inRange(BRG, lower, upper)
    #    cv2.imshow("Mask", shapeMask)
    #    time.sleep(3)
        for i in range(len(BRG)):
            for j in range(len(BRG[0])):
                if BRG[i][j][2] < 50:
                    txt_parts[(i,j)] = True;

#    print(BRG[284][93])
#    print(len(BRG))
#    print(len(BRG[0]))
    detect_letters(txt_parts)

#write the letters to text file
def write_to_file():
    print('test')

def main():
    detect_pixels()
    write_to_file()

if __name__ == '__main__':
    main()
