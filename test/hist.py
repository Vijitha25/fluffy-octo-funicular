import cv2
from matplotlib import pyplot as plt
img = cv2.imread('madrill2.png',0)

# alternative way to find histogram of an image
plt.hist(img.ravel(),255,[1,256])
plt.show()
