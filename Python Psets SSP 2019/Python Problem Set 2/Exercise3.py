import numpy as np
import math
import matplotlib.pyplot as plt
from astropy.io import fits

def astmag(file, xstar, ystar, Starwidth, Starmag, xast, yast, astwidth, xblank, yblank):
    im = fits.getdata("sampleimage.fits")
    starArray = im[(xstar - 2) :(xstar + 3), (ystar - 2) :(ystar + 3)]
    skyfield = im[yblank - 1: yblank + 2, xblank - 1: xblank + 2]
    #im = starArray
    #plt.imshow(im)
    #plt.gray()
    #plt.show()
   # countx = 0
   # for i in range(2 * Starwidth + 1):
   #     countx += sum(starArray[::, i])
    print(starArray)
    countx = starArray.sum()
    print(countx)
    avgSky = skyfield.mean()
    Signal = countx - (avgSky * 25)
    print(Signal)
    c = Starmag + 2.5 * math.log10(Signal)
    print(c)
    print(-2.5 * math.log10(Signal) + c)
    asteroidArray = im[(yast - 1): yast + 2, xast - 1: xast + 2]
    print(asteroidArray)
   # countast = 0
   # for i in range(2 * astwidth + 1):
   #    countast += np.sum(im(asteroidArray[::, i]))
    countast = (asteroidArray).sum()
    SignalAst = countast - (avgSky * 9)
    print(-2.5 * math.log10(SignalAst) + c)




print(astmag("sampleimage.fits", 285, 355, 5, 16.11, 351, 154, 3, 200, 200))
print(astmag("sampleimage.firs", 342, 173, 5, 15.26, 351, 154, 3, 200, 200))
