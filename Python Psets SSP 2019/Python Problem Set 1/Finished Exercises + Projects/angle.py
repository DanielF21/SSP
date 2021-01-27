# PURPOSE OF THIS CODE
# Angle Unit Conversion
# 6/20/19
# Daniel Fleming

import math

def convertAngle(degrees, minutes, seconds):   
    DecAng = degrees + minutes / 60 + seconds / 3600
    if degrees <= 0:
        degrees *= -1
        DecAng = (degrees + minutes/60 + seconds/3600) * (-1)
    return DecAng




# test cases for part a
print(convertAngle(90, 6, 36)) # should print 90.11
print(convertAngle(-90, 6, 36)) # should print -90.11
print(convertAngle(-0.0, 30, 45)) # should print -0.5125


def convertAngle2(degrees, minutes, seconds, radians):
    DecAng = degrees + minutes / 60 + seconds / 3600
    if degrees <= 0:
        degrees *= -1
        DecAng = (degrees + minutes/60 + seconds/3600) * (-1)
    if radians == True:
        DecAngRad = DecAng * math.pi / 180
        return DecAngRad
    else:
        return DecAng

print(convertAngle2(90, 6, 36, True)) # should print 1.57271618897
print(convertAngle2(-90, 6, 36, True)) # should print -1.57271618897
print(convertAngle2(90, 6, 36, False)) # should print 90.11
print(convertAngle2(-90, 6, 36, False)) # should print -90.11


def convertAngle3(degrees, minutes, seconds, radians, normalize):
    DecAng = degrees + minutes / 60 + seconds / 3600
    if degrees <= 0:
        degrees *= -1
        DecAng = (degrees + minutes/60 + seconds/3600) * (-1)
    if radians == True and normalize == True:
        DecAngRad = DecAng * math.pi / 180
        return DecAngRad % (2 * math.pi)
    elif radians == True:
        DecAngRad = DecAng * math.pi / 180
        return DecAngRad
    elif radians == False and normalize == True:
        return DecAng % 360
    else:
        return DecAng
# these are the test cases you will demonstrate when getting this homework checked off
# test cases for part c (uncomment these, comment out previous tests)
print(convertAngle3(90, 6, 36, False, False)) # should print 90.11
print(convertAngle3(90, 6, 36, True, False)) # should print 1.57271618897
print(convertAngle3(90, 6, 36, False, True)) # should print 90.11
print(convertAngle3(90, 6, 36, True, True)) # should print 1.57271618897
print(convertAngle3(-90, 6, 36, False, False)) # should print -90.11
print(convertAngle3(-90, 6, 36, True, False)) # should print -1.57271618897
print(convertAngle3(-90, 6, 36, False, True)) # should print 269.89
print(convertAngle3(-90, 6, 36, True, True)) # should print 4.71046911821
print(convertAngle3(540, 0, 0, False, True)) # should print 180.0
print(convertAngle3(-0.0, 30, 45, False, False)) # should print -0.5125
