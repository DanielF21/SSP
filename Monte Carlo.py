#Library initialization
from math import *
import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt
import ODFunctions
from datetime import datetime
from matplotlib import mlab as mlab

aA = []
eA = []
IA = []
OA = []
WA = []
MA = []


choice = input("Select Permutation: ")
iterations = int(input("Select number of iterations: "))

def orbitDetermination(file,choice):
    # Break inputs into Arrays
    inputfile = open(file,"r")
    read = inputfile.readlines()
    for i in range(len(read)):
        read[i] = read[i].rstrip()
    finaline = [x for x in read if x != ""]

    ra = []
    dec = []
    julian = []
    XvecR = []
    YvecR = []
    ZvecR = []


    for line in finaline:
        row = line.split()
        ra.append(float(ODFunctions.convertRa(row[4])))
        dec.append(float(ODFunctions.convertDec(row[5])))
        julian.append(ODFunctions.convertJul(row[0],row[1],row[2],row[3]))
        XvecR.append(float(row[6]))
        YvecR.append(float(row[7]))
        ZvecR.append(float(row[8]))
        enddisplay = len(ra)

        #config = (1, "i", len(ra))
        #print("\n")
        #print("Please select data permutation", config)
        #print("Options: ", *range(2,len(ra)))
        #choice = input("Select for i from the above list: ")
        #print("Selected Permutation: ", (1,choice,enddisplay))

    selection = int(choice) - 1
    ra = [float(ra[0]),float(ra[selection]),float(ra[len(ra)-1])]
    dec = [float(dec[0]),float(dec[selection]),float(dec[len(dec)-1])]

    Rvec1 = [float(XvecR[0]),float(YvecR[0]),float(ZvecR[0])]
    Rvec2 = [float(XvecR[selection]),float(YvecR[selection]),float(ZvecR[selection])]
    Rvec3 = [float(XvecR[len(XvecR)-1]),float(YvecR[len(YvecR)-1]),float(ZvecR[len(ZvecR)-1])]
    t1 = julian[0]
    t2 = julian[selection]
    t3 = julian[len(julian)-1]

    ra1 = np.random.normal(float(ra[0]),2.9089e-06,1)
    ra2 = np.random.normal(float(ra[1]),3.3937e-06,1)
    ra3 = np.random.normal(float(ra[2]),6.8942e-07,1)
    ra = [ra1,ra2,ra3]
    dec1 = np.random.normal(float(dec[0]),3.3937e-06,1)
    dec2 = np.random.normal(float(dec[1]),8.2418e-06,1)
    dec3 = np.random.normal(float(dec[2]),1.0079e-06,1)
    dec = [dec1,dec2,dec3]
    
    # Found on Pg 4, Eq 1

    unitRho1eq = [(cos(ra[0])*cos(dec[0])),(sin(ra[0])*cos(dec[0])),sin(dec[0])]
    unitRho2eq = [(cos(ra[1])*cos(dec[1])),(sin(ra[1])*cos(dec[1])),sin(dec[1])]
    unitRho3eq = [(cos(ra[2])*cos(dec[2])),(sin(ra[2])*cos(dec[2])),sin(dec[2])]

    obl = radians(23.4358)
    # Equatorial Cartesian to Ecliptic Cartesian
    xunitRho1 = unitRho1eq[0]
    yunitRho1 = unitRho1eq[1]*cos(obl) + unitRho1eq[2]*sin(obl)
    zunitRho1 = -unitRho1eq[1]*sin(obl) + unitRho1eq[2]*cos(obl)
    unitRho1 = [xunitRho1, yunitRho1, zunitRho1]
    
    xunitRho2 = unitRho2eq[0]
    yunitRho2 = unitRho2eq[1]*cos(obl) + unitRho2eq[2]*sin(obl)
    zunitRho2 = -unitRho2eq[1]*sin(obl) + unitRho2eq[2]*cos(obl)
    unitRho2 = [xunitRho2, yunitRho2, zunitRho2]

    xunitRho3 = unitRho3eq[0]
    yunitRho3 = unitRho3eq[1]*cos(obl) + unitRho3eq[2]*sin(obl)
    zunitRho3 = -unitRho3eq[1]*sin(obl) + unitRho3eq[2]*cos(obl)
    unitRho3 = [xunitRho3, yunitRho3, zunitRho3]

    # Begin the process of finding rmag using the scalar equation of Lagrange
    # Many variable initilizations and math definitions
    
    k = 0.01720209895
    mu = 1
    
    # Pg 24 Eq 87
    tau3 = k*(t3 - t2)
    tau1 = k*(t1 - t2)
    tau = tau3 - tau1

    #Pg 26 Eq 98
    D11 = np.dot(np.cross(Rvec1,unitRho2),unitRho3)
    D12 = np.dot(np.cross(Rvec2,unitRho2),unitRho3)
    D13 = np.dot(np.cross(Rvec3,unitRho2),unitRho3)
    D21 = np.dot(np.cross(unitRho1,Rvec1),unitRho3)
    D22 = np.dot(np.cross(unitRho1,Rvec2),unitRho3)
    D23 = np.dot(np.cross(unitRho1,Rvec3),unitRho3)
    D31 = np.dot(unitRho1,np.cross(unitRho2,Rvec1))
    D32 = np.dot(unitRho1,np.cross(unitRho2,Rvec2))
    D33 = np.dot(unitRho1,np.cross(unitRho2,Rvec3))
    Do = np.dot(unitRho1,np.cross(unitRho2,unitRho3))

    #Pg 38
    A1 = tau3/tau
    B1 = (A1/6)*(tau**2 - tau3**2)
    A3 = -tau1/tau
    B3 = (A3/6)*(tau**2 - tau1**2)
    
    A = (A1*D21 - D22 + A3*D23)/(-Do)
    B = (B1*D21 + B3*D23)/(-Do)
    F = (np.linalg.norm(Rvec2))**2
    E = -2*(np.dot(unitRho2,Rvec2))

    c = -(mu**2)*(B**2)
    b = -mu*(2*A*B + B*E)
    a = -(A**2 + A*E + F)

    #Solve for roots of r2mag

    poly = [1,0,a,0,0,b,0,0,c]
    p = np.poly1d(poly)
    roots = np.roots(p)
    realroots = []

    # Weed out unrealistic possibilities
    for i in range(len(roots)):
        if roots[i] > 0 and np.iscomplex(roots[i]) == False:
            realroots.append(np.real(roots[i]))
    r2mag = realroots[0]
    # Now we begin the orbit determination in earnest

    #Begin by finding our first guesses for the F and G values
    #This will use the truncated F and G taylor series

    #Pg 28 Eq 101 Preliminary f/g

    f1 = 1 - ((mu)/(2*r2mag**3))*(tau1**2)
    f3 = 1 - ((mu)/(2*r2mag**3))*(tau3**2)

    g1 = tau1 - ((mu)/(6*r2mag**3))*(tau1**3)
    g3 = tau3 - ((mu)/(6*r2mag**3))*(tau3**3)
    
    #Pg 25 Eq94/95 Preliminary c1/c3

    cdenom = f1*g3 - g1*f3
    c1 = g3/cdenom
    c3 = -g1/cdenom

    ##u2 = mu/(r2mag**3)
    ##c1donk = A1 + u2*B1 
    ##c3dink = A3 + u2*B3
    c2 = -1 # Found in Notes
    #Pg 26 Solve for each magRho

    magRho1 = (c1*D11 + c2*D12 + c3*D13)/(c1*Do)
    magRho2 = (c1*D21 + c2*D22 + c3*D23)/(c2*Do)
    magRho3 = (c1*D31 + c2*D32 + c3*D33)/(c3*Do)

    # Solve for rvec2dot
    # Pg 29 Eq 102
    ddenom = f1*g3 - f3*g1
    d1 = -f3/ddenom
    d3 = f1/ddenom

    # Solve for inital rvec values
    #Pg 4 Eq 2 (Fundamental Triangle)
    def vecDet(magRho1,magRho2,magRho3,d1,d3):
        rvec1 = np.multiply(magRho1,unitRho1) - Rvec1
        rvec2 = np.multiply(magRho2,unitRho2) - Rvec2
        rvec3 = np.multiply(magRho3,unitRho3) - Rvec3
        rvec2dot = np.multiply(d1,rvec1) + np.multiply(d3,rvec3)
        return [rvec2,rvec2dot]
    
    np.vectors = []
    np.vectors = vecDet(magRho1,magRho2,magRho3,d1,d3)
    
    # Begin Iterating r2vec and r2vecdot

    lightspeed = 173.145 # Au/day
    t1new = t1 - magRho1/lightspeed
    t2new = t2 - magRho2/lightspeed
    t3new = t3 - magRho3/lightspeed

    tau3new = k*(t3new - t2new)
    tau1new = k*(t1new - t2new)

    #print("Taus", tau1new, tau3new)
    rvec2 = np.vectors[0]
    rvec2dot = np.vectors[1]
    magRho2check = 0
    magRho2new = 1
    count = 0
    r2magnew = r2mag
    
    while abs(magRho2new - magRho2check) > 1e-6:
        magRho2check = magRho2new

        u = (mu)/(r2magnew**3)

        z = (np.dot(rvec2,rvec2dot))/(r2magnew**2)

        q = (np.dot(rvec2dot,rvec2dot))/(r2magnew**2) - u

        f1new = 1 - (mu/(2*r2magnew**3))*(tau1new**2) + ((mu*np.dot(rvec2,rvec2dot))/(2*(r2magnew**5)))*(tau1new**3)  +  (3*u*q - 15*u*z**2 + u**2)*((tau1new**4)/24)
        f3new = 1 - (mu/(2*r2magnew**3))*(tau3new**2) + ((mu*np.dot(rvec2,rvec2dot))/(2*(r2magnew**5)))*(tau3new**3)  +  (3*u*q - 15*u*z**2 + u**2)*((tau3new**4)/24)
        
        g1new = tau1new - (mu/(6*(r2magnew**3)))*(tau1new**3)  +  (6*u*z)*((tau1new**4)/24)
        g3new = tau3new - (mu/(6*(r2magnew**3)))*(tau3new**3)  +  (6*u*z)*((tau3new**4)/24)
            
        #Pg 25 Eq94/95 Preliminary c1/c3

        cdenomnew = f1new*g3new - g1new*f3new
        c1new = g3new/cdenomnew
        c3new = -g1new/cdenomnew
        c2 = -1 # Found in Notes
        #Pg 26 Solve for each magRho

        magRho1new = (c1new*D11 + c2*D12 + c3new*D13)/(c1new*Do)
        magRho2new = (c1new*D21 + c2*D22 + c3new*D23)/(c2*Do)
        magRho3new = (c1new*D31 + c2*D32 + c3new*D33)/(c3new*Do)


        # Solve for rvec2dot
        # Pg 29 Eq 102
        ddenomnew = f1new*g3new - f3new*g1new
        d1new = -f3new/ddenomnew
        d3new = f1new/ddenomnew

        np.vectorsnew = vecDet(magRho1new,magRho2new,magRho3new,d1new,d3new)
        rvec2new = np.vectorsnew[0]
        rvec2dotnew = np.vectorsnew[1]

        #Lightspeed Correction
        t1new = t1 - magRho1new/lightspeed
        t2new = t2 - magRho2new/lightspeed
        t3new = t3 - magRho3new/lightspeed
        
        tau3new = k*(t3new - t2new)
        tau1new = k*(t1new - t2new)
        taunew = tau3new - tau1new
        
        rvec2 = rvec2new
        
        rvec2dot = rvec2dotnew
        r2magnew = np.linalg.norm(rvec2)

    orbitalElements(rvec2,rvec2dot,t2)

