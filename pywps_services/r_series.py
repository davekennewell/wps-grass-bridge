# ################################################ #
# This process was generated using GrassXMLtoPyWPS #
# Author: Soeren Gebbert                           #
# Mail: soerengebbert <at> googlemail <dot> com    #
# ################################################ #

from pywps.Process import WPSProcess

from PyWPSGrassModuleStarter import PyWPSGrassModuleStarter

class r_series(WPSProcess):

  def __init__(self):
    WPSProcess.__init__(self, identifier = 'r.series', title = 'Makes each output cell value a function of the values assigned to the corresponding cells in the input raster map layers.', version = 1, statusSupported = True, storeSupported = True, metadata = [{'type': 'simple', 'title': 'raster'}, {'type': 'simple', 'title': 'aggregation'}, {'type': 'simple', 'title': 'series'}], abstract = 'http://grass.osgeo.org/grass70/manuals/html70_user/r.series.html')

    # Literal and complex inputs
    self.addComplexInput(identifier = 'input', title = 'Name of input raster map(s)', minOccurs = 0, maxOccurs = 1024, formats = [{'mimeType': 'image/tiff'}, {'mimeType': 'image/geotiff'}, {'mimeType': 'application/geotiff'}, {'mimeType': 'application/x-geotiff'}, {'mimeType': 'image/png'}, {'mimeType': 'image/gif'}, {'mimeType': 'image/jpeg'}, {'mimeType': 'application/x-erdas-hfa'}, {'mimeType': 'application/netcdf'}, {'mimeType': 'application/x-netcdf'}])
    self.addComplexInput(identifier = 'file', title = 'Input file with one raster map name and optional one weight per line, field separator between name and weight is |', minOccurs = 0, maxOccurs = 1, formats = [{'mimeType': 'text/plain'}])
    self.addLiteralInput(identifier = 'method', title = 'Aggregate operation', minOccurs = 1, maxOccurs = 1024, type = type("string"), allowedValues = ['average', 'count', 'median', 'mode', 'minimum', 'min_raster', 'maximum', 'max_raster', 'stddev', 'range', 'sum', 'variance', 'diversity', 'slope', 'offset', 'detcoeff', 'tvalue', 'quart1', 'quart3', 'perc90', 'quantile', 'skewness', 'kurtosis'])
    self.addLiteralInput(identifier = 'quantile', title = 'Quantile to calculate for method=quantile', minOccurs = 0, maxOccurs = 1024, type = type(0.0), allowedValues = '*')
    self.addLiteralInput(identifier = 'weights', title = 'Weighting factor for each input map, default value is 1.0 for each input map', minOccurs = 0, maxOccurs = 1024, type = type(0.0), allowedValues = '*')
    self.addLiteralInput(identifier = 'range', title = 'Ignore values outside this range', minOccurs = 0, maxOccurs = 2, type = type(0.0), allowedValues = '*')
    self.addLiteralInput(identifier = '-n', title = 'Propagate NULLs', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])
    self.addLiteralInput(identifier = '-z', title = 'Dont keep files open', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])
    self.addLiteralInput(identifier = 'grass_resolution_ns', title = 'Resolution of the mapset in north-south direction in meters or degrees', abstract = 'This parameter defines the north-south resolution of the mapset in meter or degrees, which should be used to process the input and output raster data. To enable this setting, you need to specify north-south and east-west resolution.', minOccurs = 0, maxOccurs = 1, type = type(0.0), allowedValues = '*')
    self.addLiteralInput(identifier = 'grass_resolution_ew', title = 'Resolution of the mapset in east-west direction in meters or degrees', abstract = 'This parameter defines the east-west resolution of the mapset in meters or degrees, which should be used to process the input and output raster data.  To enable this setting, you need to specify north-south and east-west resolution.', minOccurs = 0, maxOccurs = 1, type = type(0.0), allowedValues = '*')
    self.addLiteralInput(identifier = 'grass_band_number', title = 'Band to select for processing (default is all bands)', abstract = 'This parameter defines band number of the input raster files which should be processed. As default all bands are processed and used as single and multiple inputs for raster modules.', minOccurs = 0, maxOccurs = 1, type = type(0), allowedValues = '*')

    # complex outputs
    self.addComplexOutput(identifier = 'output', title = 'Name for output raster map', formats = [{'mimeType': 'image/tiff'}, {'mimeType': 'image/geotiff'}, {'mimeType': 'application/geotiff'}, {'mimeType': 'application/x-geotiff'}, {'mimeType': 'application/x-erdas-hfa'}, {'mimeType': 'application/netcdf'}, {'mimeType': 'application/x-netcdf'}])

  def execute(self):
    starter = PyWPSGrassModuleStarter()
    starter.fromPyWPS("r.series", self.inputs, self.outputs, self.pywps)

if __name__ == "__main__":
  process = r_series()
  process.execute()
