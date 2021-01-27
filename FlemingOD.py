from math import *
import numpy as np

'''

Inputs: Three R Vectors from JPL
        RA and DEC from three individual observations
        Julian Dates of the Observations



import time

for i in range(1):
    print("      ⣀⣤ \n ⠀⠀⠀⠀⣿⠿⣶ \n ⠀⠀⠀⠀⣿⣿⣀ \n ⠀⠀⠀⣶⣶⣿⠿⠛⣶ \n ⠤⣀⠛⣿⣿⣿⣿⣿⣿⣭⣿⣤ \n ⠒⠀⠀⠀⠉⣿⣿⣿⣿⠀⠀⠉⣀ \n ⠀⠤⣤⣤⣀⣿⣿⣿⣿⣀⠀⠀⣿ \n ⠀⠀⠛⣿⣿⣿⣿⣿⣿⣿⣭⣶⠉ \n ⠀⠀⠀⠤⣿⣿⣿⣿⣿⣿⣿ \n ⠀⠀⠀⣭⣿⣿⣿⠀⣿⣿⣿ \n ⠀⠀⠀⣉⣿⣿⠿⠀⠿⣿⣿ \n ⠀⠀⠀⠀⣿⣿⠀⠀⠀⣿⣿⣤ \n ⠀⠀⠀⣀⣿⣿⠀⠀⠀⣿⣿⣿ \n ⠀⠀⠀⣿⣿⣿⠀⠀⠀⣿⣿⣿ \n ⠀⠀⠀⣿⣿⠛⠀⠀⠀⠉⣿⣿ \n ⠀⠀⠀⠉⣿⠀⠀⠀⠀⠀⠛⣿ \n ⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⣿⣿ \n ⠀⠀⠀⠀⣛⠀⠀⠀⠀⠀⠀⠛⠿⠿⠿ \n ⠀⠀⠀⠛⠛ \n ")

    time.sleep(0.12)
    print("     ⣀⣶⣀ \n ⠀⠀⠀⠒⣛⣭ \n ⠀⠀⠀⣀⠿⣿⣶ \n ⠀⣤⣿⠤⣭⣿⣿ \n ⣤⣿⣿⣿⠛⣿⣿⠀⣀ \n ⠀⣀⠤⣿⣿⣶⣤⣒⣛ \n ⠉⠀⣀⣿⣿⣿⣿⣭⠉ \n ⠀⠀⣭⣿⣿⠿⠿⣿ \n ⠀⣶⣿⣿⠛⠀⣿⣿ \n ⣤⣿⣿⠉⠤⣿⣿⠿ \n ⣿⣿⠛⠀⠿⣿⣿ \n ⣿⣿⣤⠀⣿⣿⠿ \n ⠀⣿⣿⣶⠀⣿⣿⣶ \n ⠀⠀⠛⣿⠀⠿⣿⣿ \n ⠀⠀⠀⣉⣿⠀⣿⣿ \n ⠀⠶⣶⠿⠛⠀⠉⣿ \n ⠀⠀⠀⠀⠀⠀⣀⣿ \n ⠀⠀⠀⠀⠀⣶⣿⠿ \n ")

    time.sleep(0.12)
    print("           ⣤⣿⣿⠶⠀⠀⣀⣀ \n ⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣶⣿⣿⣿⣿⣿⣿ \n ⠀⠀⣀⣶⣤⣤⠿⠶⠿⠿⠿⣿⣿⣿⣉⣿⣿ \n ⠿⣉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⣤⣿⣿⣿⣀ \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣿⣶⣤ \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⣿⣿⠿⣛⣿ \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠛⣿⣿⣿⣿ \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿⣿⠿⠀⣿⣿⣿⠛ \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠀⠀⣿⣿⣿ \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⠿⣿⠀⠀⣿⣶ \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠛⠀⠀⣿⣿⣶ \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⠤ \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⣿ \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿ \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣀ \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿ \n")
    time.sleep(0.12)
    print(" ⠀⣀ \n ⠀⠿⣿⣿⣀ \n ⠀⠉⣿⣿⣀ \n ⠀⠀⠛⣿⣭⣀⣀⣤ \n ⠀⠀⣿⣿⣿⣿⣿⠛⠿⣶⣀ \n ⠀⣿⣿⣿⣿⣿⣿⠀⠀⠀⣉⣶ \n ⠀⠀⠉⣿⣿⣿⣿⣀⠀⠀⣿⠉ \n ⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿ \n ⠀⣀⣿⣿⣿⣿⣿⣿⣿⣿⠿ \n ⠀⣿⣿⣿⠿⠉⣿⣿⣿⣿ \n ⠀⣿⣿⠿⠀⠀⣿⣿⣿⣿ \n ⣶⣿⣿⠀⠀⠀⠀⣿⣿⣿ \n ⠛⣿⣿⣀⠀⠀⠀⣿⣿⣿⣿⣶⣀ \n ⠀⣿⣿⠉⠀⠀⠀⠉⠉⠉⠛⠛⠿⣿⣶ \n ⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿ \n ⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉ \n ⣀⣶⣿⠛ \n ")
    time.sleep(0.12)
    #
    print("         ⣀⣀ \n         ⣿⣿⣿⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤⣿ \n         ⠉⣿⣿⣿⣶⣿⣿⣿⣶⣶⣤⣶⣶⠶⠛⠉⠉ \n         ⣤⣿⠿⣿⣿⣿⣿⣿⠀⠀⠉ \n⠛⣿⣤⣤⣀⣤⠿⠉⠀⠉⣿⣿⣿⣿ \n⠀⠉⠉⠉⠉⠉⠀⠀⠀⠀⠉⣿⣿⣿⣀⠀\n ⠀   ⠀⠀    ⣶⣿⣿⣿⣿⣿⠀\n          ⠀⣿⣿⣿⣿⣿⣿⣿ \n ⠀⠀⠀    ⠀⠀⣿⣿⣿⣿⣿⣿⠛⠀\n ⠀⠀        ⣿⣿⣿⣿⣿⣿⠀\n⠀          ⣿⣿⣛⣿⣿⠀\n        ⠀⣶⣿⣿⠛⠿⣿⣿⣿⣶⣤⠀\n      ⠀⠀⠀⣿⠛⠉⠀⠀⠀⠛⠿⣿⣿⣶⣀⠀\n⠀⠀ ⠀    ⠀⣿⣀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⣶⣤⠀\n         ⠛⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿⣿⠿⠀\n ⠀⠀⠀⠀        ⠀⠀⠀⠀       ⠛⠉⠉⠀\n")
    time.sleep(0.12)
    print("⠀⠀⠀⠀ ⠀⠀⣤⣶⣶ \n ⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣀⣀ \n ⠀⠀⠀⠀⠀⣀⣶⣿⣿⣿⣿⣿⣿ \n ⣤⣶⣀⠿⠶⣿⣿⣿⠿⣿⣿⣿⣿ \n ⠉⠿⣿⣿⠿⠛⠉⠀⣿⣿⣿⣿⣿ \n ⠀⠀⠉⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣤⣤ \n ⠀⠀⠀⠀⠀⠀⠀⣤⣶⣿⣿⣿⣿⣿⣿ \n ⠀⠀⠀⠀⠀⣀⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿ \n ⠀⠀⠀⠀⣀⣿⣿⣿⠿⠉⠀⠀⣿⣿⣿⣿ \n ⠀⠀⠀⠀⣿⣿⠿⠉⠀⠀⠀⠀⠿⣿⣿⠛ \n ⠀⠀⠀⠀⠛⣿⣿⣀⠀⠀⠀⠀⠀⣿⣿⣀ \n ⠀⠀⠀⠀⠀⣿⣿⣿⠀⠀⠀⠀⠀⠿⣿⣿ \n ⠀  ⠀⠀⠉⣿⣿⠀⠀⠀⠀⠀⠀⠉⣿ \n ⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⣀⣿ \n ⠀⠀⠀⠀⠀⠀⣀⣿⣿ \n ⠀⠀⠀⠀⠤⣿⠿⠿⠿ \n")
    time.sleep(0.12)
    print("⠀⠀  ⠀⣀ \n ⠀⠀⣶⣿⠿⠀⠀⠀⣀⠀⣤⣤ \n ⠀⣶⣿⠀⠀⠀⠀⣿⣿⣿⠛⠛⠿⣤⣀ \n ⣶⣿⣤⣤⣤⣤⣤⣿⣿⣿⣀⣤⣶⣭⣿⣶⣀ \n ⠉⠉⠉⠛⠛⠿⣿⣿⣿⣿⣿⣿⣿⠛⠛⠿⠿ \n ⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⠿ \n ⠀⠀⠀⠀⠀⠀⠀⠿⣿⣿⣿⣿ \n ⠀⠀⠀⠀⠀⠀⠀⠀⣭⣿⣿⣿⣿⣿ \n ⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⣿⣿⣿⣿ \n ⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⠿ \n ⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⠿ \n ⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿ \n ⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣿ \n ⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣿ \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⠛⠿⣿⣤ \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿⠀⠀⠀⣿⣿⣤ \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⣶⣿⠛⠉ \n ⠀⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⠀⠀⠉ \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉ \n")
    time.sleep(0.12)
    print("⠀⠀⠀⠀ ⠀⠀⣶⣿⣶ \n ⠀⠀⠀⣤⣤⣤⣿⣿⣿ \n ⠀⠀⣶⣿⣿⣿⣿⣿⣿⣿⣶ \n ⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿ \n ⠀⠀⣿⣉⣿⣿⣿⣿⣉⠉⣿⣶ \n ⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿ \n ⠀⣤⣿⣿⣿⣿⣿⣿⣿⠿⠀⣿⣶ \n ⣤⣿⠿⣿⣿⣿⣿⣿⠿⠀⠀⣿⣿⣤ \n ⠉⠉⠀⣿⣿⣿⣿⣿⠀⠀⠒⠛⠿⠿⠿ \n ⠀⠀⠀⠉⣿⣿⣿⠀⠀⠀⠀⠀⠀⠉ \n ⠀⠀⠀⣿⣿⣿⣿⣿⣶ \n ⠀⠀⠀⠀⣿⠉⠿⣿⣿ \n ⠀⠀⠀⠀⣿⣤⠀⠛⣿⣿ \n ⠀⠀⠀⠀⣶⣿⠀⠀⠀⣿⣶ \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣭⣿⣿ \n ⠀⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⠉ \n")
    time.sleep(0.12)
    print("⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⣤⣶ \n ⠀⠀⠀⠀⠀⣀⣀⠀⣶⣿⣿⠶ \n ⣶⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣤ \n ⠀⠉⠶⣶⣀⣿⣿⣿⣿⣿⣿⣿⠿⣿⣤⣀ \n ⠀⠀⠀⣿⣿⠿⠉⣿⣿⣿⣿⣭⠀⠶⠿⠿ \n ⠀⠀⠛⠛⠿⠀⠀⣿⣿⣿⣉⠿⣿⠶ \n ⠀⠀⠀⠀⠀⣤⣶⣿⣿⣿⣿⣿ \n ⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⠒ \n ⠀⠀⠀⠀⣀⣿⣿⣿⣿⣿⣿⣿ \n ⠀⠀⠀⠀⠀⣿⣿⣿⠛⣭⣭⠉ \n ⠀⠀⠀⠀⠀⣿⣿⣭⣤⣿⠛ \n ⠀⠀⠀⠀⠀⠛⠿⣿⣿⣿⣭ \n ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠉⠛⠿⣶⣤ \n ⠀⠀⠀⠀⠀⠀⣀⣿⠀⠀⣶⣶⠿⠿⠿ \n ⠀⠀⠀⠀⠀⠀⣿⠛ \n ⠀⠀⠀⠀⠀⠀⣭⣶ \n")

    time.sleep(0.12)
    print("           ⣤⣿⣿⠶⠀⠀⣀⣀ \n ⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣶⣿⣿⣿⣿⣿⣿ \n ⠀⠀⣀⣶⣤⣤⠿⠶⠿⠿⠿⣿⣿⣿⣉⣿⣿ \n ⠿⣉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⣤⣿⣿⣿⣀ \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣿⣶⣤ \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⣿⣿⠿⣛⣿ \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠛⣿⣿⣿⣿ \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿⣿⠿⠀⣿⣿⣿⠛ \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠀⠀⣿⣿⣿ \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⠿⣿⠀⠀⣿⣶ \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠛⠀⠀⣿⣿⣶ \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⠤ \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⣿ \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿ \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣀ \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿ \n")
    time.sleep(0.12)
    print(" ⠀⣀ \n ⠀⠿⣿⣿⣀ \n ⠀⠉⣿⣿⣀ \n ⠀⠀⠛⣿⣭⣀⣀⣤ \n ⠀⠀⣿⣿⣿⣿⣿⠛⠿⣶⣀ \n ⠀⣿⣿⣿⣿⣿⣿⠀⠀⠀⣉⣶ \n ⠀⠀⠉⣿⣿⣿⣿⣀⠀⠀⣿⠉ \n ⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿ \n ⠀⣀⣿⣿⣿⣿⣿⣿⣿⣿⠿ \n ⠀⣿⣿⣿⠿⠉⣿⣿⣿⣿ \n ⠀⣿⣿⠿⠀⠀⣿⣿⣿⣿ \n ⣶⣿⣿⠀⠀⠀⠀⣿⣿⣿ \n ⠛⣿⣿⣀⠀⠀⠀⣿⣿⣿⣿⣶⣀ \n ⠀⣿⣿⠉⠀⠀⠀⠉⠉⠉⠛⠛⠿⣿⣶ \n ⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿ \n ⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉ \n ⣀⣶⣿⠛ \n ")
    time.sleep(0.12)
    #
    print("         ⣀⣀ \n         ⣿⣿⣿⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤⣿ \n         ⠉⣿⣿⣿⣶⣿⣿⣿⣶⣶⣤⣶⣶⠶⠛⠉⠉ \n         ⣤⣿⠿⣿⣿⣿⣿⣿⠀⠀⠉ \n⠛⣿⣤⣤⣀⣤⠿⠉⠀⠉⣿⣿⣿⣿ \n⠀⠉⠉⠉⠉⠉⠀⠀⠀⠀⠉⣿⣿⣿⣀⠀\n ⠀   ⠀⠀    ⣶⣿⣿⣿⣿⣿⠀\n          ⠀⣿⣿⣿⣿⣿⣿⣿ \n ⠀⠀⠀    ⠀⠀⣿⣿⣿⣿⣿⣿⠛⠀\n ⠀⠀        ⣿⣿⣿⣿⣿⣿⠀\n⠀          ⣿⣿⣛⣿⣿⠀\n        ⠀⣶⣿⣿⠛⠿⣿⣿⣿⣶⣤⠀\n      ⠀⠀⠀⣿⠛⠉⠀⠀⠀⠛⠿⣿⣿⣶⣀⠀\n⠀⠀ ⠀    ⠀⣿⣀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⣶⣤⠀\n         ⠛⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿⣿⠿⠀\n ⠀⠀⠀⠀        ⠀⠀⠀⠀       ⠛⠉⠉⠀\n")
    time.sleep(0.12)
    print("⠀⠀⠀⠀ ⠀⠀⣤⣶⣶ \n ⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣀⣀ \n ⠀⠀⠀⠀⠀⣀⣶⣿⣿⣿⣿⣿⣿ \n ⣤⣶⣀⠿⠶⣿⣿⣿⠿⣿⣿⣿⣿ \n ⠉⠿⣿⣿⠿⠛⠉⠀⣿⣿⣿⣿⣿ \n ⠀⠀⠉⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣤⣤ \n ⠀⠀⠀⠀⠀⠀⠀⣤⣶⣿⣿⣿⣿⣿⣿ \n ⠀⠀⠀⠀⠀⣀⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿ \n ⠀⠀⠀⠀⣀⣿⣿⣿⠿⠉⠀⠀⣿⣿⣿⣿ \n ⠀⠀⠀⠀⣿⣿⠿⠉⠀⠀⠀⠀⠿⣿⣿⠛ \n ⠀⠀⠀⠀⠛⣿⣿⣀⠀⠀⠀⠀⠀⣿⣿⣀ \n ⠀⠀⠀⠀⠀⣿⣿⣿⠀⠀⠀⠀⠀⠿⣿⣿ \n ⠀  ⠀⠀⠉⣿⣿⠀⠀⠀⠀⠀⠀⠉⣿ \n ⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⣀⣿ \n ⠀⠀⠀⠀⠀⠀⣀⣿⣿ \n ⠀⠀⠀⠀⠤⣿⠿⠿⠿ \n")
    time.sleep(0.12)
    print("⠀⠀  ⠀⣀ \n ⠀⠀⣶⣿⠿⠀⠀⠀⣀⠀⣤⣤ \n ⠀⣶⣿⠀⠀⠀⠀⣿⣿⣿⠛⠛⠿⣤⣀ \n ⣶⣿⣤⣤⣤⣤⣤⣿⣿⣿⣀⣤⣶⣭⣿⣶⣀ \n ⠉⠉⠉⠛⠛⠿⣿⣿⣿⣿⣿⣿⣿⠛⠛⠿⠿ \n ⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⠿ \n ⠀⠀⠀⠀⠀⠀⠀⠿⣿⣿⣿⣿ \n ⠀⠀⠀⠀⠀⠀⠀⠀⣭⣿⣿⣿⣿⣿ \n ⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⣿⣿⣿⣿ \n ⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⠿ \n ⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⠿ \n ⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿ \n ⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣿ \n ⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣿ \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⠛⠿⣿⣤ \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿⠀⠀⠀⣿⣿⣤ \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⣶⣿⠛⠉ \n ⠀⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⠀⠀⠉ \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉ \n")
    time.sleep(0.12)
    print("⠀⠀⠀⠀ ⠀⠀⣶⣿⣶ \n ⠀⠀⠀⣤⣤⣤⣿⣿⣿ \n ⠀⠀⣶⣿⣿⣿⣿⣿⣿⣿⣶ \n ⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿ \n ⠀⠀⣿⣉⣿⣿⣿⣿⣉⠉⣿⣶ \n ⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿ \n ⠀⣤⣿⣿⣿⣿⣿⣿⣿⠿⠀⣿⣶ \n ⣤⣿⠿⣿⣿⣿⣿⣿⠿⠀⠀⣿⣿⣤ \n ⠉⠉⠀⣿⣿⣿⣿⣿⠀⠀⠒⠛⠿⠿⠿ \n ⠀⠀⠀⠉⣿⣿⣿⠀⠀⠀⠀⠀⠀⠉ \n ⠀⠀⠀⣿⣿⣿⣿⣿⣶ \n ⠀⠀⠀⠀⣿⠉⠿⣿⣿ \n ⠀⠀⠀⠀⣿⣤⠀⠛⣿⣿ \n ⠀⠀⠀⠀⣶⣿⠀⠀⠀⣿⣶ \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣭⣿⣿ \n ⠀⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⠉ \n")
    time.sleep(0.12)
    print("⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⣤⣶ \n ⠀⠀⠀⠀⠀⣀⣀⠀⣶⣿⣿⠶ \n ⣶⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣤ \n ⠀⠉⠶⣶⣀⣿⣿⣿⣿⣿⣿⣿⠿⣿⣤⣀ \n ⠀⠀⠀⣿⣿⠿⠉⣿⣿⣿⣿⣭⠀⠶⠿⠿ \n ⠀⠀⠛⠛⠿⠀⠀⣿⣿⣿⣉⠿⣿⠶ \n ⠀⠀⠀⠀⠀⣤⣶⣿⣿⣿⣿⣿ \n ⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⠒ \n ⠀⠀⠀⠀⣀⣿⣿⣿⣿⣿⣿⣿ \n ⠀⠀⠀⠀⠀⣿⣿⣿⠛⣭⣭⠉ \n ⠀⠀⠀⠀⠀⣿⣿⣭⣤⣿⠛ \n ⠀⠀⠀⠀⠀⠛⠿⣿⣿⣿⣭ \n ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠉⠛⠿⣶⣤ \n ⠀⠀⠀⠀⠀⠀⣀⣿⠀⠀⣶⣶⠿⠿⠿ \n ⠀⠀⠀⠀⠀⠀⣿⠛ \n ⠀⠀⠀⠀⠀⠀⣭⣶ \n")


    time.sleep(0.12)
    print("⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⣤⣤ \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿ \n ⠀⠀⣶⠀⠀⣀⣤⣶⣤⣉⣿⣿⣤⣀ \n ⠤⣤⣿⣤⣿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣀ \n ⠀⠛⠿⠀⠀⠀⠀⠉⣿⣿⣿⣿⣿⠉⠛⠿⣿⣤ \n ⠀⠀⠀⠀⠀⠀⠀⠀⠿⣿⣿⣿⠛⠀⠀⠀⣶⠿ \n ⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿⣿⣿⣿⣤⠀⣿⠿ \n ⠀⠀⠀⠀⠀⠀⠀⣶⣿⣿⣿⣿⣿⣿⣿⣿ \n ⠀⠀⠀⠀⠀⠀⠀⠿⣿⣿⣿⣿⣿⠿⠉⠉ \n ⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣿⠿ \n ⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠉ \n ⠀⠀⠀⠀⠀⠀⠀⠀⣛⣿⣭⣶⣀ \n ⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿ \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠉⠛⣿ \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⣿⣿ \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣉⠀⣶⠿ \n ⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿⠿ \n ⠀⠀⠀⠀⠀⠀⠀⠛⠿⠛ \n")
    time.sleep(0.12)
    print("⠀   ⣶⣿⣶ \n ⠀⠀⠀⣿⣿⣿⣀ \n ⠀⣀⣿⣿⣿⣿⣿⣿ \n ⣶⣿⠛⣭⣿⣿⣿⣿ \n ⠛⠛⠛⣿⣿⣿⣿⠿ \n ⠀⠀⠀⠀⣿⣿⣿ \n ⠀⠀⣀⣭⣿⣿⣿⣿⣀ \n ⠀⠤⣿⣿⣿⣿⣿⣿⠉ \n ⠀⣿⣿⣿⣿⣿⣿⠉ \n ⣿⣿⣿⣿⣿⣿ \n ⣿⣿⣶⣿⣿ \n ⠉⠛⣿⣿⣶⣤ \n ⠀⠀⠉⠿⣿⣿⣤ \n ⠀⠀⣀⣤⣿⣿⣿ \n ⠀⠒⠿⠛⠉⠿⣿ \n ⠀⠀⠀⠀⠀⣀⣿⣿ \n ⠀⠀⠀⠀⣶⠿⠿⠛ \n")
'''
k = 0.01720209895
mu = 1
speed_of_light = 173.145

