# PURPOSE OF THIS CODE
# Exercise 2
# 6/21/19
# Daniel Fleming

from math import pi, radians, degrees, sin, cos, asin, acos


def AltAz(ra, dec, long, lat, year, month, day, UT):
    Jo = (367 * year) - int(7 * (year + int((month + 9) /12.))/4.) + int(275 * month/ 9.) + day + 1721013.5
    J = (Jo - 2451545)/ 36525.0
    ThetaO = 100.46061837 + 36000.77053608 * J + (3.87933 * 10**(-4) * J**2) - ((J**3)/(3.871 * 10**7))
    ThetaG = ThetaO + 360.985647366 * (UT / 24.0)
    Theta = ThetaG + long
    LSTHours = (Theta % 360) / 15.0
    radDec = dec * pi / 180.0
    radLat = lat * pi / 180.0
    raHours = ra / 15
    H = LSTHours - raHours
    HDeg = H * 15
    print(HDeg)
    HRad = HDeg * pi / 180
    print(HRad)
    print(sin(HRad))
    Alt = (asin(sin(radDec) * sin(radLat) + cos(radDec) * cos(radLat) * cos(HRad))) * 180 / pi
    #Az = acos(sin(radDec) - sin(Alt) * sin(radLat))/(cos(Alt) * cos(radLat))
    Az = acos(((sin(radDec) * cos(radLat) - cos(radDec) * sin(radLat) * cos(HRad))/cos(Alt * pi / 180))) * 180 / pi
    print(Az)
    if sin(HRad) > 0:
        Az = 360 - Az
    print(Alt)
    print(Az)
    
print(AltAz(156.65166, 24.90443, 253.08608, 34.0727, 2019, 6, 12, 5))
   
def re(Ra, Dec):
    x = cos(Ra) * cos(Dec)
    y = sin(Ra)* cos(Dec) * cos(23.45 * pi / 180) + sin(Dec) * sin(23.45 * pi / 180)
    z = -1 * sin(Ra) * cos(Dec) * sin(23.45 * pi / 180) + sin(Dec) * cos(23.45 * pi / 180)
    wlist = [x,y,z]
    return wlist

print(re((14 + 12/60. + 38.5/3600.) * 15 * pi / 180., (23 + 48/60. + 38/3600.) * pi / 180.))
print(re(6 * 15 * pi / 180, 0))

