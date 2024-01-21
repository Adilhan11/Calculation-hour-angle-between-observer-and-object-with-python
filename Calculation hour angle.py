from astropy.coordinates import Angle,SkyCoord
from astropy.time import TimeDelta,Time
import numpy as np

#hometown coordinates
lat_ev=Angle(39.994056657701854,unit="deg")
lon_ev=Angle(32.859298875626415,unit="deg")

#get right ascension and declination
vega = SkyCoord(ra="18h37m36.7s",dec="+38°48'24.9",frame="gcrs")


ra = vega.ra
dec = vega.dec
print(f"Right ascension angle :{ra}")
print(f"Declination angle :{dec}")

#import epoh 
epoh = Time("2020-11-13T09:34:33",scale="utc")
print(f"epoh:{epoh}")

#we calculate for GMT+3 
epoh = epoh - TimeDelta(3*60*60, format='sec')
print(f"epoh:{epoh}")


#calculate GAST and LAST 
GAST = epoh.sidereal_time("apparent",longitude=0)
print(f"GAST:{GAST}")
LAST = Angle(GAST,"deg") + Angle(lon_ev,"deg")
print(f"LAST:{LAST}")


#Calculate hour angle 
hour_angle = LAST.deg - ra.deg 
hour_angle = Angle(hour_angle,"deg")
print(f"hour angle:{hour_angle}")



vega = SkyCoord(ra="18h37m36.7s",dec="+38°48'24.9",frame="gcrs")

lat=Angle(39.994056657701854,unit="deg")
lon=Angle(32.859298875626415,unit="deg")

ra = vega.ra
dec = vega.dec

#Zenith direction
z = Angle(90.01,unit="deg")

#cosine rule for triangle Vega,Observer,North Pole.
h = Angle(np.degrees(np.arccos((-np.sin(dec.rad)*np.sin(lat.rad))/(np.cos(dec.rad)*np.cos(lat.rad)))), unit="deg")

print ("Hour angle is:",h.deg)

Set = ra+h

epoch = Time("2020-11-13T09:34:33",scale="utc")

LAST = epoch.sidereal_time("apparent",longitude=lon.deg)

lon_set = 0.9973*(Set-LAST)

print ("Vega Set:",epoch + TimeDelta(lon_set.deg*4*60,format="sec")+TimeDelta(3*60*60,format="sec"))