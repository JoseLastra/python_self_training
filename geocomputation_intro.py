# geocomputation intro
import pandas as pd
import shapely
import geopandas as gpd

## >>> pip install folium matplotlib mapclassify needed for  interactive view
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

## interactive
gdf.explore()

## subsets can be plotted as well
gdf[gdf["name_long"] == "Egypt"].explore()

## geopandas is essentially and sf so it has a geometry column
gdf.geometry

## crs data
gdf.geometry.crs

## bbox
gdf.envelope
gdf.geometry.envelope

## centroid, convex hull among others return just the sfc kind of geometry not the data frame
## if you want the data later it is better to create a copy of the data in a different object

gdf_2 = gdf.copy()
gdf_2.geometry = gdf.envelope
gdf_2

## checking geometry Note: as sf, a column may have several geom types
gdf.geometry.type
gdf.geom_type

## summarize geom types can be done with pandas .value_counts()
gdf.geometry.type.value_counts()

## A geodataframe can gav multiple geo series
gdf["bbox"] = gdf.envelope
gdf["polygon"] = gdf.geometry
gdf

# only one geom column can be active for operations like centroid or others
## you can change that column by
gdf = gdf.set_geometry("bbox")
gdf.explore()

gdf = gdf.set_geometry("polygon")
gdf.explore()

## Geometry
# each elements is a geometry of class shapely
gdf.geometry.iloc[3]  # simple subset

gdf[gdf["name_long"] == "Egypt"].geometry.iloc[0]

# shapely is compatible with sf standard support for seven geom types

# example creating a point
point = shapely.Point([5, 2])
point

# we can use a WKT string to create a geometry via shapely.from_wkt
point = shapely.from_wkt("POINT (5 2)")
point

## linestrings
linestring = shapely.LineString([(1, 5), (4, 4), (4, 1), (2, 2), (3, 2)])
linestring

## Polygon. note the first and last coordinate must be the same to close the polygon
polygon = shapely.Polygon(
    [(1, 5), (2, 2), (4, 1), (4, 4), (1, 5)],  ## Exterior
    [[(2, 4), (3, 4), (3, 3), (2, 3), (2, 4)]],  ## Hole(s)
)
polygon

# multipoint
multipoint = shapely.MultiPoint([(5, 2), (1, 3), (3, 4), (3, 2)])
multipoint

# multiline string
multilinestring = shapely.MultiLineString(
    [
        [(1, 5), (4, 4), (4, 1), (2, 2), (3, 2)],  ## 1st sequence
        [(1, 2), (2, 4)],  ## 2nd sequence, etc.
    ]
)
multilinestring

# multipolygon
multipolygon = shapely.MultiPolygon(
    [
        [[(1, 5), (2, 2), (4, 1), (4, 4), (1, 5)], []],  ## Polygon 1
        [[(0, 2), (1, 2), (1, 3), (0, 3), (0, 2)], []],  ## Polygon 2, etc.
    ]
)
multipolygon

## you can merge everything in a Geometrycollection
geometrycollection = shapely.GeometryCollection([multipoint, multilinestring])
geometrycollection

## shapely geometries are lac atomic units of vector data.
## GeoSeries and GeoDataFrame are used to deal with sets of shapely geometries collectively

multipolygon.buffer(0.2).difference(multipolygon)

## by default we saw an image in positron or jupyternotebooks
# but to see the WKT we can use print
print(linestring)

# raw coordinates combination of .exterior.coords
list(polygon.exterior.coords)

## adding elements to a geoSeries
lnd_point = shapely.Point(0.1, 51.5)
lnd_point

# GeoSeries
lnd_geom = gpd.GeoSeries([lnd_point], crs=4326)
lnd_geom

# combine the GeoSeries with a dictionary of attributes
lnd_data = {
    "name": ["London"],
    "temperature": [25],
    "date": ["2023-06-21"],
    "geometry": lnd_geom,
}

# Parse to GeoDataFrame
lnd_layer = gpd.GeoDataFrame(lnd_data)  # do not forget that gpd is geopandas!
lnd_layer

## example for more than one feature
lnd_point = shapely.Point(0.1, 51.5)
paris_point = shapely.Point(2.3, 48.9)
towns_geom = gpd.GeoSeries([lnd_point, paris_point], crs=4326)
towns_data = {
    "name": ["London", "Paris"],
    "temperature": [25, 27],
    "date": ["2013-06-21", "2013-06-21"],
    "geometry": towns_geom,
}
towns_layer = gpd.GeoDataFrame(towns_data)
towns_layer

# interactive view
