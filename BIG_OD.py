from math import *
import numpy as np
import astropy.io as fits
import matplotlib.pyplot as plt

# The comments will represent my un - edited thoughts while programming (7/13/2019 13:49 MDT)
# Already confused (7/13/19 13:50 MDT)

# Method of Gauss to get r2_vector and r2_dot_vector

k = 0.01720209895
mu = k**2
speed_of_light = 173.145

BIG_R1_VECTOR = [-1.419535308255705E-01, 1.006729973431543E+00, -4.751644037536355E-05]
BIG_R2_VECTOR = [-2.086345958778717E-01, 9.951175491609900E-01, -4.422280627344284E-05]
BIG_R3_VECTOR = [-2.737167847620506E-01, 9.791832018812779E-01, -4.142625927076923E-05]

BIG_R1_VECTOR_MAG = np.linalg.norm(BIG_R1_VECTOR)
BIG_R2_VECTOR_MAG = np.linalg.norm(BIG_R2_VECTOR)
BIG_R3_VECTOR_MAG = np.linalg.norm(BIG_R3_VECTOR)

#Ra/Dec 1 taken from Observation 3 Seq 3 Frame 1
#Ra/Dec 2 taken from Observation 4 Seq 3 Frame 5
#Ra/Dec 3 taken from Observation 5 Seq 1 Frame 1

Ra1 = 20.5465833 * 15
Ra2 = 20.5881972 * 15
Ra3 = 20.62599956956769 * 15
Dec1 = -6.6352833 * 15
Dec2 = -6.7002972 * 15
Dec3 = -6.872044214771413 * 15

Ra = [Ra1, Ra2, Ra3]
Dec = [Dec1, Dec2, Dec3]

Obliquity = radians(23.4358)

transform = np.array([[1,0,0],[0,cos(Obliquity), sin(Obliquity)],[0, -sin(Obliquity), cos(Obliquity)]])

rho_hat_1 = np.matmul(np.array([(cos(Ra1) * cos(Dec1)), (sin(Ra1) * cos(Dec1)), sin(Dec1)]), transform)
rho_hat_2 = np.matmul(np.array([(cos(Ra2) * cos(Dec2)), sin(Ra2) * cos(Dec2), sin(Dec2)]), transform)
rho_hat_3 = np.matmul(np.array([(cos(Ra3) * cos(Dec3)), sin(Ra3) * cos(Dec3), sin(Dec3)]), transform)
print(rho_hat_1)
print(rho_hat_2)
print(rho_hat_3)

Julian = [2458664.85285, 2458668.85264, 2458672.8132885415]

Tau1 = k * (Julian[2] - Julian[1])
Tau3 = k * (Julian[0] - Julian[1])
Tau = Tau3 - Tau1

A1 = Tau3 / Tau
B1 = (A1 / 6) * (Tau**2 - Tau3**2)
A3 = (-Tau1 / Tau)
B3 = (A3 / 6) * (Tau**2 - Tau1**2)

# How do I find the R Vectors?? (7/13/19 14:24 MDT)

E = -2 * np.dot(rho_hat_2, BIG_R2_VECTOR)
F = np.linalg.norm(BIG_R2_VECTOR)**2

# Found the R Vectors + their Magnitudes (7/13/10 15:44 MDT)

D0 = np.dot(rho_hat_1, np.cross(rho_hat_2, rho_hat_3))
D11 = np.dot(np.cross(BIG_R1_VECTOR, rho_hat_2), rho_hat_3)
D12 = np.dot(np.cross(BIG_R2_VECTOR, rho_hat_2), rho_hat_3)
D13 = np.dot(np.cross(BIG_R3_VECTOR, rho_hat_2), rho_hat_3)
D21 = np.dot(np.cross(rho_hat_1, BIG_R1_VECTOR), rho_hat_3)
D22 = np.dot(np.cross(rho_hat_1, BIG_R2_VECTOR), rho_hat_3)
D23 = np.dot(np.cross(rho_hat_1, BIG_R3_VECTOR), rho_hat_3)
D31 = np.dot(np.cross(rho_hat_2, BIG_R1_VECTOR), rho_hat_3)
D32 = np.dot(np.cross(rho_hat_2, BIG_R2_VECTOR), rho_hat_3)
D33 = np.dot(np.cross(rho_hat_2, BIG_R3_VECTOR), rho_hat_3)

A = (A1 * D21 - D22 + A3 * D23) / -D0
##B = (B1 * D21 - D22 + A3 * D23) / -D0

a = -(A**2 + A * E + F)
b = -mu * (2 * A * B + B * E)
c = -mu**2 * B**2

