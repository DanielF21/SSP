from vpython import *
from math import * 
a = 2.7072115289466603
e = 0.000000000000000000000001
M = radians(336.36938730764535)
Oprime = radians(139.36283170416212)
iprime = radians(9.048448306581388)
wprime = radians(221.38791777245146)

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
period = sqrt(4*pi**2*a**3/mu)
r1ecliptic = vector(0, 0, 0)
Mtrue = 2*pi/period*(time) + M
Etrue = solvekep(Mtrue)
r1ecliptic.x = (cos(wprime)*cos(Oprime) - sin(wprime)*cos(iprime)*sin(Oprime))*(a*cos(Etrue)-a*e) - (cos(wprime)*cos(iprime)*sin(Oprime) + sin(wprime)*cos(Oprime))*(a*sqrt(1-e**2)*sin(Etrue))
r1ecliptic.y = (cos(wprime)*sin(Oprime) + sin(wprime)*cos(iprime)*cos(Oprime))*(a*cos(Etrue)-a*e) + (cos(wprime)*cos(iprime)*cos(Oprime) - sin(wprime)*sin(Oprime))*(a*sqrt(1-e**2)*sin(Etrue))
r1ecliptic.z = sin(wprime)*sin(iprime)*(a*cos(Etrue)-a*e) + cos(wprime)*sin(iprime)*(a*sqrt(1-e**2)*sin(Etrue))
asteroid = sphere(pos=r1ecliptic*150, radius=(15), color=color.white)
asteroid.trail = curve(color=color.white)
sun = sphere(pos=vector(0,0,0), radius=(90), color=color.yellow)

while (1==1):
    rate(200)
    time = time + 1
    Mtrue = 2*pi/period*(time) + M
    Etrue = solvekep(Mtrue)
    r1ecliptic.x = (cos(wprime)*cos(Oprime) - sin(wprime)*cos(iprime)*sin(Oprime))*(a*cos(Etrue)-a*e) - (cos(wprime)*cos(iprime)*sin(Oprime) + sin(wprime)*cos(Oprime))*(a*sqrt(1-e**2)*sin(Etrue))
    r1ecliptic.y = ((cos(wprime)*sin(Oprime) + sin(wprime)*cos(iprime)*cos(Oprime))*(a*cos(Etrue)-a*e)) + (cos(wprime)*cos(iprime)*cos(Oprime) - sin(wprime)*sin(Oprime))*(a*sqrt(1-e**2)*sin(Etrue))
    r1ecliptic.z = sin(wprime)*sin(iprime)*(a*cos(Etrue)-a*e) + cos(wprime)*sin(iprime)*(a*sqrt(1-e**2)*sin(Etrue))
    asteroid.pos = r1ecliptic*150
    asteroid.trail.append(pos=asteroid.pos)



ax = 1.000001018
ec = 0.0167086
Me = radians(100.46435)
O = radians(174.9)
i = radians(7.155)
w = radians(102.9)

def yee(M):
    Eguess = Me
    Mguess = Eguess - ec*sin(Eguess)
    Mtrue = Me
    while abs(Mguess - Mtrue) > 1e-004:
        Mguess = Eguess - ec*sin(Eguess)
        Eguess = Eguess - (Eguess - e*sin(Eguess) - Mtrue) / (1 - ec*cos(Eguess))
    return Eguess

period_earth = sqrt(4*pi**2*ax**3/mu)
r1ecliptic2 = vector(0, 0, 0)
Mtrue = 2*pi/period_earth*(time) + Me
Etrue = yee(Mtrue)
r1ecliptic2.x = (cos(w)*cos(O) - sin(w)*cos(i)*sin(O))*(ax*cos(Etrue)-ax*ec) - (cos(w)*cos(i)*sin(O) + sin(w)*cos(O))*(ax*sqrt(1-ec**2)*sin(Etrue))
r1ecliptic2.y = (cos(w)*sin(O) + sin(w)*cos(i)*cos(O))*(ax*cos(Etrue)-ax*ec) + (cos(w)*cos(i)*cos(O) - sin(w)*sin(O))*(ax*sqrt(1-ec**2)*sin(Etrue))
r1ecliptic2.z = sin(w)*sin(i)*(ax*cos(Etrue)-ax*ec) + cos(w)*sin(i)*(ax*sqrt(1-ec**2)*sin(Etrue))
earth = sphere(pos=r1ecliptic2*150, radius=(40), color=color.blue)
earth.trail = curve(color=color.red)

while (1==1):
    rate(300)
    time = time + 1
    Mtrue = 2*pi/period_earth*(time) + Me
    Etrue = yee(Mtrue)
    r1ecliptic2.x = (cos(w)*cos(O) - sin(w)*cos(i)*sin(O))*(ax*cos(Etrue)-ax*ec) - (cos(w)*cos(i)*sin(O) + sin(w)*cos(O))*(ax*sqrt(1-ec**2)*sin(Etrue))
    r1ecliptic2.y = ((cos(w)*sin(O) + sin(w)*cos(i)*cos(O))*(ax*cos(Etrue)-ax*ec)) + (cos(w)*cos(i)*cos(O) - sin(w)*sin(O))*(ax*sqrt(1-ec**2)*sin(Etrue))
    r1ecliptic2.z = sin(w)*sin(i)*(ax*cos(Etrue)-ax*ec) + cos(w)*sin(i)*(ax*sqrt(1-ec**2)*sin(Etrue))
    earth.pos = r1ecliptic2*150
    earth.trail.append(pos=earth.pos)  



    

