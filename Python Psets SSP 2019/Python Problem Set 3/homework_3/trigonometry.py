# PURPOSE OF THIS CODE
# PROJECT
# NAME
# DATE
from math import *
# a function to determine the quadrant of an angle based on its sine and cosine (in radians)
# returns the angle in the correct quadrant (in radians)
def findQuadrant(sine, cosine):
    if cosine > 0 and sine > 0: 
        return asin(sine)

    if cosine < 0 and sine > 0:
        return acos(cosine)

    if cosine < 0 and sine < 0: 
        return pi - asin(sine)

    if cosine > 0 and sine < 0: 
        return 2*pi + asin(sine)

# a function that given the values (in radians) of two sides and the included angle of a spheical triangle
# returns the values of the remaining side and two angles (in radians)
def SAS(a, B, c):
    a = radians(a)
    B = radians(B)
    c = radians(c)
    b = acos(cos(c) * cos(a) + sin(c) * sin(a) * cos(B))
    A = asin(sin(a) * sin(B) / sin(b))
    C = acos(-cos(A) * cos(B) + sin(A) * sin(B) * cos(c))
    A = findQuadrant(sin(A), cos(A))
    b = findQuadrant(sin(b), cos(b))
    C = findQuadrant(sin(C), cos(C))
    b = degrees(b)
    A = degrees(A)
    C = degrees(C)
    
    return b, A, C
print(SAS(106, 114, 42))