def convertRa(raHours):
    raDegrees = 0
    raSplit = [float(x) for x in raHours.split(":")]
    raDegrees = raSplit[0] * 15 + raSplit[1] * 15 /60 + raSplit[2] * 15 / 3600
    if raSplit[0] < 0:
        raDegrees = raSplit[0] * 15 - raSplit[1] * 15 / 60 - raSplit[2] * 15 / 3600
    return raDegrees

#print(convertRa("19:10:27.78"))

def convertDec(dec):
        decDegrees = 0
        decSplit = [float(x) for x in dec.split(":")]
        decDegrees = decSplit[0] + decSplit[1] / 60 + decSplit[2] / 3600
        if decSplit[0] < 0:
            decDegrees = decSplit[0] - decSplit[1] / 60 - decSplit[2] / 3600
        return decDegrees
    
##print(convertDec("35:36:18.0"))
print("I did not make the dance. I just thought it would be fun to put it in. Credits to @DaviDEW")
middle_obs = input("Middle Obsevation?: ")
yes = input("Yes? (1 for yes, 0 for no)")

def OD(filename):
    RaList = []
    DecList = []
    JulianList = []
    R_Vector_List_1 = []
    R_Vector_List_2 = []
    R_Vector_List_3 = []
    x = []
    y = []
    z = []
    input = open(filename, 'r')
    for line in input.readlines():
        row = line.split()
        if len(row) > 0:
            JulianList.append(float(row[0]))
            RaList.append(float(convertRa(row[1])))
            DecList.append(float(convertDec(row[2])))
            x.append(float((row[3])))
            y.append(float((row[4])))
            z.append(float((row[5])))

            
    print("X STUFF", x)
    print("Y STUFF", y)
    print("Z STUFF", z)

    if yes == 1:
        if middle_obs == 2:
            R_Vector_List_1.append(x[0])
            R_Vector_List_1.append(y[0])
            R_Vector_List_1.append(z[0])
            R_Vector_List_2.append(x[1])
            R_Vector_List_2.append(y[1])
            R_Vector_List_2.append(z[1])
            R_Vector_List_3.append(x[4])
            R_Vector_List_3.append(y[4])
            R_Vector_List_3.append(z[4])
        elif middle_obs == 3:
            R_Vector_List_1.append(x[0])
            R_Vector_List_1.append(y[0])
            R_Vector_List_1.append(z[0])
            R_Vector_List_2.append(x[2])
            R_Vector_List_2.append(y[2])
            R_Vector_List_2.append(z[2])
            R_Vector_List_3.append(x[4])
            R_Vector_List_3.append(y[4])
            R_Vector_List_3.append(z[4])   
        else:
            R_Vector_List_1.append(x[0])
            R_Vector_List_1.append(y[0])
            R_Vector_List_1.append(z[0])
            R_Vector_List_2.append(x[3])
            R_Vector_List_2.append(y[3])
            R_Vector_List_2.append(z[3])
            R_Vector_List_3.append(x[4])
            R_Vector_List_3.append(y[4])
            R_Vector_List_3.append(z[4])
    else:
        R_Vector_List_1.append(x[0])
        R_Vector_List_1.append(y[0])
        R_Vector_List_1.append(z[0])
        R_Vector_List_2.append(x[1])
        R_Vector_List_2.append(y[1])
        R_Vector_List_2.append(z[1])
        R_Vector_List_3.append(x[2])
        R_Vector_List_3.append(y[2])
        R_Vector_List_3.append(z[2])
            
    print("RaList", RaList)
    print("DecList", DecList)
    print("JulianList", JulianList)
    print("R_Vector_List_1", R_Vector_List_1)
    print("R_Vector_List_2", R_Vector_List_2)
    print("R_Vector_List_3", R_Vector_List_3)
    print("----------------------------------------------------------------------------")
    
    RaList_Radians = []
    DecList_Radians = []

    for i in range(len(RaList)):
        variable = radians(RaList[i])
        RaList_Radians.append(variable)

    for i in range(len(DecList)):
        variable = radians(DecList[i])
        DecList_Radians.append(variable)

    print("RaList_Radians", RaList_Radians)
    print("DecList_Radians", DecList_Radians)
    print("----------------------------------------------------------------------------")
    
    Obliquity = radians(23.4358)
    transform = np.array([[1,0,0],[0,cos(Obliquity), sin(Obliquity)],[0, -sin(Obliquity), cos(Obliquity)]])

    rho_hat_1 = [cos(RaList_Radians[0]) * cos(DecList_Radians[0]), sin(RaList_Radians[0]) * cos(DecList_Radians[0]), sin(DecList_Radians[0])]                
    rho_hat_2 = [cos(RaList_Radians[1]) * cos(DecList_Radians[1]), sin(RaList_Radians[1]) * cos(DecList_Radians[1]), sin(DecList_Radians[1])]
    rho_hat_3 = [cos(RaList_Radians[2]) * cos(DecList_Radians[2]), sin(RaList_Radians[2]) * cos(DecList_Radians[2]), sin(DecList_Radians[2])]

    rho_hat_1_ecliptic = [rho_hat_1[0], rho_hat_1[1] * cos(Obliquity) + rho_hat_1[2] * sin(Obliquity), -rho_hat_1[1] * sin(Obliquity) + rho_hat_1[2] * cos(Obliquity)]
    rho_hat_2_ecliptic = [rho_hat_2[0], rho_hat_2[1] * cos(Obliquity) + rho_hat_2[2] * sin(Obliquity), -rho_hat_2[1] * sin(Obliquity) + rho_hat_2[2] * cos(Obliquity)]
    rho_hat_3_ecliptic = [rho_hat_3[0], rho_hat_3[1] * cos(Obliquity) + rho_hat_3[2] * sin(Obliquity), -rho_hat_3[1] * sin(Obliquity) + rho_hat_3[2] * cos(Obliquity)]