def orbitalElements(r2vec,r2vecdot,t2):
    #print("--------------------------------------------------------------")
    # Baby OD
    k = 0.01720209895
    mu = k**2
    obl = radians(23.4358)

    # Find semimajor axis A
    a = ((2/np.linalg.norm(r2vec))-np.dot(r2vecdot,r2vecdot))**-1

    # Find Eccentricity e
    e =(1-(np.linalg.norm(abs(np.cross(r2vec,r2vecdot)))**2/a))**0.5

    # Find Inclination I 
    #Convert from virgin Equatorial Rectangular to chad Ecliptic
    xEclip = r2vec[0]
    yEclip = r2vec[1] #*cos(obl) + r2vec[2]*sin(obl)
    zEclip = r2vec [2] #*sin(obl) + r2vec[2]*cos(obl)
    r2Eclip = [xEclip, yEclip, zEclip]

    xEclipdot = r2vecdot[0]
    yEclipdot = r2vecdot[1] #*cos(obl) + r2vecdot[2]*sin(obl)
    zEclipdot = r2vecdot[2] #*sin(obl) + r2vecdot[2]*cos(obl)
    r2Eclipdot = [xEclipdot, yEclipdot, zEclipdot]

    hx = yEclip*zEclipdot - zEclip*yEclipdot
    hy = zEclip*xEclipdot - xEclip*zEclipdot
    hz = xEclip*yEclipdot - yEclip*xEclipdot
    h = np.cross(r2Eclip,r2Eclipdot)
    I = acos(np.linalg.norm(hz)/np.linalg.norm(h))

    # Note c and s notation for quadrant ambiguity. c = cos component | s = sin component
    # Find Omega O 
    sO = (hx/(np.linalg.norm(h)*sin(I)))
    cO = -1*(hy/(np.linalg.norm(h)*sin(I)))
    O = atan2(sO,cO)
    if O > 2*pi:
        O = O-2*pi
    elif O < 0:
        O = O+2*pi

    # Find baby omega w 

    cU = (xEclip*cos(O) + yEclip*sin(O))/np.linalg.norm(r2Eclip)
    sU = zEclip/(np.linalg.norm(r2Eclip)*sin(I))
    U = atan2(sU,cU)

    v = asin((((a*(1-e**2)/np.linalg.norm(h))*(np.dot(r2Eclip,r2Eclipdot)/np.linalg.norm(r2Eclip)))/e))

    w = U - v

    # Find Mean Anomaly at obs time M2
