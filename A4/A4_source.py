# import necessary libraries
import numpy as np
import rasterio as rio
from rasterio.plot import show
import A4_functions


# task: read a raster file (Data: Sentinel-2) and perform an index calculation
# the calculated index wil be the normalized difference vegetation index (NDVI)
# the instructions to this index can be found at https://www.indexdatabase.de/db/i-single.php?id=391

# for this script, the necessary data are stored locally on the machine

# data can be found at https://browser.dataspace.copernicus.eu/?zoom=9&lat=38.44897&lng=66.93311&themeId=DEFAULT-THEME&visualizationUrl=U2FsdGVkX18wEuUwqWryjONcimFkAuyOmkGwRNrXfvUXR44a7bE2gtbe1tXdmx8Y0z6q3i3NJvwG25o83YxierXMsqk7hG68Np%2BCp5LACOYARUPfOPjU9hOgdE7bxLct&datasetId=S2_L2A_CDAS&fromTime=2025-06-02T00%3A00%3A00.000Z&toTime=2025-06-02T23%3A59%3A59.999Z&layerId=1_TRUE_COLOR
# or in this repo in the data folder

# setting up environment and reading datasets
# reading datasets is a crucial step and quite easy with rasterio
# for a script like this, an opening and closing dataset system enforced by the "with" keyword isn't necessary
# but I decided to use it for demonstration purposes.
# The documentation to this and many more functions and features can be found at https://rasterio.readthedocs.io/en/stable/

with rio.Env():
    with rio.open(fp="A4\\data\\T42SUG_20240523T061629_B04_10m.jp2", driver="JP2OpenJPEG") as red, rio.open(fp="A4\\data\\T42SUG_20240523T061629_B08_10m.jp2", driver="JP2OpenJPEG") as nir:

        # you will have to download sentinel imagery yourself, as I could not upload it to this repository, due to its size

        # converting from DN to reflectance values
        r1 = red.read(1).astype('float32') / 10000
        nir1 = nir.read(1).astype('float32') / 10000

        # masking missing values
        mask = (r1 + nir1) == 0

        # calculating ndvi, ignoring missing values and giving them the numpy notANumber-value
        ndvi = np.where(~mask, (nir1 - r1) / (nir1 + r1), np.nan)

        # generating a map as an intermediate result
        show(ndvi, cmap="RdYlGn")

        # generating masks depending on ndvi value. This can be adapted further by combining different indices etc.
        # so that more exact masks are produced
        veg = (ndvi > 0.2) & (ndvi < 0.6)
        healthyVeg = ndvi > 0.6
        other = ndvi < 0.2

        # the masks could be exported for further analysis
        show(healthyVeg)

        highFiltered = A4_functions.highPassFilter(ndvi)
        lowFiltered = A4_functions.lowPassFilter(ndvi)
        edges = A4_functions.edgeDetectionFilter(ndvi)

        show(highFiltered)
        show(lowFiltered)
        show(edges)

    # this is a simple workflow, however this could be executed in a loop with thousands of datasets and comparisons
    # over times or counts of ndvi ranges over time could be generated
    # this could indicate where healthy vegetation has been how many times in a year in a region

    # write to the mask into a new file
        with rio.open("A4\\data\\ndviBasedHealthyVeg.tif", "w", driver="GTiff", width=r1.shape[1], height=r1.shape[0], count=1, dtype=rio.uint16, crs=red.crs, transform=red.transform) as dst:
            dst.write(healthyVeg, 1)
        with rio.open("A4\\data\\ndviBasedHighFiltered.tif", "w", driver="GTiff", width=r1.shape[1], height=r1.shape[0], count=1, dtype=rio.float32, crs=red.crs, transform=red.transform) as dst:
            dst.write(highFiltered, 1)
        with rio.open("A4\\data\\ndviBasedLowFiltered.tif", "w", driver="GTiff", width=r1.shape[1], height=r1.shape[0], count=1, dtype=rio.float32, crs=red.crs, transform=red.transform) as dst:
            dst.write(lowFiltered, 1)
        with rio.open("A4\\data\\ndviBasedEdges.tif", "w", driver="GTiff", width=r1.shape[1], height=r1.shape[0], count=1, dtype=rio.float32, crs=red.crs, transform=red.transform) as dst:
            dst.write(edges, 1)
