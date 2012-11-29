# ################################################ #
# This process was generated using GrassXMLtoPyWPS #
# Author: Soeren Gebbert                           #
# Mail: soerengebbert <at> googlemail <dot> com    #
# ################################################ #

from pywps.Process import WPSProcess

from PyWPSGrassModuleStarter import PyWPSGrassModuleStarter

class t_vect_what_strds(WPSProcess):

  def __init__(self):
    WPSProcess.__init__(self, identifier = 't.vect.what.strds', title = 'Store raster map values at spatial and temporal positions of vector points as vector attributes.', version = 1, statusSupported = True, storeSupported = True, metadata = [{'type': 'simple', 'title': 'temporal'}, {'type': 'simple', 'title': 'sampling'}], abstract = 'http://grass.osgeo.org/grass70/manuals/html70_user/t.vect.what.strds.html')

    # Literal and complex inputs
    self.addComplexInput(identifier = 'input', title = 'Name of the input space time vector dataset', minOccurs = 1, maxOccurs = 1, formats = [{'mimeType': 'application/x-grass-stvds-tar'}, {'mimeType': 'application/x-grass-stvds-tar-gz'}, {'mimeType': 'application/x-grass-stvds-tar-bzip'}])
    self.addComplexInput(identifier = 'strds', title = 'Name of the input space time raster dataset', minOccurs = 1, maxOccurs = 1, formats = [{'mimeType': 'application/x-grass-strds-tar'}, {'mimeType': 'application/x-grass-strds-tar-gz'}, {'mimeType': 'application/x-grass-strds-tar-bzip'}])
    self.addLiteralInput(identifier = 'column', title = 'The use of a column name forces t.vect.what.rast to sample only values from the first map found in an interval. Otherwise the raster map names are used as column names', minOccurs = 0, maxOccurs = 1, type = type("string"), allowedValues = '*')
    self.addLiteralInput(identifier = 'method', title = 'Aggregate operation to be performed on the raster maps', minOccurs = 1, maxOccurs = 1, type = type("string"), default = "disabled", allowedValues = ['disabled', 'average', 'count', 'median', 'mode', 'minimum', 'min_raster', 'maximum', 'max_raster', 'stddev', 'range', 'sum', 'variance', 'diversity', 'slope', 'offset', 'detcoeff', 'quart1', 'quart3', 'perc90', 'quantile', 'skewness', 'kurtosis'])
    self.addLiteralInput(identifier = 'where', title = 'Example: income &#60; 1000 and inhab &#62;= 10000', minOccurs = 0, maxOccurs = 1, type = type("string"), allowedValues = '*')
    self.addLiteralInput(identifier = 't_where', title = 'Example: start_time &#62; 2001-01-01 12:30:00', minOccurs = 0, maxOccurs = 1, type = type("string"), allowedValues = '*')
    self.addLiteralInput(identifier = 'sampling', title = 'The method to be used for sampling the input dataset', minOccurs = 0, maxOccurs = 1024, type = type("string"), default = "start", allowedValues = ['start', 'during', 'overlap', 'contain', 'equal', 'follows', 'precedes'])
    self.addLiteralInput(identifier = 'grass_resolution_ns', title = 'Resolution of the mapset in north-south direction in meters or degrees', abstract = 'This parameter defines the north-south resolution of the mapset in meter or degrees, which should be used to process the input and output raster data. To enable this setting, you need to specify north-south and east-west resolution.', minOccurs = 0, maxOccurs = 1, type = type(0.0), allowedValues = '*')
    self.addLiteralInput(identifier = 'grass_resolution_ew', title = 'Resolution of the mapset in east-west direction in meters or degrees', abstract = 'This parameter defines the east-west resolution of the mapset in meters or degrees, which should be used to process the input and output raster data.  To enable this setting, you need to specify north-south and east-west resolution.', minOccurs = 0, maxOccurs = 1, type = type(0.0), allowedValues = '*')

    # complex outputs
    self.addComplexOutput(identifier = 'stdout', title = 'Module output on stdout', abstract = 'The output of the module written to stdout', formats = [{'mimeType': 'text/plain'}])

  def execute(self):
    starter = PyWPSGrassModuleStarter()
    starter.fromPyWPS("t.vect.what.strds", self.inputs, self.outputs, self.pywps)

if __name__ == "__main__":
  process = t_vect_what_strds()
  process.execute()