##    rho_hat_1_ecliptic = np.matmul(transform, rho_hat_1)
##    rho_hat_2_ecliptic = np.matmul(transform, rho_hat_2)
##    rho_hat_3_ecliptic = np.matmul(transform, rho_hat_3)
    
    print("Rho Hat 1 Ecliptic", rho_hat_1_ecliptic)
    print("Rho Hat 2 Ecliptic", rho_hat_2_ecliptic)
    print("Rho Hat 3 Ecliptic", rho_hat_3_ecliptic)
    print("----------------------------------------------------------------------------")


#Finding Initial Tau Values


    Tau3 = k * (JulianList[2] - JulianList[1])
    Tau1 = k * (JulianList[0] - JulianList[1])
    Tau = Tau3 - Tau1
    

    print("Tau1", Tau1)
    print("Tau3", Tau3)
    print("Tau", Tau)
    print("----------------------------------------------------------------------------")


#Define A1 A3 B1 B3
    

    A1 = Tau3 / Tau

    A3 = -Tau1 / Tau

    B1 = (A1 / 6) * (Tau**2 - Tau3**2)
    
    B3 = (A3 / 6) * (Tau**2 - Tau1**2)

    print("A1", A1)
    print("A3", A3)
    print("B1", B1)
    print("B3", B3)
    print("----------------------------------------------------------------------------")


