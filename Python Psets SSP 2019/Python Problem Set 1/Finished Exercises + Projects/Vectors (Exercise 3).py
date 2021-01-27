from math import *

# part a 
def mag(vector):
    Sum = 0
    sqrtSum = 0
    if vector == []:
        print("[]")
    for i in vector:
        newI = pow(i,2)
        Sum += newI
        sqrtSum = sqrt(Sum)
    return sqrtSum

print(mag([]))
print(mag([1,1,1,1]))

# part b

def dot(vector1, vector2):
    SumDot = 0
    for i in range(len(vector1)):
        y = vector1[i] * vector2[i]
        SumDot += y
    return SumDot

print(dot([2,5,6],[3,7,8]))

# part c

def cross(vector1, vector2):
    SumCross = 0
    for i in range(len(vector1)):
        x = vector1[1] * vector2[2] - vector1[2] * vector2[1]
        y = (vector1[2] * vector2[0] - vector1[0] * vector2[2]) * -1
        z = vector1[0] * vector2[1] - vector1[1] * vector2[0]
        Sum = x + y + z
        list = [x,y,z]
    return list


print(cross([1,0,0],[0,1,0]))
print(cross([1,0,0],[0,0,1]))
print(cross([2,5,6],[3,7,8]))
