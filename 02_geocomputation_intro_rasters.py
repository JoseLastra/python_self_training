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