#Define E and F
    

    E = -2 * np.dot(rho_hat_2_ecliptic, R_Vector_List_2)
    
    F = np.linalg.norm(R_Vector_List_2)**2

    print("E", E)
    print("F", F)
    

#Define all the Ds
    
    
    D0 = np.dot(rho_hat_1_ecliptic, np.cross(rho_hat_2_ecliptic, rho_hat_3_ecliptic))
    D11 = np.dot(np.cross(R_Vector_List_1, rho_hat_2_ecliptic), rho_hat_3_ecliptic)
    D12 = np.dot(np.cross(R_Vector_List_2, rho_hat_2_ecliptic), rho_hat_3_ecliptic)
    D13 = np.dot(np.cross(R_Vector_List_3, rho_hat_2_ecliptic), rho_hat_3_ecliptic)
    D21 = np.dot(np.cross(rho_hat_1_ecliptic, R_Vector_List_1), rho_hat_3_ecliptic)
    D22 = np.dot(np.cross(rho_hat_1_ecliptic, R_Vector_List_2), rho_hat_3_ecliptic)
    D23 = np.dot(np.cross(rho_hat_1_ecliptic, R_Vector_List_3), rho_hat_3_ecliptic)
    D31 = np.dot(rho_hat_1_ecliptic, np.cross(rho_hat_2_ecliptic, R_Vector_List_1))
    D32 = np.dot(rho_hat_1_ecliptic, np.cross(rho_hat_2_ecliptic, R_Vector_List_2))
    D33 = np.dot(rho_hat_1_ecliptic, np.cross(rho_hat_2_ecliptic, R_Vector_List_3))
    
    print("----------------------------------------------------------------------------")

    print("D", D0, D11, D12, D13, D21, D22, D23, D31, D32, D33)

    print("----------------------------------------------------------------------------")


