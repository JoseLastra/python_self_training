# geocomputation intro
import pandas as pd
import shapely
import geopandas as gpd

## limit the number of printed rows
pd.set_option("display.max_rows", 6)

## for reading a geopackage from our path as a geodataframe (gdf)
gdf = gpd.read_file("data/world.gpkg")

# check output class
type(gdf)
gdf.shape  # dimensions

## sf like following pandas structure so you can use pandas subset base code
gdf = gdf[["name_long", "geometry"]]
gdf

## creating a sub dataset based on a condition
## filtering egypt
gdf[gdf["name_long"] == "Egypt"]

# basic plot
gdf.plot()
