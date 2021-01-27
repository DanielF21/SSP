import numpy as np
import math
from astropy.io import fits
import matplotlib.pyplot as plt
'''
pA = np.array([[0,33,21,33,8],[0,56,51,53,26],[23,120,149,73,18],[55,101,116,50,16],[11,78,26,2,10]])
n = pA[::, 0:1:1].sum() + pA[::, 1:2:1].sum() + pA[::, 2:3:1].sum() + pA[::, 3:4:1].sum() + pA[::, 4::1].sum()
cX = (pA[::, 0:1:1].sum() + pA[::, 1:2:1].sum() * 2 + pA[::, 2:3:1].sum() * 3 + pA[::, 3:4:1].sum() * 4 + pA[::, 4::1].sum() * 5)/(n) - 1
print(cX)
cY = (pA[0:1:1, ::1].sum() + pA[1:2:1, ::1].sum() * 2 + pA[2:3:1, ::1].sum() * 3 + pA[3:4:1, ::1].sum() * 4 + pA[4::1, ::1].sum() * 5)/(n) - 1 
print(cY)
'''
print("Part b")

print(fits.getheader("sampleimage.fits"))
image = fits.getdata("sampleimage.fits")
print(image)
print(image.shape)
plt.gray()
plt.imshow(image)
plt.show()


im = fits.getdata("sampleimage.fits")
def centroid(file, x, y, r):
    im = fits.getdata("sampleimage.fits")
    Region = im[x-r:x+r+1,y-r:y+r+1]
    im = Region
    plt.gray()
    plt.imshow(im, vmin=im.mean(),vmax = 2 * im.mean())
    plt.show()
    countx = 0
    county = 0
    countXn = 0
    countYn = 0
# weighted mean
    for i in range(2 * r + 1):
        countx += sum(Region[::, i] * (i))
        
   
    for i in range(2 * r + 1):
        county += sum(Region[i, ::] * (i))
        
   
    for i in range(2 * r + 1):
        countXn += sum(Region[::, i])
        

    for i in range(2 * r + 1):
        countYn += sum(Region[i, ::])


    WeightedMeanX = countx / countXn
    WeightedMeanY = county / countYn
    stdevx = 0
    stdevxBottom = 0
    stdevy = 0
    stdevyBottom = 0
    print(WeightedMeanX)
    print(WeightedMeanX - r + x)
    print(WeightedMeanY)
    print(WeightedMeanY - r + y)
    for i in range(2 * r + 1):
        stdevx += sum(Region[i, ::] * (WeightedMeanX - i)**2)
    for i in range(2 * r + 1):
        stdevxBottom += sum(Region[i, ::])
    xstd = math.sqrt(stdevx / stdevxBottom)
    print(xstd)
    uncx = xstd / (math.sqrt(stdevxBottom - 1))
    print(uncx)

    for i in range(2 * r + 1):
        stdevy += sum(Region[::, i] * (WeightedMeanY - i)**2)
    for i in range(2 * r + 1):
        stdevyBottom += sum(Region[::, i])
    ystd = math.sqrt(stdevy / stdevyBottom)
    print(ystd)
    uncy = ystd / (math.sqrt(stdevyBottom - 1))
    print(uncy)


    
print(centroid("sampleimage.fits",154,351,1))