#Define A and B
    

    A = (A1 * D21 - D22 + A3 * D23) / (-D0)
    B = (B1 * D21 + B3 * D23) / (-D0)
    

    print("A", A)
    print("B", B)
    print("----------------------------------------------------------------------------")
    
    
#Define a, b, and c
    

    a = -(A**2 + A * E + F)
    b = -mu * (2 * A * B + B * E)
    c = -mu**2 * B**2
    

    print("a", a)
    print("b", b)
    print("c", c)
    print("----------------------------------------------------------------------------")
    
    
#Solve for Initial R2
    

    print("roots")
    polynomial = [1,0,a,0,0,b,0,0,c]
    poly = np.poly1d(polynomial)
    print(np.roots(poly))
    roots = (np.roots(poly))
    RealPositiveRoots = []

    for i in range(len(roots)):
        if roots[i] > 0 and np.iscomplex(roots[i]) == False:
            print(roots[i])
            RealPositiveRoots.append(np.real(roots[i]))

    OnlyRoot = RealPositiveRoots[0]
            
    print("----------------------------------------------------------------------------")
    

#Solve for f and g series

    u = (mu/(OnlyRoot**3))

    f_series1 = 1 - (u * (Tau1**2))/2
    f_series3 = 1 - (u * (Tau3**2))/2
    g_series1 = Tau1 - (u * (Tau1**3))/6
    g_series3 = Tau3 - (u * (Tau3**3))/6
    

    print("f and g series")
    print(f_series1)
    print(f_series3)
    print(g_series1)
    print(g_series3)
    print(f_series1.shape)
    print("----------------------------------------------------------------------------")
    
    
#Solve for c1 and c3
    

    c_denominator = f_series1 * g_series3 - g_series1 * f_series3
    c1 = g_series3 / c_denominator
    c3 = -g_series1 / c_denominator
    c2 = -1
    
    
    print("c1", c1)
    print("c3", c3)
    print("----------------------------------------------------------------------------")


