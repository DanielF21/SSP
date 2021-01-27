from vpython import *
from math import *

ax = 1.000001018
ec = 0.0167086
M = radians(100.46435)
O = radians(174.9)
i = radians(7.155)
w = radians(102.9)

def solvekep(M):
    Eguess = M
    Mguess = Eguess - e*sin(Eguess)
    Mtrue = M
    while abs(Mguess - Mtrue) > 1e-004:
        Mguess = Eguess - e*sin(Eguess)
        Eguess = Eguess - (Eguess - e*sin(Eguess) - Mtrue) / (1 - e*cos(Eguess))
    return Eguess

sqrtmu = 0.01720209895
mu = sqrtmu**2
time = 0
dt = 0.05
period = sqrt(4*pi**2*ax**3/mu)
r1ecliptic = vector(0, 0, 0)
Mtrue = 2*pi/period*(time) + M
Etrue = solvekep(Mtrue)
r1ecliptic.x = (cos(w)*cos(O) - sin(w)*cos(i)*sin(O))*(ax*cos(Etrue)-ax*ec) - (cos(w)*cos(i)*sin(O) + sin(w)*cos(O))*(ax*sqrt(1-ec**2)*sin(Etrue))
r1ecliptic.y = (cos(w)*sin(O) + sin(w)*cos(i)*cos(O))*(ax*cos(Etrue)-ax*ec) + (cos(w)*cos(i)*cos(O) - sin(w)*sin(O))*(ax*sqrt(1-ec**2)*sin(Etrue))
r1ecliptic.z = sin(w)*sin(i)*(ax*cos(Etrue)-ax*ec) + cos(w)*sin(i)*(ax*sqrt(1-ec**2)*sin(Etrue))
asteroid = sphere(pos=r1ecliptic*150, radius=(15), color=color.white)
asteroid.trail = curve(color=color.white)
sun = sphere(pos=vector(0,0,0), radius=(90), color=color.yellow)

while (1==1):
    rate(200)
    time = time + 1
    Mtrue = 2*pi/period*(time) + M
    Etrue = solvekep(Mtrue)
    r1ecliptic.x = (cos(w)*cos(O) - sin(w)*cos(i)*sin(O))*(ax*cos(Etrue)-ax*ec) - (cos(w)*cos(i)*sin(O) + sin(w)*cos(O))*(ax*sqrt(1-ec**2)*sin(Etrue))
    r1ecliptic.y = ((cos(w)*sin(O) + sin(w)*cos(i)*cos(O))*(ax*cos(Etrue)-ax*ec)) + (cos(w)*cos(i)*cos(O) - sin(w)*sin(O))*(ax*sqrt(1-ec**2)*sin(Etrue))
    r1ecliptic.z = sin(w)*sin(i)*(ax*cos(Etrue)-ax*ec) + cos(w)*sin(i)*(ax*sqrt(1-ec**2)*sin(Etrue))
    asteroid.pos = r1ecliptic*150
    asteroid.trail.append(pos=asteroid.pos)


