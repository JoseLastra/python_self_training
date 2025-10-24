## Raster section from Geocoputation book for python
## Raster is less organized in python  than R and than it is for vectors in general
## rasterio and rioxarray as main packages
## Rasterio as a numpy approach to rasters
## rioxarray is a rasterio wrapper
## Rasterio is better known and developed

## Import section ----------#
import numpy as np
import rasterio
import rasterio.plot

## Importing data implies open a connection and read
### open
src = rasterio.open("data/srtm.tif")
src

# super random plot
rasterio.plot.show(src)

# exploring headers
src.meta

# we can also access individually
src.driver
src.dtypes
src.nodata
src.crs
src.transform
# transform is and important attribute as relate with the raster origin

### read
# reading can be done using .read() or passing indices .read(1) read([1,2])
# this connects with numpy arrays with three dimensions (reading more than 1 layer)
# or two dimensions (1 specific layers)

# our data has only one layer
src.read(1)
# two dimensional array

## Raster data from scratch
# creating elev: 6x6 array with seq values 1:36
elev = np.arange(1, 37, dtype=np.uint8).reshape(6, 6)
elev

# creating grain: categorical values [0,1,2] clay, stilt, sand

v = [
    1,
    0,
    1,
    2,
    2,
    2,
    0,
    2,
    0,
    0,
    2,
    1,
    0,
    2,
    2,
    0,
    0,
    2,
    0,
    0,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    2,
    1,
    1,
    2,
    1,
    2,
    2,
    0,
    2,
]
grain = np.array(v, dtype=np.uint8).reshape(6, 6)
grain

## ading georeferencing info origin and resolution

new_transform = rasterio.transform.from_origin(
    west=-1.5, north=1.5, xsize=0.5, ysize=0.5
)
new_transform

#  Note that, confusingly,
#  (i.e., ysize) is defined in rasterio.transform.from_origin using a positive value (0.5), even though it is, in fact, negative (-0.5).

rasterio.plot.show(elev, transform=new_transform)
