# ################################################ #
# This process was generated using GrassXMLtoPyWPS #
# Author: Soeren Gebbert                           #
# Mail: soerengebbert <at> googlemail <dot> com    #
# ################################################ #

from pywps.Process import WPSProcess

from PyWPSGrassModuleStarter import PyWPSGrassModuleStarter

class t_rast_aggregate(WPSProcess):

  def __init__(self):
    WPSProcess.__init__(self, identifier = 't.rast.aggregate', title = 'Temporally aggregates the maps of a space time raster dataset by a user defined granularity.', version = 1, statusSupported = True, storeSupported = True, metadata = [{'type': 'simple', 'title': 'temporal'}, {'type': 'simple', 'title': 'aggregation'}], abstract = 'http://grass.osgeo.org/grass70/manuals/html70_user/t.rast.aggregate.html')

    # Literal and complex inputs
    self.addComplexInput(identifier = 'input', title = 'Name of the input space time raster dataset', minOccurs = 1, maxOccurs = 1, formats = [{'mimeType': 'application/x-grass-strds-tar'}, {'mimeType': 'application/x-grass-strds-tar-gz'}, {'mimeType': 'application/x-grass-strds-tar-bzip'}])
    self.addComplexInput(identifier = 'base', title = 'Name of base raster map', minOccurs = 1, maxOccurs = 1, formats = [{'mimeType': 'image/tiff'}, {'mimeType': 'image/geotiff'}, {'mimeType': 'application/geotiff'}, {'mimeType': 'application/x-geotiff'}, {'mimeType': 'image/png'}, {'mimeType': 'image/gif'}, {'mimeType': 'image/jpeg'}, {'mimeType': 'application/x-erdas-hfa'}, {'mimeType': 'application/netcdf'}, {'mimeType': 'application/x-netcdf'}])
    self.addLiteralInput(identifier = 'granularity', title = 'Aggregation granularity, format absolute time "x years, x months, x weeks, x days, x hours, x minutes, x seconds" or an integer value for relative time', minOccurs = 1, maxOccurs = 1, type = type("string"), allowedValues = '*')
    self.addLiteralInput(identifier = 'method', title = 'Aggregate operation to be performed on the raster maps', minOccurs = 1, maxOccurs = 1, type = type("string"), default = "average", allowedValues = ['average', 'count', 'median', 'mode', 'minimum', 'min_raster', 'maximum', 'max_raster', 'stddev', 'range', 'sum', 'variance', 'diversity', 'slope', 'offset', 'detcoeff', 'quart1', 'quart3', 'perc90', 'quantile', 'skewness', 'kurtosis'])
    self.addLiteralInput(identifier = 'sampling', title = 'The method to be used for sampling the input dataset', minOccurs = 0, maxOccurs = 1024, type = type("string"), default = "start", allowedValues = ['start', 'during', 'overlap', 'contain', 'equal', 'follows', 'precedes'])
    self.addLiteralInput(identifier = 'where', title = 'Example: start_time &#62; 2001-01-01 12:30:00', minOccurs = 0, maxOccurs = 1, type = type("string"), allowedValues = '*')
    self.addLiteralInput(identifier = '-n', title = 'Register Null maps', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])
    self.addLiteralInput(identifier = 'grass_resolution_ns', title = 'Resolution of the mapset in north-south direction in meters or degrees', abstract = 'This parameter defines the north-south resolution of the mapset in meter or degrees, which should be used to process the input and output raster data. To enable this setting, you need to specify north-south and east-west resolution.', minOccurs = 0, maxOccurs = 1, type = type(0.0), allowedValues = '*')
    self.addLiteralInput(identifier = 'grass_resolution_ew', title = 'Resolution of the mapset in east-west direction in meters or degrees', abstract = 'This parameter defines the east-west resolution of the mapset in meters or degrees, which should be used to process the input and output raster data.  To enable this setting, you need to specify north-south and east-west resolution.', minOccurs = 0, maxOccurs = 1, type = type(0.0), allowedValues = '*')
    self.addLiteralInput(identifier = 'grass_band_number', title = 'Band to select for processing (default is all bands)', abstract = 'This parameter defines band number of the input raster files which should be processed. As default all bands are processed and used as single and multiple inputs for raster modules.', minOccurs = 0, maxOccurs = 1, type = type(0), allowedValues = '*')

    # complex outputs
    self.addComplexOutput(identifier = 'output', title = 'Name of the output space time raster dataset', formats = [{'mimeType': 'application/x-grass-strds-tar'}, {'mimeType': 'application/x-grass-strds-tar-gz'}, {'mimeType': 'application/x-grass-strds-tar-bzip'}])

  def execute(self):
    starter = PyWPSGrassModuleStarter()
    starter.fromPyWPS("t.rast.aggregate", self.inputs, self.outputs, self.pywps)

if __name__ == "__main__":
  process = t_rast_aggregate()
  process.execute()
