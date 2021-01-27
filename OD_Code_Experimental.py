from math import *
import numpy as np

'''

Inputs: Three R Vectors from JPL
        RA and DEC from three individual observations
        Julian Dates of the Observations

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

def OD(filename):
    RaList = []
    DecList = []
    JulianList = []
    R_Vector_List_1 = []
    R_Vector_List_2 = []
    R_Vector_List_3 = []
    input = open(filename, 'r')
    for line in input.readlines():
        row = line.split()
        if len(row) > 0:
            JulianList.append(float(row[0]))
            RaList.append(float(convertRa(row[1])))
            DecList.append(float(convertDec(row[2])))
            R_Vector_List_3.append(float((row[5])))
            R_Vector_List_2.append(float((row[4])))
            R_Vector_List_1.append(float((row[3])))
            
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
    

    f_series1 = 1 - (mu/(2 * RealPositiveRoots[0]**3)) * (Tau1**2)
    f_series3 = 1 - (mu/(2 * RealPositiveRoots[0]**3)) * (Tau3**2)
    g_series1 = Tau1 - (mu/(6 * RealPositiveRoots[0]**3)) * (Tau1**3)
    g_series3 = Tau3 - (mu/(6 * RealPositiveRoots[0]**3)) * (Tau3**3)
    

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

#Solve for f and g series in the iteration     

    u = mu / OnlyRoot**3
    z = (np.dot(r2_vector, r2_dot_vector)/OnlyRoot**2)
    q = (np.dot(r2_dot_vector, r2_dot_vector)/OnlyRoot**2) - u

    iteration_f_series1 = 1 - (u * Tau1_New**2)/2 + (u * z * Tau1_New**3)/2 + ((3 * u * q - 15 * u * z**2 + u**2) * Tau1_New**4)/24
    iteration_f_series3 = 1 - (u * Tau3_New**2)/2 + (u * z * Tau3_New**3)/2 + ((3 * u * q - 15 * u * z**2 + u**2) * Tau3_New**4)/24
    iteration_g_series1 = Tau1_New - (u * Tau1_New**3)/6 + (u * z * Tau1_New**4)/4
    iteration_g_series3 = Tau3_New - (u * Tau3_New**3)/6 + (u * z * Tau3_New**4)/4

#Iteration Time :)

    iteration_r2_vector = [0,0,0]
    
    while abs(iteration_r2_vector[0] - r2_vector[0]) > 1e-9000:

        r2_vector = iteration_r2_vector

        iteration_c_denominator = (iteration_f_series1 * iteration_g_series3) - (iteration_g_series1 * iteration_f_series3)
        
        iteration_c1 = iteration_g_series3 / iteration_c_denominator
        
        iteration_c3 = -1 * iteration_g_series1 / iteration_c_denominator
        
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
        
        iteration_r2_dot_vector = iteration_d1 * iteration_r1_vector + iteration_d3 * iteration_r3_vector
        

        #Correct for light travel time in the iteration

        iteration_t1 = JulianList[0] - (iteration_rho_mag_1_ecliptic / speed_of_light)
        iteration_t2 = JulianList[1] - (iteration_rho_mag_2_ecliptic / speed_of_light)
        iteration_t3 = JulianList[2] - (iteration_rho_mag_3_ecliptic / speed_of_light)

        iteration_Tau1_New = k * (iteration_t1 - iteration_t2)
        iteration_Tau3_New = k * (iteration_t3 - iteration_t2)
        iteration_Tau_New = iteration_Tau3_New - iteration_Tau1_New

        u = mu / OnlyRoot**3
        z = (np.dot(iteration_r2_vector, iteration_r2_dot_vector)/OnlyRoot**2)
        q = (np.dot(iteration_r2_dot_vector, iteration_r2_dot_vector)/OnlyRoot**2) - u

        iteration_f_series1 = 1 - (u * Tau1_New**2)/2 + (u * z * Tau1_New**3)/2 + ((3 * u * q - 15 * u * z**2 + u**2) * Tau1_New**4)/24
        iteration_f_series3 = 1 - (u * Tau3_New**2)/2 + (u * z * Tau3_New**3)/2 + ((3 * u * q - 15 * u * z**2 + u**2) * Tau3_New**4)/24
        iteration_g_series1 = Tau1_New - (u * Tau1_New**3)/6 + (u * z * Tau1_New**4)/4
        iteration_g_series3 = Tau3_New - (u * Tau3_New**3)/6 + (u * z * Tau3_New**4)/4

##        print("f and g series in loop", iteration_f_series1, iteration_f_series3, iteration_g_series1, iteration_g_series3)

        print("r2 vector", iteration_r2_vector)
        print("r2 dot vector", iteration_r2_dot_vector)


print(OD("GaussTest.txt"))



