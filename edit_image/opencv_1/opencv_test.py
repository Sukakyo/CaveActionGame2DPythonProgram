import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('Cave1-A1.png')

h = round(img.shape[0]/2)
w = round(img.shape[1]/2)
trim_img = img[0:32,0:64]
# plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.imshow(cv2.cvtColor(trim_img,cv2.COLOR_BGR2RGB))
plt.show()
