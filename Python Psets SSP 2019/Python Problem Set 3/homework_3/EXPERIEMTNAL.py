from vpython import *
from math import * 
a = 1.000001018
e = 0.0167086
M = radians(100.46435)
Oprime = radians(174.9)
iprime = radians(7.155)
wprime = radians(102.9)

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
asteroid = sphere(pos=r1ecliptic*150, radius=(20), color=color.orange)
asteroid.trail = curve(color=color.white)
sun = sphere(pos=vector(0,0,0), radius=(40), color=color.yellow)

##while (1==1):
##    rate(200)
##    time = time + 1
##    Mtrue = 2*pi/period*(time) + M
##    Etrue = solvekep(Mtrue)
##    r1ecliptic.x = (cos(wprime)*cos(Oprime) - sin(wprime)*cos(iprime)*sin(Oprime))*(a*cos(Etrue)-a*e) - (cos(wprime)*cos(iprime)*sin(Oprime) + sin(wprime)*cos(Oprime))*(a*sqrt(1-e**2)*sin(Etrue))
##    r1ecliptic.y = ((cos(wprime)*sin(Oprime) + sin(wprime)*cos(iprime)*cos(Oprime))*(a*cos(Etrue)-a*e)) + (cos(wprime)*cos(iprime)*cos(Oprime) - sin(wprime)*sin(Oprime))*(a*sqrt(1-e**2)*sin(Etrue))
##    r1ecliptic.z = sin(wprime)*sin(iprime)*(a*cos(Etrue)-a*e) + cos(wprime)*sin(iprime)*(a*sqrt(1-e**2)*sin(Etrue))
##    asteroid.pos = r1ecliptic*150
##    asteroid.trail.append(pos=asteroid.pos)
######################################################################################################################################################################################################
a_earth = 2.7072115289466603
e_earth = 0.5663623655706188
M_earth = radians(336.36938730764535)
Oprime_earth = radians(139.36283170416212)
iprime_earth = radians(9.048448306581388)
wprime_earth = radians(221.38791777245146)

def solvekep_earth(M_earth):
    Eguess_earth = M_earth
    Mguess_earth = Eguess_earth - e_earth*sin(Eguess_earth)
    Mtrue_earth = M_earth
    while abs(Mguess_earth - Mtrue_earth) > 1e-004:
        Mguess_earth = Eguess_earth - e_earth*sin(Eguess_earth)
        Eguess_earth = Eguess_earth - (Eguess_earth - e_earth*sin(Eguess_earth) - Mtrue_earth) / (1 - e_earth*cos(Eguess_earth))
    return Eguess_earth

sqrtmu_earth = 0.01720209895
mu_earth = sqrtmu**2
time_earth = 0
dt_earth = 0.05
period_earth = sqrt(4*pi**2*a_earth**3/mu_earth)
r1ecliptic_earth = vector(0, 0, 0)
Mtrue_earth = 2*pi/period_earth*(time_earth) + M_earth
Etrue_earth = solvekep_earth(Mtrue_earth)
r1ecliptic_earth.x = (cos(wprime_earth)*cos(Oprime_earth) - sin(wprime_earth)*cos(iprime_earth)*sin(Oprime_earth))*(a_earth*cos(Etrue_earth)-a_earth*e_earth) - (cos(wprime_earth)*cos(iprime_earth)*sin(Oprime_earth) + sin(wprime_earth)*cos(Oprime_earth))*(a_earth*sqrt(1-e_earth**2)*sin(Etrue_earth))
r1ecliptic_earth.y = (cos(wprime_earth)*sin(Oprime_earth) + sin(wprime_earth)*cos(iprime_earth)*cos(Oprime_earth))*(a_earth*cos(Etrue_earth)-a_earth*e_earth) + (cos(wprime_earth)*cos(iprime_earth)*cos(Oprime_earth) - sin(wprime_earth)*sin(Oprime_earth))*(a_earth*sqrt(1-e_earth**2)*sin(Etrue_earth))
r1ecliptic_earth.z = sin(wprime_earth)*sin(iprime_earth)*(a_earth*cos(Etrue_earth)-a_earth*e_earth) + cos(wprime_earth)*sin(iprime_earth)*(a_earth*sqrt(1-e_earth**2)*sin(Etrue_earth))
earth = sphere(pos=r1ecliptic*150, radius=(10), color=color.white)
earth.trail = curve(color=color.white)

while (1==1):
    rate(100)
    time_earth = time_earth + 1
    Mtrue_earth = 2*pi/period_earth*(time_earth) + M_earth
    Etrue_earth = solvekep_earth(Mtrue_earth)
    r1ecliptic_earth.x = (cos(wprime_earth)*cos(Oprime_earth) - sin(wprime_earth)*cos(iprime_earth)*sin(Oprime_earth))*(a_earth*cos(Etrue_earth)-a_earth*e_earth) - (cos(wprime_earth)*cos(iprime_earth)*sin(Oprime_earth) + sin(wprime_earth)*cos(Oprime_earth))*(a_earth*sqrt(1-e_earth**2)*sin(Etrue_earth))
    r1ecliptic_earth.y = (cos(wprime_earth)*sin(Oprime_earth) + sin(wprime_earth)*cos(iprime_earth)*cos(Oprime_earth))*(a_earth*cos(Etrue_earth)-a_earth*e_earth) + (cos(wprime_earth)*cos(iprime_earth)*cos(Oprime_earth) - sin(wprime_earth)*sin(Oprime_earth))*(a_earth*sqrt(1-e_earth**2)*sin(Etrue_earth))
    r1ecliptic_earth.z = sin(wprime_earth)*sin(iprime_earth)*(a_earth*cos(Etrue_earth)-a_earth*e_earth) + cos(wprime_earth)*sin(iprime_earth)*(a_earth*sqrt(1-e_earth**2)*sin(Etrue_earth))
    earth.pos = r1ecliptic_earth*150
    earth.trail.append(pos=earth.pos)
    rate(200)
    time = time + 1
    Mtrue = 2*pi/period*(time) + M
    Etrue = solvekep(Mtrue)
    r1ecliptic.x = (cos(wprime)*cos(Oprime) - sin(wprime)*cos(iprime)*sin(Oprime))*(a*cos(Etrue)-a*e) - (cos(wprime)*cos(iprime)*sin(Oprime) + sin(wprime)*cos(Oprime))*(a*sqrt(1-e**2)*sin(Etrue))
    r1ecliptic.y = ((cos(wprime)*sin(Oprime) + sin(wprime)*cos(iprime)*cos(Oprime))*(a*cos(Etrue)-a*e)) + (cos(wprime)*cos(iprime)*cos(Oprime) - sin(wprime)*sin(Oprime))*(a*sqrt(1-e**2)*sin(Etrue))
    r1ecliptic.z = sin(wprime)*sin(iprime)*(a*cos(Etrue)-a*e) + cos(wprime)*sin(iprime)*(a*sqrt(1-e**2)*sin(Etrue))
    asteroid.pos = r1ecliptic*150
    asteroid.trail.append(pos=asteroid.pos)
