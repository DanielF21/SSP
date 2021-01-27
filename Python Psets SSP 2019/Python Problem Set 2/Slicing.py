# starter code for exercise 0 on programming homework 2

import numpy as np

fruits = np.array([["Apple","Banana","Blueberry","Cherry"],
["Coconut","Grapefruit","Kumquat","Mango"],
["Nectarine","Orange","Tangerine","Pomegranate"],
["Lemon","Raspberry","Strawberry","Tomato"]])

print(fruits)
tomato = fruits[-1, -1]
print(tomato)
print("----------")
middle = fruits[1:3, 1:3]
print(middle)
print("----------")
firstthird = fruits[::2, ::]
print(firstthird)
print("----------")
middleinverted = fruits[-2:-4:-1, -2:-4:-1]
print(middleinverted)
print("----------")
fFirst = fruits[::,0:1:1].copy()
print(fFirst)
fLast = fruits[::,3::].copy()
fruits[::,0:1:1] = fLast
fruits[::,3::] = fFirst
print(fruits)
print("----------")
fruits[::,::] = "SLICED!"
print(fruits)
