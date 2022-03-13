import numpy as np
import cv2 as cv

img = cv.imread('478d2f55-ec07-4abb-ad37-c1cbcf9620bd.jpg',0)
equ = cv.equalizeHist(img)
res = np.hstack((img, equ))
cv.imwrite('NEW.png',res)

