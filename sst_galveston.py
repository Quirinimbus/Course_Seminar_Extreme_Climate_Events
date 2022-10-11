#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  6 15:23:49 2022

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

sstfile = '/home/mixteco/Documents/UNIBE/FS2022/extreme_climate_events/extre_py/ersst.v5.190009.nc'

sstds = xr.open_dataset(sstfile)

#sstds.sst.attrs['units'] = '°C'

print(sstds.sst)

levels0 = range(20,35,1)

ax = plt.axes(projection=ccrs.PlateCarree())

ax.set_extent([-110,-10,10,45])
ax.coastlines()
ax.add_feature(cfeature.BORDERS)
 
sstds.sst.isel(time = 0, lev = 0).plot.contourf(ax = ax, levels = levels0, cmap ='hot_r',
                                                 transform=ccrs.PlateCarree(), cbar_kwargs=dict(label = "SST °C", location='bottom'))

ax.set_title('Sea Surface Temperature for September 1900')

plt.savefig("091900_SST.jpg",bbox_inches='tight', dpi=300)
   
# #ds.prmsl.isel(time=l, ensemble_member=8).plot.contour(ax=ax, transform=ccrs.PlateCarree())
# # 