print(a)
print(b)
print(c)

polynomial = [1,0,a,0,0,b,0,0,c]
poly = np.poly1d(polynomial)
print(np.roots(poly))

root = 2.83482765e-02

mu2 = mu / (root**3)

# Whats c2??? (7/13/19 17:09 MDT)

f_series1 = 1 - (mu/(2 * root**3)) * (Tau1**2)
f_series3 = 1 - (mu/(2 * root**3)) * (Tau3**2)
g_series1 = Tau1 - (mu/(6 * root**3)) * (Tau1**2)
g_series3 = Tau3 - (mu/(6 * root**3)) * (Tau3**2)

c1 = g_series3 /(f_series1 * g_series3 - g_series1 * f_series3)
c3 = -g_series1 /(f_series1 * g_series3 - g_series1 * f_series3)

##c1 = A1 + mu2 * B1
##c3 = A3 + mu2 * B3

c2 = -1

rho_mag_1 = (c1 * D11 + c2 * D12 + c3 * D13) / (c1 * D0)
rho_mag_2 = (c1 * D21 + c2 * D22 + c3 * D23) / (c2 * D0)
rho_mag_3 = (c1 * D31 + c2 * D32 + c3 * D33) / (c3 * D0)

rho_vector_1 = rho_mag_1 * rho_hat_1
rho_vector_2 = rho_mag_2 * rho_hat_2
rho_vector_3 = rho_mag_3 * rho_hat_3

d1 = -f_series3 / (f_series1 * g_series3 - f_series3 * g_series1)
d3 = f_series1 / (f_series1 * g_series3 - f_series3 * g_series1)

r1_vector = rho_vector_1 - BIG_R1_VECTOR
r2_vector = rho_vector_2 - BIG_R2_VECTOR
r3_vector = rho_vector_3 - BIG_R3_VECTOR

r2_vector_magnitude = np.linalg.norm(r2_vector)

r2_dot_vector = d1 * r1_vector + d3 * r3_vector

Julian[0] = Julian[0] - rho_mag_1 / speed_of_light
Julian[1] = Julian[1] - rho_mag_2 / speed_of_light
Julian[2] = Julian[2] - rho_mag_3 / speed_of_light

Tau1_New = k * (Julian[2] - Julian[1])
Tau3_New = k * (Julian[0] - Julian[1])
Tau_New = Tau3_New - Tau1_New
print("prelim r2")
print(r2_vector)


for i in range(30):
    
    u = mu/root**3
    z = np.dot(r2_vector, r2_dot_vector) / root**2
    q = (np.dot(r2_dot_vector, r2_dot_vector) / root**2) - u
    new_f_series1 = 1 - ((mu/(2 * root**3)) * (Tau1**2)) + ((mu * (np.dot(r2_vector, r2_dot_vector)) * Tau1_New**3)/(2 * root**5)) + (3 * u * q - 15 * u * z**2 + u**2)
    new_f_series3 = 1 - ((mu/(2 * root**3)) * (Tau3**2)) + ((mu * (np.dot(r2_vector, r2_dot_vector)) * Tau3_New**3)/(2 * root**5)) + (3 * u * q - 15 * u * z**2 + u**2)
    new_g_series1 = Tau1 - (mu/(6 * root**3)) * (Tau1**2) + (6 * u * z)
    new_g_series3 = Tau3 - (mu/(6 * root**3)) * (Tau3**2) + (6 * u * z)

##    c1 = A1 + mu2 * B1
##    c3 = A3 + mu2 * B3
    c1 = g_series3 /(f_series1 * g_series3 - g_series1 * f_series3)
    c3 = -g_series1 /(f_series1 * g_series3 - g_series1 * f_series3)
    c2 = -1

    rho_mag_1 = (c1 * D11 + c2 * D12 + c3 * D13) / (c1 * D0)
    rho_mag_2 = (c1 * D21 + c2 * D22 + c3 * D23) / (c2 * D0)
    rho_mag_3 = (c1 * D31 + c2 * D32 + c3 * D33) / (c3 * D0)

    rho_vector_1 = rho_mag_1 * rho_hat_1
    rho_vector_2 = rho_mag_2 * rho_hat_2
    rho_vector_3 = rho_mag_3 * rho_hat_3

    r1_vector = rho_vector_1 - BIG_R1_VECTOR
    r2_vector = rho_vector_2 - BIG_R2_VECTOR
    r3_vector = rho_vector_3 - BIG_R3_VECTOR

    d1 = -f_series3 / (new_f_series1 * new_g_series3 - new_f_series3 * new_g_series1)
    d3 = f_series1 / (new_f_series1 * new_g_series3 - new_f_series3 * new_g_series1)

    r2_dot_vector = d1 * r1_vector + d3 * r3_vector

    Tau1_New = k * (Julian[2] - Julian[1])
    Tau3_New = k * (Julian[0] - Julian[1])
    Tau_New = Tau3_New - Tau1_New

    print(r2_vector, r2_dot_vector)
