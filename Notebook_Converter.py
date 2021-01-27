from math import *
import numpy as np

def Convert(Ra, Dec):
    Ra /= 15
    RaMinutes = Ra - int(Ra)
    Ra = Ra - RaMinutes
    RaMinutes *= 60
    RaSeconds = RaMinutes - int(RaMinutes)
    RaMinutes = RaMinutes - RaSeconds
    RaSeconds *= 60
    print("==============================")
    print("Right Ascention in Sexagesimal")
    print(Ra, RaMinutes, RaSeconds)
    print("==============================")
    Dec /= 15
    DecMinutes = Dec - int(Dec)
    Dec = Dec - DecMinutes
    DecMinutes *= 60
    DecSeconds = DecMinutes - int(DecMinutes)
    DecMinutes = DecMinutes - DecSeconds
    DecSeconds *= 60
    print("Declination in Sexagesimal")
    print(Dec, DecMinutes, DecSeconds)
    print("==============================")
    return("Done!")
print(Convert(20.62599956956769 * 15, -6.872044214771413 * 15))