#Solve for rho vector
    
    
    rho_mag_1_ecliptic = (c1 * D11 + c2 * D12 + c3 * D13)/(c1 * D0)
    rho_mag_2_ecliptic = (c1 * D21 + c2 * D22 + c3 * D23)/(c2 * D0)
    rho_mag_3_ecliptic = (c1 * D31 + c2 * D32 + c3 * D33)/(c3 * D0)

    print("rho mag 1", rho_mag_1_ecliptic)
    print("rho mag 2", rho_mag_2_ecliptic)
    print("rho mag 3", rho_mag_3_ecliptic)
    print("----------------------------------------------------------------------------")
    

    rho_vector_1 = np.multiply(rho_mag_1_ecliptic, rho_hat_1_ecliptic)
    rho_vector_2 = np.multiply(rho_mag_2_ecliptic, rho_hat_2_ecliptic)
    rho_vector_3 = np.multiply(rho_mag_3_ecliptic, rho_hat_3_ecliptic)

    print("rho vector 1", rho_vector_1)
    print("rho vector 2", rho_vector_2)
    print("rho vector 3", rho_vector_3)
    print("----------------------------------------------------------------------------")
    

#Solve for the r2 vector

    r1_vector = rho_vector_1 - R_Vector_List_1
    r2_vector = rho_vector_2 - R_Vector_List_2
    r3_vector = rho_vector_3 - R_Vector_List_3
    
    print("R2 Vector", r2_vector)
    print("----------------------------------------------------------------------------")
    
#Solve for the r2 dot vector (will need d1 and d3 values)

    d1 = -f_series3 / c_denominator
    d3 = f_series1 / c_denominator
    r2_dot_vector = d1 * r1_vector + d3 * r3_vector

    print("d1 and d3", d1, d3)
    
    print("R2 Dot Vector",r2_dot_vector)
    print("----------------------------------------------------------------------------")

#Correct for light travel time

    t1_new = JulianList[0] - (rho_mag_1_ecliptic/speed_of_light)
    t2_new = JulianList[1] - (rho_mag_2_ecliptic/speed_of_light)
    t3_new = JulianList[2] - (rho_mag_3_ecliptic/speed_of_light)

    Tau1_New = k * (t1_new - t2_new)
    Tau3_New = k * (t3_new - t2_new)
    Tau_New = Tau3_New - Tau1_New

    print("Initially Corrected Tau", Tau1_New, Tau3_New, Tau_New)
    print("----------------------------------------------------------------------------")

    print("r2 vector", r2_vector)

#Iteration Time :)
    
    iteration_r2_vector = [0,0,0]
    check = [0,0,0]
    
    while abs(np.linalg.norm(check) - np.linalg.norm(r2_vector)) > 1e-8:

        check = r2_vector
        
        #Solve for f and g series in the iteration     

        u = (mu / (OnlyRoot**3))
        z = (np.dot(r2_vector, r2_dot_vector))/(OnlyRoot**2)
        q = (np.dot(r2_dot_vector, r2_dot_vector)/(OnlyRoot**2)) - u

        iteration_f_series1 = 1 - (u * Tau1_New**2)/2 + (u * z * Tau1_New**3)/2 + ((((3 * u * q) - (15 * u * z**2) + (u**2)) * Tau1_New**4)/24)
        iteration_f_series3 = 1 - (u * Tau3_New**2)/2 + (u * z * Tau3_New**3)/2 + (((3 * u * q - (15 * u * z**2) + u**2) * Tau3_New**4)/24)
        iteration_g_series1 = Tau1_New - (u * Tau1_New**3)/6 + (u * z * Tau1_New**4)/4
        iteration_g_series3 = Tau3_New - (u * Tau3_New**3)/6 + (u * z * Tau3_New**4)/4
        