##
##Ignorance_Moment_Count += 1        
##
### How to I make this iterate?? (7/13/19 20:48 MDT)
##
##Obliquity = radians(23.4358)
##
###Step 1: Get a
##
##a = ((2/r2_vector_magnitude) - np.dot(r2_dot_vector, r2_dot_vector))**-1
##
##print("-------------")
##print("A")
##print(a)
##print("-------------")
##
###Step 2: Get e
##
##e = sqrt((1 - ((np.linalg.norm(abs(np.cross(r2_vector, r2_dot_vector)))**2)/a)))
##print("e")
##print(e)
##print("-------------")
##
##
###Step 3: Get I
##
##transform = np.array([[1,0,0],[0,cos(Obliquity), sin(Obliquity)],[0, -sin(Obliquity), cos(Obliquity)]])
##
##r2_vector_ec = np.matmul(transform, r2_vector)
##
##r2_dot_vector_ec = np.matmul(transform, r2_dot_vector)
##
##h = np.linalg.norm(np.cross(r2_vector, r2_dot_vector))
##
##hz = (r2_vector_ec[0] * r2_dot_vector_ec[1]) - (r2_vector_ec[1] * r2_dot_vector_ec[0])
##
##r2_vector_ec_magnitude = np.linalg.norm(r2_vector_ec)
##
####print(h)
####print(hz)
##
##I = acos(hz/h)
##
##print("I")
##print(degrees(I))
##print("-------------")
##
###Step 4: Get Ω
##
##hx = (r2_vector_ec[1] * r2_dot_vector_ec[2]) - (r2_vector_ec[2] * r2_dot_vector_ec[1])
##
##hy = (r2_vector_ec[2] * r2_dot_vector_ec[0]) - (r2_vector_ec[0] * r2_dot_vector_ec[2])
##
##BigOmega = degrees(atan2((hx/h*sin(I)),(-hy/h*sin(I))))
##
##for i in range(10):
##    if BigOmega > 360:
##        BigOmega -= 360
##    elif BigOmega < 0:
##        BigOmega += 360
##
##        
##print("Ω")
##print(BigOmega)
##print("-------------")
##
###Step 5: Get ω
##
####print("r2 vector / ecliptic")
####print(r2_vector_ec[0])
####print(r2_vector_ec[1])
####print(r2_vector_ec[2])
####print("-----")
##
##Ucos = (r2_vector_ec[0] * cos(radians(BigOmega)) + r2_vector_ec[1] * sin(radians(BigOmega)))/(r2_vector_ec_magnitude)
##
##Usin = (r2_vector_ec[2] / ((r2_vector_ec_magnitude * sin(I))))
##
##U = (atan2(Usin, Ucos))
##
##Nucos = (((a * (1 - (e**2))/r2_vector_ec_magnitude) - 1) / (e))
##
##Nusin = (a * (1-e**2) * np.dot(r2_vector, r2_dot_vector)/((h * e * r2_vector_ec_magnitude)))
##
##Nu = atan2(Nusin, Nucos)
##
##SmallOmega = degrees(U - Nu)
##
##print ("U" , degrees(U))
##print ("Nu" , degrees(Nu))
##for i in range(10):
##    if SmallOmega > 360:
##        SmallOmega -= 360
##    elif SmallOmega < 0:
##        SmallOmega += 360
##
####SmallOmega = abs(SmallOmega) % 360
##   
##print("ω")
##print(SmallOmega)
##print("-------------")
##
###Step 6: Get M0 (Mean Anomaly)
##
##E = acos((1/e) * (1 - (r2_vector_ec_magnitude / a)))
##
##E2 = E
##
##M0 = E2 - e * sin(E2)
##
##print("E")
##print(degrees(E2))
##print("-------------")
##
##print("M0")
##print(degrees(M0))
##print("-------------")
##
##print("n")
##n = sqrt(0.01720209894**2/(a**3))
##print(n)
##print("-------------")
##
##print("P")
##P = (2 * pi)/n / 365.25
##print(P)
##print("-------------")
##
##print("T")
##T = Julian[1] - ((M0))/n
##print(T)
##print("------------")
##
