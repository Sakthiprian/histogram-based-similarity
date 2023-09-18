    
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import math
import cv2 as cv

def Bhattacharya(hist1, hist2):
    hist1 = hist1.astype(np.float32)  
    hist2 = hist2.astype(np.float32)  
    Bd = cv.compareHist(hist1, hist2, cv.HISTCMP_BHATTACHARYYA)
    return Bd

qimage = Image.open('D:/coding/PRML/lab4/queryimage.png')
refimage1 = Image.open('D:/coding/PRML/lab4/refimage1.png')
refimage2 = Image.open('D:/coding/PRML/lab4/refimage2.png')

bins = np.arange(256)

H1=np.histogram(qimage, bins)
H2=np.histogram(refimage1, bins)
H3=np.histogram(refimage2, bins)

hist0 = H1[0]
hist1 = H2[0]
hist2 = H3[0]

dist = []
for hist in [hist1, hist2]:
    dist.append(Bhattacharya(hist0, hist))

min=min(dist)
if dist.index(min)==0:
    print("The query histogram is most similar to refimage1.png")
else:
    print("The query image is most similar to refimage2.png")

fig, ax = plt.subplots(3, 1, sharey=True, tight_layout=False)

ax[0].hist(H1[0],bins)
ax[1].hist(H2[0],bins)
ax[2].hist(H3[0],bins)

plt.show()
