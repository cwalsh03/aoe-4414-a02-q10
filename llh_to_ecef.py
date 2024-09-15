# llh_to_ecef.py
#
# Usage: python3 llh_to_ecef.py lat_deg lon_deg hae_km
#  Converts LLH to ECEF
# Parameters:
#  lat_deg: latitude in deg
#  lon_deg: longitude in deg
#   hae_km: height above ellipsoid in km
#  ...
# Output:
#   Prints the x y and z ECEF components in km
#
# Written by Connor Walsh
# Other contributors: Brad Denby
#

# import Python modules
# e.g., import math # math module
import sys # argv
import math # math module

# "constants"
R_E_KM = 6378.1363
e_E = 0.081819221456

# helper functions
## calculated denominator
def calc_denom(ecc, lat_rad):
    return math.sqrt(1.0-(e_E**2)*(math.sin(lat_rad)**2))


# initialize script arguments
lat_deg = float('nan')  # latitude in deg
long_deg = float('nan')  # longitude in deg
hae_km = float('nan')   # height above ellipsoid in km

# parse script arguments
if len(sys.argv)==4:
    lat_deg = float(sys.argv[1])
    long_deg = float(sys.argv[2])
    hae_km = float(sys.argv[3])
else:
   print(\
    'Usage: '\
    'python3 llh_to_ecef.py lat_deg long_deg hae_km'\
   )
   exit()

# write script below this line
lat_rad = lat_deg * (math.pi/180)
long_rad = long_deg * (math.pi/180)

denom = calc_denom(e_E, lat_rad)
C_E = R_E_KM / denom
S_E = (R_E_KM*(1 - e_E*e_E)) / denom

r_x_km = (C_E + hae_km)*math.cos(lat_rad)*math.cos(long_rad)
r_y_km = (C_E + hae_km)*math.cos(lat_rad)*math.sin(long_rad)
r_z_km = (S_E + hae_km)*math.sin(lat_rad)
r_mag_km = math.sqrt(r_x_km*r_x_km + r_y_km*r_y_km + r_z_km*r_z_km)

# print ECEF coordinates:
print(r_x_km)
print(r_y_km)
print(r_z_km)