##        iteration_f_series1 = 1 - (mu/(2 * OnlyRoot**3)) * (Tau1**2) + ((mu * np.dot(r2_vector, r2_dot_vector))/(2 * OnlyRoot**5)) * Tau1**3
##        iteration_f_series3 = 1 - (mu/(2 * OnlyRoot**3)) * (Tau3**2) + ((mu * np.dot(r2_vector, r2_dot_vector))/(2 * OnlyRoot**5)) * Tau3**3
##        iteration_g_series1 = Tau1 - (mu/(6 * OnlyRoot**3)) * (Tau1**3)
##        iteration_g_series3 = Tau3 - (mu/(6 * OnlyRoot**3)) * (Tau3**3)

        #Solve for c1 and c3 in the iteration
        
        iteration_c_denominator = (iteration_f_series1 * iteration_g_series3) - (iteration_g_series1 * iteration_f_series3)
        
        iteration_c1 = iteration_g_series3 / iteration_c_denominator
        
        iteration_c3 = (-1 * iteration_g_series1) / iteration_c_denominator
        
        iteration_c2 = -1
        

        #Solve for new scalar ranges in the iteration
        

        iteration_rho_mag_1_ecliptic = (iteration_c1 * D11 + iteration_c2 * D12 + iteration_c3 * D13)/(iteration_c1 * D0)
        iteration_rho_mag_2_ecliptic = (iteration_c1 * D21 + iteration_c2 * D22 + iteration_c3 * D23)/(iteration_c2 * D0)
        iteration_rho_mag_3_ecliptic = (iteration_c1 * D31 + iteration_c2 * D32 + iteration_c3 * D33)/(iteration_c3 * D0)
        

        #Sove for the new rho vector in the iteration
        

        iteration_rho_vector_1 = np.multiply(iteration_rho_mag_1_ecliptic, rho_hat_1_ecliptic)
        iteration_rho_vector_2 = np.multiply(iteration_rho_mag_2_ecliptic, rho_hat_2_ecliptic)
        iteration_rho_vector_3 = np.multiply(iteration_rho_mag_3_ecliptic, rho_hat_3_ecliptic)
        

        #Solve for the new R2 vector in the iteration
        

        iteration_r1_vector = iteration_rho_vector_1 - R_Vector_List_1
        iteration_r2_vector = iteration_rho_vector_2 - R_Vector_List_2
        iteration_r3_vector = iteration_rho_vector_3 - R_Vector_List_3
        

        #Solve for the new R2 dot vector in the iteration

        iteration_d1 = -1 * iteration_f_series3 / iteration_c_denominator
        
        iteration_d3 = iteration_f_series1 / iteration_c_denominator
        
        iteration_r2_dot_vector = np.multiply(iteration_d1, iteration_r1_vector) + np.multiply(iteration_d3, iteration_r3_vector)
        

        #Correct for light travel time in the iteration

        t1_new = JulianList[0] - (iteration_rho_mag_1_ecliptic / speed_of_light)
        t2_new = JulianList[1] - (iteration_rho_mag_2_ecliptic / speed_of_light)
        t3_new = JulianList[2] - (iteration_rho_mag_3_ecliptic / speed_of_light)

        Tau1_New = k * (t1_new - t2_new)
        Tau3_New = k * (t3_new - t2_new)
        Tau_New = Tau3_New - Tau1_New

        r2_vector = iteration_r2_vector
        r2_dot_vector = iteration_r2_dot_vector

        OnlyRoot = np.linalg.norm(r2_vector)

        print("f and g series in loop", iteration_f_series1, iteration_f_series3, iteration_g_series1, iteration_g_series3)

        print("r2 vector", iteration_r2_vector)
        print("r2 dot vector", iteration_r2_dot_vector*365.25 * k)




    # Baby OD Integrated

    t_due = 2458685.749999

    r2_vector_magnitude = np.linalg.norm(iteration_r2_vector)

    Obliquity = radians(23.4358)

    #Step 1: Get a

    a = ((2/r2_vector_magnitude) - np.dot(iteration_r2_dot_vector, iteration_r2_dot_vector))**-1

    print("-------------")
    print("A")
    print(a)
    print("-------------")

    #Step 2: Get e

    e = sqrt((1 - ((np.linalg.norm(abs(np.cross(iteration_r2_vector, iteration_r2_dot_vector)))**2)/a)))
    print("e")
    print(e)
    print("-------------")


    #Step 3: Get I

    #transform = np.array([[1,0,0],[0,cos(Obliquity), sin(Obliquity)],[0, -sin(Obliquity), cos(Obliquity)]])

    #r2_vector_ec = np.matmul(transform, iteration_r2_vector)
    r2_vector_ec = iteration_r2_vector

    #r2_dot_vector_ec = np.matmul(transform, iteration_r2_dot_vector)
    r2_dot_vector_ec = iteration_r2_dot_vector

    h = np.linalg.norm(np.cross(iteration_r2_vector, iteration_r2_dot_vector))

    hz = (r2_vector_ec[0] * r2_dot_vector_ec[1]) - (r2_vector_ec[1] * r2_dot_vector_ec[0])

    r2_vector_ec_magnitude = np.linalg.norm(r2_vector_ec)

    ##print(h)
    ##print(hz)

    I = acos(hz/h)

    print("I")
    print(degrees(I))
    print("-------------")

    #Step 4: Get Ω

    hx = (r2_vector_ec[1] * r2_dot_vector_ec[2]) - (r2_vector_ec[2] * r2_dot_vector_ec[1])

    hy = (r2_vector_ec[2] * r2_dot_vector_ec[0]) - (r2_vector_ec[0] * r2_dot_vector_ec[2])

    BigOmega = degrees(atan2((hx/h*sin(I)),(-hy/h*sin(I))))

    for i in range(10):
        if BigOmega > 360:
            BigOmega -= 360
        elif BigOmega < 0:
            BigOmega += 360

            
    print("Ω")
    print(BigOmega)
    print("-------------")

    #Step 5: Get ω

    ##print("r2 vector / ecliptic")
    ##print(r2_vector_ec[0])
    ##print(r2_vector_ec[1])
    ##print(r2_vector_ec[2])
    ##print("-----")

    Ucos = (r2_vector_ec[0] * cos(radians(BigOmega)) + r2_vector_ec[1] * sin(radians(BigOmega)))/(r2_vector_ec_magnitude)

    Usin = (r2_vector_ec[2] / ((r2_vector_ec_magnitude * sin(I))))

    U = (atan2(Usin, Ucos))

    Nucos = (((a * (1 - (e**2))/r2_vector_ec_magnitude) - 1) / (e))

    Nusin = (a * (1-e**2) * np.dot(r2_vector, r2_dot_vector)/((h * e * r2_vector_ec_magnitude)))

    Nu = atan2(Nusin, Nucos)

    SmallOmega = degrees(U - Nu)

    print ("U" , degrees(U))
    print ("Nu" , degrees(Nu))
    for i in range(10):
        if SmallOmega > 360:
            SmallOmega -= 360
        elif SmallOmega < 0:
            SmallOmega += 360

    ##SmallOmega = abs(SmallOmega) % 360
       
    print("ω")
    print(SmallOmega)
    print("-------------")

    #Step 6: Get M0 (Mean Anomaly)

    E = acos((1/e) * (1 - (r2_vector_ec_magnitude / a)))

    E2 = E

    M0 = E2 - e * sin(E2)

    print("E")
    print(degrees(E2))
    print("-------------")

    print("M0")
    print(degrees(M0))
    print("-------------")

    print("n")
    n = sqrt(0.01720209894**2/(a**3))
    print(n)
    print("-------------")

    print("P")
    P = (2 * pi)/n / 365.25
    print(P)
    print("-------------")

    print("T")
    t2 = int(middle_obs) - 1
    T = JulianList[t2] - ((M0))/n
    print(T)
    print("------------")

    print("M0 NEW")
    M0_New = M0 + n * (t_due - JulianList[t2])
    print(360 - degrees(M0_New))

print(OD("FlemingInput.txt"))

