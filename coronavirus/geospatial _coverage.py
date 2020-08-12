import numpy as np
import pandas as pd
import geopandas as gpd
from scipy.stats import gaussian_kde
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.path import Path
from matplotlib.textpath import TextToPath
import tilemapbase
import descartes
import warnings
import matplotlib.cbook

warnings.filterwarnings("ignore", category=matplotlib.cbook.mplDeprecation)
import seaborn as sns
import shapely.speedups

shapely.speedups.enable()
points = gpd.read_file('../.data/cy_1km.shp')
points = points.to_crs({"init": "EPSG:3857"})

points = points.dropna()

# edit the figure size however you need to

plt.figure(num=None, figsize=(10, 10), dpi=80, facecolor='w', edgecolor='k')

# create plot and axes

fig = plt.plot()
ax1 = plt.axes()

# these values can be changed as needed, the markers are LaTeX symbols

# city.plot(ax=ax1, alpha=0.1, edgecolor="black", facecolor="white")
points.plot(ax=ax1, alpha=0.1, color="red", marker='$\\bigtriangledown$', )
ax1.figure.savefig('./data/plot1.png')
