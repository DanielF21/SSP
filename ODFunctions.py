#Library initialization
from math import *
import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt

def convertRa(ra):
    rasplit = ra.split(":")
    hour = float(rasplit[0])
    minute = float(rasplit[1])
    second = float(rasplit[2])
    decimal = hour + minute/60 + second/3600
    decimal = decimal*15
    return radians(decimal)

def unconvertRa(ra):
    ra = ra/15
    decminute = ra - int(ra)
    minute = decminute*60
    decsecond = minute - int(minute)
    second = decsecond*60
    hour = ra - decminute
    return str(int(hour))+":"+str(int(minute))+":"+str(round(second,2))

def unconvertDec(dec):
    decarcmin = dec - int(dec)
    arcmin = decarcmin*60
    decarcsec = arcmin - int(arcmin)
    arcsec = decarcsec*60
    degree = dec - decarcmin
    return str(int(degree))+":"+str(int(arcmin))+":"+str(round(arcsec,2))
    

def convertDec(dec):
    decsplit = dec.split(":")
    degree = float(decsplit[0])
    arcmin = copysign(float(decsplit[1]),degree)
    arcsec = copysign(float(decsplit[2]),degree)
    decimal = degree + arcmin/60 + arcsec/3600
    return radians(decimal)

def party(partycount):
        
        if partycount == 1:
            print("""
   .-.   .-.
  (_  \ /  _)    Aries-  The Ram
       |
       |
              """)
        elif partycount == 2:
            print("""
    .     .
    '.___.'      Taurus-  The Bull
    .'   `.    
   :       :   
   :       :
    `.___.'   """)

        elif partycount == 3:
             print("""
    ._____.
      | |        Gemini-  The Twins
      | |
     _|_|_
    '     '
            """)
        elif partycount == 4:
            print("""
      .--.
     /   _`.     Cancer-  The Crab
    (_) ( )
   '.    /
     `--'
             """)
        elif partycount == 5:
            print("""
      .--.
     (    )       Leo-  The Lion
    (_)  /
        (_,

            """)
        elif partycount == 6:
            print("""
   _
  ' `:--.--.
     |  |  |_     Virgo-  The Virgin
     |  |  | )
     |  |  |/

          """)
        elif partycount == 7:
            print("""
        __
   ___.'  '.___   Libra-  The Balance
   ____________

              """)
        elif partycount == 8:
            print("""
   _
  ' `:--.--.
     |  |  |      Scorpius-  The Scorpion
     |  |  |
     |  |  |  ..,
           `---':
             """)
        elif partycount == 9:
            print("""
          ...
          .':     Sagittarius-  The Archer
        .'
    `..'
    .'`.
             """)
        elif partycount == 10:
            print("""
            _
    \      /_)    Capricorn-  The Goat
     \    /`.
      \  /   ;
       \/ __.'

        """)
        elif partycount == 11:
            print("""
    
 .-"-._.-"-._.-   Aquarius-  The Water Bearer
 .-"-._.-"-._.-


        """)
        elif partycount == 12:
            print("""
     `-.    .-'   Pisces-  The Fishes
        :  :
      --:--:--
        :  :
     .-'    `-.
        """)

def convertJul(year,month,day,time):
    time = time.split(":")
    hour = float(time[0])
    minute = float(time[1])
    second = float(time[2])
    year = float(year)
    month = float(month)
    day = float(day)
    
    Jo = 367*year - int((7*(year + int((month + 9)/(12))))/(4))  +  int((275*month)/(9))  +  day  +  1721013.5

    JD = Jo + ((hour) + (minute/60) + (second/3600))/(24)
    return JD





    
