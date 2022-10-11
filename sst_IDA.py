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
from metpy.units import units

sstfile = '/home/mixteco/Documents/UNIBE/FS2022/extreme_climate_events/extre_py/20210825000000-NAVO-L4_GHRSST-SST1m-K10_SST-GLOB-v02.0-fv01.0.nc'
#sstfile = '/home/mixteco/Documents/UNIBE/FS2022/extreme_climate_events/extre_py/SST_20210830.nc'

#sstfile = '/home/mixteco/Documents/UNIBE/FS2022/extreme_climate_events/extre_py/SST_29082021.nc'

#sstfile = '/home/mixteco/Documents/UNIBE/FS2022/extreme_climate_events/extre_py/SST_28082021.nc'

sstds = xr.open_dataset(sstfile)

# sstds.sst.attrs['units'] = '°C'

print(sstds)

#sert latitude and longitud

sstds.analysed_sst.values = sstds.analysed_sst.values - 273 

sstds.analysed_sst.attrs['units'] = '°C'
levels0 = range(25,35,1)
ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_extent([-100,-70,15,33])
# #levels
ax.coastlines()

ax.add_feature(cartopy.feature.RIVERS)


#sstds.analysed_sst.isel(time = 0).plot.contourf()
sstds.analysed_sst.isel(time = 0).plot.contourf(ax = ax, levels = levels0, cmap ='hot_r',
                                             transform=ccrs.PlateCarree(), cbar_kwargs=dict(label = "SST °C"))
# # analysed_sst
# #sstds.analysed_sst.isel(time = 0).plot()
#sstds.sea_surface_temperature.isel(time = 0).plot.contourf(ax = ax, cmap ='Reds',
#                                                transform=ccrs.PlateCarree(), cbar_kwargs=dict(label = "SST °C", location='bottom'))

ax.set_title('Sea Surface Temperature 26-08-2021')

plt.savefig("IDA26082021_SST.jpg",bbox_inches='tight', dpi=300)
   
#ds.prmsl.isel(time=l, ensemble_member=8).plot.contour(ax=ax, transform=ccrs.PlateCarree())
# 
