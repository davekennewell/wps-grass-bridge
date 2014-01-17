# ################################################ #
# This process was generated using GrassXMLtoPyWPS #
# Author: Soeren Gebbert                           #
# Mail: soerengebbert <at> googlemail <dot> com    #
# ################################################ #

from pywps.Process import WPSProcess

from PyWPSGrassModuleStarter import PyWPSGrassModuleStarter

class t_rast_series(WPSProcess):

  def __init__(self):
    WPSProcess.__init__(self, identifier = 't.rast.series', title = 'Performs different aggregation algorithms from r.series on all or a subset of raster maps in a space time raster dataset.', version = 1, statusSupported = True, storeSupported = True, metadata = [{'type': 'simple', 'title': 'temporal'}, {'type': 'simple', 'title': 'series'}], abstract = 'http://grass.osgeo.org/grass70/manuals/html70_user/t.rast.series.html')

    # Literal and complex inputs
    self.addComplexInput(identifier = 'input', title = 'Name of the input space time raster dataset', minOccurs = 1, maxOccurs = 1, formats = [{'mimeType': 'application/x-grass-strds-tar'}, {'mimeType': 'application/x-grass-strds-tar-gz'}, {'mimeType': 'application/x-grass-strds-tar-bzip'}])
    self.addLiteralInput(identifier = 'method', title = 'Aggregate operation to be performed on the raster maps', minOccurs = 1, maxOccurs = 1, type = type("string"), default = "average", allowedValues = ['average', 'count', 'median', 'mode', 'minimum', 'min_raster', 'maximum', 'max_raster', 'stddev', 'range', 'sum', 'variance', 'diversity', 'slope', 'offset', 'detcoeff', 'quart1', 'quart3', 'perc90', 'quantile', 'skewness', 'kurtosis'])
    self.addLiteralInput(identifier = 'order', title = 'Sort the maps by category', minOccurs = 0, maxOccurs = 1024, type = type("string"), default = "id", allowedValues = ['id', 'name', 'creator', 'mapset', 'creation_time', 'modification_time', 'start_time', 'end_time', 'north', 'south', 'west', 'east', 'min', 'max'])
    self.addLiteralInput(identifier = 'where', title = 'Example: start_time &#62; 2001-01-01 12:30:00', minOccurs = 0, maxOccurs = 1, type = type("string"), allowedValues = '*')
    self.addLiteralInput(identifier = '-t', title = 'Do not assign the space time raster dataset start and end time to the output map', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])
    self.addLiteralInput(identifier = '-n', title = 'Propagate NULLs', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])
    self.addLiteralInput(identifier = 'grass_resolution_ns', title = 'Resolution of the mapset in north-south direction in meters or degrees', abstract = 'This parameter defines the north-south resolution of the mapset in meter or degrees, which should be used to process the input and output raster data. To enable this setting, you need to specify north-south and east-west resolution.', minOccurs = 0, maxOccurs = 1, type = type(0.0), allowedValues = '*')
    self.addLiteralInput(identifier = 'grass_resolution_ew', title = 'Resolution of the mapset in east-west direction in meters or degrees', abstract = 'This parameter defines the east-west resolution of the mapset in meters or degrees, which should be used to process the input and output raster data.  To enable this setting, you need to specify north-south and east-west resolution.', minOccurs = 0, maxOccurs = 1, type = type(0.0), allowedValues = '*')

    # complex outputs
    self.addComplexOutput(identifier = 'output', title = 'Name for output raster map', formats = [{'mimeType': 'image/tiff'}, {'mimeType': 'image/geotiff'}, {'mimeType': 'application/geotiff'}, {'mimeType': 'application/x-geotiff'}, {'mimeType': 'application/x-erdas-hfa'}, {'mimeType': 'application/netcdf'}, {'mimeType': 'application/x-netcdf'}])

  def execute(self):
    starter = PyWPSGrassModuleStarter()
    starter.fromPyWPS("t.rast.series", self.inputs, self.outputs, self.pywps)

if __name__ == "__main__":
  process = t_rast_series()
  process.execute()