##a = 1.000001018
##e = 0.0167086
##M = radians(100.46435)
##Oprime = radians(174.9)
##iprime = radians(7.155)
##wprime = radians(102.9)
##
##def solvekep(M):
##    Eguess = M
##    Mguess = Eguess - e*sin(Eguess)
##    Mtrue = M
##    while abs(Mguess - Mtrue) > 1e-004:
##        Mguess = Eguess - e*sin(Eguess)
##        Eguess = Eguess - (Eguess - e*sin(Eguess) - Mtrue) / (1 - e*cos(Eguess))
##    return Eguess
##
##sqrtmu = 0.01720209895
##mu = sqrtmu**2
##time = 0
##dt = 0.05
##period = sqrt(4*pi**2*a**3/mu)
##r1ecliptic = vector(0, 0, 0)
##Mtrue = 2*pi/period*(time) + M
##Etrue = solvekep(Mtrue)
##r1ecliptic.x = (cos(wprime)*cos(Oprime) - sin(wprime)*cos(iprime)*sin(Oprime))*(a*cos(Etrue)-a*e) - (cos(wprime)*cos(iprime)*sin(Oprime) + sin(wprime)*cos(Oprime))*(a*sqrt(1-e**2)*sin(Etrue))
##r1ecliptic.y = (cos(wprime)*sin(Oprime) + sin(wprime)*cos(iprime)*cos(Oprime))*(a*cos(Etrue)-a*e) + (cos(wprime)*cos(iprime)*cos(Oprime) - sin(wprime)*sin(Oprime))*(a*sqrt(1-e**2)*sin(Etrue))
##r1ecliptic.z = sin(wprime)*sin(iprime)*(a*cos(Etrue)-a*e) + cos(wprime)*sin(iprime)*(a*sqrt(1-e**2)*sin(Etrue))
##asteroid = sphere(pos=r1ecliptic*150, radius=(20), color=color.blue)
##asteroid.trail = curve(color=color.white)
##sun = sphere(pos=vector(0,0,0), radius=(40), color=color.yellow)
##
####while (1==1):
####    rate(200)
####    time = time + 1
####    Mtrue = 2*pi/period*(time) + M
####    Etrue = solvekep(Mtrue)
####    r1ecliptic.x = (cos(wprime)*cos(Oprime) - sin(wprime)*cos(iprime)*sin(Oprime))*(a*cos(Etrue)-a*e) - (cos(wprime)*cos(iprime)*sin(Oprime) + sin(wprime)*cos(Oprime))*(a*sqrt(1-e**2)*sin(Etrue))
####    r1ecliptic.y = ((cos(wprime)*sin(Oprime) + sin(wprime)*cos(iprime)*cos(Oprime))*(a*cos(Etrue)-a*e)) + (cos(wprime)*cos(iprime)*cos(Oprime) - sin(wprime)*sin(Oprime))*(a*sqrt(1-e**2)*sin(Etrue))
####    r1ecliptic.z = sin(wprime)*sin(iprime)*(a*cos(Etrue)-a*e) + cos(wprime)*sin(iprime)*(a*sqrt(1-e**2)*sin(Etrue))
####    asteroid.pos = r1ecliptic*150
####    asteroid.trail.append(pos=asteroid.pos)
########################################################################################################################################################################################################
##a_earth = 2.7072115289466603
##e_earth = 0.5663623655706188
##M_earth = radians(336.36938730764535)
##Oprime_earth = radians(139.36283170416212)
##iprime_earth = radians(9.048448306581388)
##wprime_earth = radians(221.38791777245146)
##
##def solvekep_earth(M_earth):
##    Eguess_earth = M_earth
##    Mguess_earth = Eguess_earth - e_earth*sin(Eguess_earth)
##    Mtrue_earth = M_earth
##    while abs(Mguess_earth - Mtrue_earth) > 1e-004:
##        Mguess_earth = Eguess_earth - e_earth*sin(Eguess_earth)
##        Eguess_earth = Eguess_earth - (Eguess_earth - e_earth*sin(Eguess_earth) - Mtrue_earth) / (1 - e_earth*cos(Eguess_earth))
##    return Eguess_earth
##
##sqrtmu_earth = 0.01720209895
##mu_earth = sqrtmu**2
##time_earth = 0
##dt_earth = 0.05
##period_earth = sqrt(4*pi**2*a_earth**3/mu_earth)
##r1ecliptic_earth = vector(0, 0, 0)
##Mtrue_earth = 2*pi/period_earth*(time_earth) + M_earth
##Etrue_earth = solvekep_earth(Mtrue_earth)
##r1ecliptic_earth.x = (cos(wprime_earth)*cos(Oprime_earth) - sin(wprime_earth)*cos(iprime_earth)*sin(Oprime_earth))*(a_earth*cos(Etrue_earth)-a_earth*e_earth) - (cos(wprime_earth)*cos(iprime_earth)*sin(Oprime_earth) + sin(wprime_earth)*cos(Oprime_earth))*(a_earth*sqrt(1-e_earth**2)*sin(Etrue_earth))
##r1ecliptic_earth.y = (cos(wprime_earth)*sin(Oprime_earth) + sin(wprime_earth)*cos(iprime_earth)*cos(Oprime_earth))*(a_earth*cos(Etrue_earth)-a_earth*e_earth) + (cos(wprime_earth)*cos(iprime_earth)*cos(Oprime_earth) - sin(wprime_earth)*sin(Oprime_earth))*(a_earth*sqrt(1-e_earth**2)*sin(Etrue_earth))
##r1ecliptic_earth.z = sin(wprime_earth)*sin(iprime_earth)*(a_earth*cos(Etrue_earth)-a_earth*e_earth) + cos(wprime_earth)*sin(iprime_earth)*(a_earth*sqrt(1-e_earth**2)*sin(Etrue_earth))
##earth = sphere(pos=r1ecliptic*150, radius=(10), color=color.white)
##earth.trail = curve(color=color.white)
##
##while (1==1):
##    rate(100)
##    time_earth = time_earth + 1
##    Mtrue_earth = 2*pi/period_earth*(time_earth) + M_earth
##    Etrue_earth = solvekep_earth(Mtrue_earth)
##    r1ecliptic_earth.x = (cos(wprime_earth)*cos(Oprime_earth) - sin(wprime_earth)*cos(iprime_earth)*sin(Oprime_earth))*(a_earth*cos(Etrue_earth)-a_earth*e_earth) - (cos(wprime_earth)*cos(iprime_earth)*sin(Oprime_earth) + sin(wprime_earth)*cos(Oprime_earth))*(a_earth*sqrt(1-e_earth**2)*sin(Etrue_earth))
##    r1ecliptic_earth.y = (cos(wprime_earth)*sin(Oprime_earth) + sin(wprime_earth)*cos(iprime_earth)*cos(Oprime_earth))*(a_earth*cos(Etrue_earth)-a_earth*e_earth) + (cos(wprime_earth)*cos(iprime_earth)*cos(Oprime_earth) - sin(wprime_earth)*sin(Oprime_earth))*(a_earth*sqrt(1-e_earth**2)*sin(Etrue_earth))
##    r1ecliptic_earth.z = sin(wprime_earth)*sin(iprime_earth)*(a_earth*cos(Etrue_earth)-a_earth*e_earth) + cos(wprime_earth)*sin(iprime_earth)*(a_earth*sqrt(1-e_earth**2)*sin(Etrue_earth))
##    earth.pos = r1ecliptic_earth*150
##    earth.trail.append(pos=earth.pos)
##    rate(200)
##    time = time + 1
##    Mtrue = 2*pi/period*(time) + M
##    Etrue = solvekep(Mtrue)
##    r1ecliptic.x = (cos(wprime)*cos(Oprime) - sin(wprime)*cos(iprime)*sin(Oprime))*(a*cos(Etrue)-a*e) - (cos(wprime)*cos(iprime)*sin(Oprime) + sin(wprime)*cos(Oprime))*(a*sqrt(1-e**2)*sin(Etrue))
##    r1ecliptic.y = ((cos(wprime)*sin(Oprime) + sin(wprime)*cos(iprime)*cos(Oprime))*(a*cos(Etrue)-a*e)) + (cos(wprime)*cos(iprime)*cos(Oprime) - sin(wprime)*sin(Oprime))*(a*sqrt(1-e**2)*sin(Etrue))
##    r1ecliptic.z = sin(wprime)*sin(iprime)*(a*cos(Etrue)-a*e) + cos(wprime)*sin(iprime)*(a*sqrt(1-e**2)*sin(Etrue))
##    asteroid.pos = r1ecliptic*150
##    asteroid.trail.append(pos=asteroid.pos)

    