##    if v > pi:
##        v = v - 2*pi
##    if v < 0:
##        v = v + 2*pi
    E2 = acos((1/e)*(1-(np.linalg.norm(r2Eclip)/a)))
    if v < 0:
        E2 = 2*pi-E2 
    M2 = E2 - e*sin(E2)
##    if v > pi:
##        M2 = M2 - 2*pi
##        E2 = E2 - 2*pi
##    if v < 0:
##        M2 = M2 + pi
##        E2 = E2 + pi

    # Find Period and n

    n = sqrt(mu/a**3)
    P = (2*pi)/n
    P  = P / 365.25
    # Find T

    # Precess the Mean Anomaly
    tcur = datetime.now()
    #julcur = ODFunctions.convertJul(tcur.year,tcur.month,tcur.day,str(tcur.hour)+":"+str(tcur.minute)+":"+str(tcur.second))
    julcur = 2458684.75
    M2 = M2 + n*(julcur - t2)
    
    T = t2-(M2/n)
    
    aA.append(a)
    eA.append(e)
    IA.append(degrees(I))
    OA.append(degrees(O))
    WA.append(degrees(w))
    MA.append(degrees(M2))


for i in range(iterations):
    orbitDetermination("FlemingInput.txt",choice)

#Plot things ye


#n,bins,patches = plt.hist(aA,alpha=0.75,bins=50,color="r",histtype="step",linewidth=2,normed=True)
plt.hist(aA,alpha=0.75,bins=50,color="r",histtype="step",linewidth=2)
plt.axvline(np.mean(aA), color='k', linewidth=1,label="Mean")
plt.axvline(2.752391406893238,color="b", linestyle='dashed',label="JPL")
plt.axvline(np.mean(aA)-np.std(aA), color='g', linestyle='dotted', linewidth=1,label="1st Std Dev")
plt.axvline(np.mean(aA)+np.std(aA), color='g', linestyle='dotted', linewidth=1)
plt.axvline(np.mean(aA)-2*np.std(aA), color='m', linestyle='dashdot', linewidth=1,label="2st Std Dev")
plt.axvline(np.mean(aA)+2*np.std(aA), color='m', linestyle='dashdot', linewidth=1)
plt.legend()
plt.xlabel("a (Au)")
plt.ylabel("Counts")
plt.title("Monte Carlo Distribution - Semi-Major Axis")
#mlab.normpdf(bins,np.mean(aA),np.std(aA))
plt.show(aA)
plt.savefig("A3" ,format="pdf")
print("+/- Au A",np.std(aA))

