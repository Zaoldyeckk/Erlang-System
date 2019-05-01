import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

IMG_NAME = "16.png"
img = cv2.imread(IMG_NAME)

kernel = np.ones((2,2),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 1)
plt.imsave("ero-" + IMG_NAME, erosion)

# identifer_x = 300
# identifer_y = 240
# walkable = erosion.copy()
# identifer = erosion[identifer_x, identifer_y]
# walkable[walkable != identifer] = 0
# walkable = cv2.cvtColor(walkable, cv2.COLOR_BGR2GRAY)
# walkable[walkable != 0] = 1
# kernel = np.ones((3,3),np.uint8)
# dilation = cv2.dilate(walkable,kernel,iterations = 1)
# plt.imsave("dwalk-" + IMG_NAME, dilation, cmap="gray")

erosion = cv2.cvtColor(erosion, cv2.COLOR_BGR2GRAY)
roi = erosion[300:360, 160:320]
im = Image.fromarray(roi)
plt.imsave("roi-" + IMG_NAME, roi)
w, h = im.size
colors = im.getcolors(w*h)
print(colors)
print(max(colors))
count, (c) = max(colors)
colors.remove((count, c))
if len(colors) > 0:
    _, (c2) = max(colors)
walkable = erosion.copy()
walkable[walkable == c] = 1
if len(colors) > 0:
    walkable[walkable == c2] = 1
walkable[walkable != 1] = 0
plt.imsave("walk-" + IMG_NAME, walkable, cmap="gray")

