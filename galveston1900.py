#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 14:08:53 2022

@author: mixteco
"""

import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import sys
import warnings
import shapely.geometry as sgeom
import time
import cartopy.feature
from matplotlib.animation import FuncAnimation

if not sys.warnoptions:
    warnings.simplefilter("ignore")


file1 = '/home/mixteco/Documents/UNIBE/FS2022/extreme_climate_events/extre_py/galveston1900_prmsl.nc'
file2 = '/home/mixteco/Documents/UNIBE/FS2022/extreme_climate_events/extre_py/galveston1900_wspd10m.nc'
file3 = '/home/mixteco/Documents/UNIBE/FS2022/extreme_climate_events/extre_py/galveston1900_u10m.nc'
file4 = '/home/mixteco/Documents/UNIBE/FS2022/extreme_climate_events/extre_py/galveston1900_v10m.nc'


ds = xr.open_dataset(file1)

ds2 = xr.open_dataset(file2)

#ds3 = xr.open_dataset(file3)

#ds4 = xr.open_dataset(file4)

#ax.quiver(lons[::2,::2], lats[::2,::2], u_wind[::2,::2], v_wind[::2,::2]

#print(ds2.wspd10m.values * 3.6)

ds2.wspd10m.values = ds2.wspd10m.values * 3.6

ds2.wspd10m.attrs['units'] = 'kmph'
#print(ds3.u10m)

minds = xr.Dataset.values(file1)

print(ds)

print(ds2)

# for i in range(56):    
#     x = ds.prmsl.isel(ensemble_member=i).min()
#     y = ds2.wspd10m.isel(ensemble_member=i).max()
#     print(i,y)


#print(ds.prmsl.isel(ensemble_member=8).min())

#print(ds2.wspd10m.isel(ensemble_member=30).max())

###################################################33

#ds.prmsl.isel(time=1, ensemble_member=1).plot.contour()

#ax = plt.axes(projection=ccrs.PlateCarree())

min = ds.prmsl.min()

names = list()

levels1 = range(0,200,20)

for j in range(40,75):
    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.set_extent([-102,-79,17,35])
    #ax.set_extent([-110,-10,10,35])
    ax.coastlines()
    ax.add_feature(cfeature.BORDERS)
    #ax.set_extent([-110,-10,10,35])   
    #ds.prmsl.isel(time=33, ensemble_member=j).plot.contour(ax=ax, colors='k', transform=ccrs.PlateCarree())
    
    ds2.wspd10m.isel(time=j, ensemble_member=8).plot.contourf(ax=ax,levels=levels1, cmap='BuPu',transform=ccrs.PlateCarree())
    date = np.datetime_as_string(ds2.time[j], timezone='UTC')[:16]
    print(date)
    ax.set_title('Hurrcaine Gaveston, Timestep: '+ date)    
    #plt.savefig("Galveston_atlantic"+ str(j) +"hur.jpg",bbox_inches='tight', dpi=150)
    plt.savefig(date +"Galveston_gulf"+"hur.jpg",bbox_inches='tight', dpi=300)
    #print('Finished plotting for {}'.format(run[j]))
    
    plt.show()
    plt.close()


#######################################################################################3


# for l in range(0,113):
#     ax = plt.axes(projection=ccrs.PlateCarree())
#     #
#     #ax.set_extent([-102,-79,17,35])
#     ax.set_extent([-110,-10,10,45])
#     ax.coastlines()
#     ax.add_feature(cfeature.BORDERS)
    
#     ds.prmsl.isel(time=l, ensemble_member=8).plot.contour(ax=ax, transform=ccrs.PlateCarree())
#     ds2.wspd10m.isel(time=l, ensemble_member=8).plot.contourf(ax=ax,levels=levels1, cmap='BuPu',transform=ccrs.PlateCarree())
#     date = np.datetime_as_string(ds2.time[l], timezone='UTC')[:16]
#     #print(date)
#     ax.set_title('Hurrcaine Gaveston, Timestep: '+ date)    
#     #plt.savefig("Galveston_atlantic"+ str(j) +"hur.jpg",bbox_inches='tight', dpi=150)
#     #plt.savefig("Galveston_gulf"+ str(j) +"hur.jpg",bbox_inches='tight', dpi=300)
#     #print('Finished plotting for {}'.format(run[j]))
    
#     plt.show()
#     plt.close()