plt.hist(eA,alpha=0.75,bins=50,color="r",histtype="step",linewidth=2)
plt.axvline(np.mean(eA), color='k', linewidth=1,label="Mean")
plt.axvline(0.5661985478013619	,color="b",label="JPL", linestyle='dashed')
plt.axvline(np.mean(eA)-np.std(eA), color='g', linestyle='dotted', linewidth=1,label="1st Std Dev")
plt.axvline(np.mean(eA)+np.std(eA), color='g', linestyle='dotted', linewidth=1)
plt.axvline(np.mean(eA)-2*np.std(eA), color='m', linestyle='dashdot', linewidth=1,label="2st Std Dev")
plt.axvline(np.mean(eA)+2*np.std(eA), color='m', linestyle='dashdot', linewidth=1)
plt.legend()
plt.xlabel("e")
plt.ylabel("Counts")
plt.title("Monte Carlo Distribution - Eccentricity")
plt.show(eA)
plt.savefig("e3"  ,format="pdf")
print("+/- e",np.std(eA))

plt.hist(IA,alpha=0.75,bins=50,color="r",histtype="step",linewidth=2)
plt.axvline(np.mean(IA), color='k', linewidth=1,label="Mean")
plt.axvline(8.99662834743236	,color="b",label="JPL", linestyle='dashed')
plt.axvline(np.mean(IA)-np.std(IA), color='g', linestyle='dotted', linewidth=1,label="1st Std Dev")
plt.axvline(np.mean(IA)+np.std(IA), color='g', linestyle='dotted', linewidth=1)
plt.axvline(np.mean(IA)-2*np.std(IA), color='m', linestyle='dashdot', linewidth=1,label="2st Std Dev")
plt.axvline(np.mean(IA)+2*np.std(IA), color='m', linestyle='dashdot', linewidth=1)
plt.legend()
plt.xlabel("I (deg)")
plt.ylabel("Counts")
plt.title("Monte Carlo Distribution - Inclination")

