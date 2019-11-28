#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 14:00:33 2019

@author: helenetonchia
"""

import cartopy.crs as ccrs
import matplotlib.pyplot as plt

import cartopy.io.img_tiles as cimgt

def plot_track_with_tiles(tiler, title=None, **kwargs):
    """
    plot a track in latitudes and longitudes coordinate
    and add the tiles corresponding to the chosen tiler
    for example OSM or GoogleTiles from cartopy_fork.io.img_tiles
    the plot is in the crs of the tiler, Mercator for OSM and GoogleTiles
    kwargs is for the plot options
    """
    lons = [2.28495, 2.28502, 2.28471, 2.28521, 2.28548, 2.28577, 2.28617, 2.28376,
            2.28217, 2.28049]
    lats = [48.76278, 48.76538, 48.76818, 48.77056, 48.77379, 48.77591, 48.77703,
            48.77775, 48.77897, 48.77996]

    plt.figure(figsize=(10, 6.2))
    axe = plt.axes(projection=tiler.crs)
    axe.plot(lons, lats, color='red', transform=ccrs.Geodetic(), **kwargs)
    if title:
        axe.set_title(title)

    zoom = 12
    axe.add_image(tiler, zoom)

    plt.show()
    if title:
        plt.savefig(title+'.png')

for provider in [
        {'tiler' : cimgt.OSM(), 'title' : 'OSM'},
        {'tiler' : cimgt.GoogleTiles(), 'title' : 'GoogleTiles'},
        {'tiler' : cimgt.MapQuestOpenAerial(), 'title' : 'MapQuestOpenAerial'},
        #this last one raises an errot which is managed
        {'tiler' : cimgt.Stamen(), 'title' : 'Stamen'},
        {'tiler' : cimgt.QuadtreeTiles(), 'title' : 'QuadtreeTiles'},
        ]:
    print(provider['title'])
    plot_track_with_tiles(provider['tiler'], title=provider['title'], lw=3)
