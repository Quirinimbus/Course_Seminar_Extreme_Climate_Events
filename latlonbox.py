#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 11:59:03 2022

@author: mixteco
"""

import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
import sys
import warnings
import shapely.geometry as sgeom
import cartopy.feature

if not sys.warnoptions:
    warnings.simplefilter("ignore")


####      Global          ################


box = sgeom.box(minx=-100, maxx=-20, miny=-60, maxy=20)  

x0, y0, x1, y1 = box.bounds

proj = ccrs.PlateCarree(central_longitude=0)

# ax1 = plt.subplot(211,projection=proj) 
# ax1.stock_img() 
# ax1.add_geometries([box], proj, facecolor='coral',edgecolor='black', alpha=0.5) 
# plt.title('Global')

  
# ax2 = plt.subplot(212, projection=proj) 
# ax2.stock_img() 
# ax2.set_extent([x0, x1, y0, y1], proj) 
# plt.title('Mediterranean')

# ax2.add_feature(cartopy.feature.LAND) 
# ax2.add_feature(cartopy.feature.OCEAN) 
# ax2.coastlines('50m')

#plt.savefig('Mediterranean.jpg',bbox_inches='tight', dpi=300)

#plt.show()


# ####        TEXAS       #########################

box2 = sgeom.box(minx=-50, maxx=-45, miny=-25, maxy=-20)

x2, y2, x3, y3 = box2.bounds

ax2 = plt.subplot(211, projection=proj) 
ax2.stock_img() 
ax2.set_extent([x0, x1, y0, y1], proj)
ax2.add_geometries([box2], proj, facecolor='coral',edgecolor='black', alpha=0.5) 
plt.title('South America')

ax2.add_feature(cartopy.feature.LAND) 
ax2.add_feature(cartopy.feature.OCEAN) 
ax2.coastlines('50m')

ax3 = plt.subplot(212, projection=proj) 
ax3.stock_img() 
ax3.set_extent([x2, x3, y2, y3], proj) 
plt.title('Sao Paulo Metro-Region')

ax3.add_feature(cartopy.feature.LAND) 
ax3.add_feature(cartopy.feature.OCEAN) 
ax3.coastlines('50m')

plt.savefig('SAO_PAULO.jpg',bbox_inches='tight', dpi=150)

plt.show()


####        IDA       #########################

# box2 = sgeom.box(minx=-92, maxx=-86, miny=28.5, maxy=27.5)

# x2, y2, x3, y3 = box2.bounds

# ax2 = plt.subplot(211, projection=proj) 
# ax2.stock_img() 
# ax2.set_extent([x0, x1, y0, y1], proj)
# ax2.add_geometries([box2], proj, facecolor='coral',edgecolor='black', alpha=0.5) 
# plt.title('IDA')

# ax2.add_feature(cartopy.feature.LAND) 
# ax2.add_feature(cartopy.feature.OCEAN) 
# ax2.coastlines('50m')

# # ax3 = plt.subplot(212, projection=proj) 
# # ax3.stock_img() 
# # ax3.set_extent([x2, x3, y2, y3], proj) 
# # plt.title('IDA')

# # ax3.add_feature(cartopy.feature.LAND) 
# # ax3.add_feature(cartopy.feature.OCEAN) 
# # ax3.coastlines('50m')

# #plt.savefig('IDA2.jpg',bbox_inches='tight', dpi=300)

# plt.show()

####        Tunisia       #########################

# box2 = sgeom.box(minx=7.5, maxx=11.6, miny=30.1, maxy=38.5)

# x2, y2, x3, y3 = box2.bounds

# ax2 = plt.subplot(211, projection=proj) 
# ax2.stock_img() 
# ax2.set_extent([x0, x1, y0, y1], proj)
# ax2.add_geometries([box2], proj, facecolor='coral',edgecolor='black', alpha=0.5) 
# plt.title('Mediterranean')

# ax2.add_feature(cartopy.feature.LAND) 
# ax2.add_feature(cartopy.feature.OCEAN) 
# ax2.coastlines('50m')

# ax3 = plt.subplot(212, projection=proj) 
# ax3.stock_img() 
# ax3.set_extent([x2, x3, y2, y3], proj) 
# plt.title('Tunisia')

# ax3.add_feature(cartopy.feature.LAND) 
# ax3.add_feature(cartopy.feature.OCEAN) 
# ax3.coastlines('50m')

#plt.savefig('Tunisia.jpg',bbox_inches='tight', dpi=300)

plt.show()