plt.show(IA)
plt.savefig("I3"  ,format="pdf")
print("+/- deg I",np.std(IA))

plt.hist(OA,alpha=0.75,bins=50,color="r",histtype="step",linewidth=2)
plt.axvline(np.mean(OA), color='k',  linewidth=1,label="Mean")
plt.axvline(139.8833057741518	,color="b",label="JPL",linestyle='dashed')
plt.axvline(np.mean(OA)-np.std(OA), color='g', linestyle='dotted', linewidth=1,label="1st Std Dev")
plt.axvline(np.mean(OA)+np.std(OA), color='g', linestyle='dotted', linewidth=1)
plt.axvline(np.mean(OA)-2*np.std(OA), color='m', linestyle='dashdot', linewidth=1,label="2st Std Dev")
plt.axvline(np.mean(OA)+2*np.std(OA), color='m', linestyle='dashdot', linewidth=1)
plt.legend()
plt.xlabel("O (deg)")
plt.ylabel("Counts")
plt.title("Monte Carlo Distribution - Longitude of Ascending Node")

plt.show(OA)
plt.savefig("O3"  ,format="pdf")
print("+/- deg O",np.std(OA))

plt.hist(WA,alpha=0.75,bins=50,color="r",histtype="step",linewidth=2)
plt.axvline(np.mean(WA), color='k',linewidth=1,label="Mean")
plt.axvline(219.3181059798912	,color="b",label="JPL",linestyle='dashed')
plt.axvline(np.mean(WA)-np.std(WA), color='g', linestyle='dotted', linewidth=1,label="1st Std Dev")
plt.axvline(np.mean(WA)+np.std(WA), color='g', linestyle='dotted', linewidth=1)
plt.axvline(np.mean(WA)-2*np.std(WA), color='m', linestyle='dashdot', linewidth=1,label="2st Std Dev")
plt.axvline(np.mean(WA)+2*np.std(WA), color='m', linestyle='dashdot', linewidth=1)
plt.legend()
plt.xlabel("W (deg)")
plt.ylabel("Counts")
plt.title("Monte Carlo Distribution - Argument of Periapsis")

plt.show(WA)
plt.savefig("W3" , format="pdf")
print("+/- deg W",np.std(WA))

plt.hist(MA,alpha=0.75,bins=50,color="r",histtype="step",linewidth=2)
plt.axvline(np.mean(MA), color='k', linewidth=1,label="Mean")
plt.axvline(344.69110680705984 , color="b",label="JPL",linestyle='dashed')
plt.axvline(np.mean(MA)-np.std(MA), color='g', linestyle='dotted', linewidth=1,label="1st Std Dev")
plt.axvline(np.mean(MA)+np.std(MA), color='g', linestyle='dotted', linewidth=1)
plt.axvline(np.mean(MA)-2*np.std(MA), color='m', linestyle='dashdot', linewidth=1,label="2st Std Dev")
plt.axvline(np.mean(MA)+2*np.std(MA), color='m', linestyle='dashdot', linewidth=1)
plt.legend()
plt.xlabel("M (deg)")
plt.ylabel("Counts")
plt.title("Monte Carlo Distribution - Mean Anomaly")

plt.show(MA)
plt.savefig("M3"  ,format="pdf")
print("+/- deg M",np.std(MA))
