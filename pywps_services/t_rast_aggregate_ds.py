# ################################################ #
# This process was generated using GrassXMLtoPyWPS #
# Author: Soeren Gebbert                           #
# Mail: soerengebbert <at> googlemail <dot> com    #
# ################################################ #

from pywps.Process import WPSProcess

from PyWPSGrassModuleStarter import PyWPSGrassModuleStarter

class t_rast_aggregate_ds(WPSProcess):

  def __init__(self):
    WPSProcess.__init__(self, identifier = 't.rast.aggregate.ds', title = 'Aggregated data of an existing space time raster dataset using the time intervals of a second space time dataset.', version = 1, statusSupported = True, storeSupported = True, metadata = [{'type': 'simple', 'title': 'temporal'}, {'type': 'simple', 'title': 'aggregation'}], abstract = 'http://grass.osgeo.org/grass70/manuals/html70_user/t.rast.aggregate.ds.html')

    # Literal and complex inputs
    self.addComplexInput(identifier = 'input', title = 'Name of the input space time raster dataset', minOccurs = 1, maxOccurs = 1, formats = [{'mimeType': 'application/x-grass-strds-tar'}, {'mimeType': 'application/x-grass-strds-tar-gz'}, {'mimeType': 'application/x-grass-strds-tar-bzip'}])
    self.addComplexInput(identifier = 'sample', title = 'Time intervals from this space time dataset (raster, vector or raster3d) are used for aggregation computation', minOccurs = 1, maxOccurs = 1, formats = [{'mimeType': 'application/x-grass-strds-tar'}, {'mimeType': 'application/x-grass-strds-tar-gz'}, {'mimeType': 'application/x-grass-strds-tar-bzip'}, {'mimeType': 'application/x-grass-stvds-tar'}, {'mimeType': 'application/x-grass-stvds-tar-gz'}, {'mimeType': 'application/x-grass-stvds-tar-bzip'}])
    self.addLiteralInput(identifier = 'type', title = 'Type of the aggregation space time dataset, default is strds', minOccurs = 0, maxOccurs = 1, type = type("string"), default = "strds", allowedValues = ['strds', 'stvds', 'str3ds'])
    self.addLiteralInput(identifier = 'basename', title = 'Base name of the new generated output maps"', abstract = 'A numerical suffix separated by an underscore will be attached to create a unique identifier', minOccurs = 1, maxOccurs = 1, type = type("string"), allowedValues = '*')
    self.addLiteralInput(identifier = 'method', title = 'Aggregate operation to be peformed on the raster maps', minOccurs = 1, maxOccurs = 1, type = type("string"), default = "average", allowedValues = ['average', 'count', 'median', 'mode', 'minimum', 'min_raster', 'maximum', 'max_raster', 'stddev', 'range', 'sum', 'variance', 'diversity', 'slope', 'offset', 'detcoeff', 'quart1', 'quart3', 'perc90', 'quantile', 'skewness', 'kurtosis'])
    self.addLiteralInput(identifier = 'sampling', title = 'The method to be used for sampling the input dataset', minOccurs = 0, maxOccurs = 1024, type = type("string"), default = "start", allowedValues = ['start', 'during', 'overlap', 'contain', 'equal', 'follows', 'precedes'])
    self.addLiteralInput(identifier = '-n', title = 'Register Null maps', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])
    self.addLiteralInput(identifier = 'grass_resolution_ns', title = 'Resolution of the mapset in north-south direction in meters or degrees', abstract = 'This parameter defines the north-south resolution of the mapset in meter or degrees, which should be used to process the input and output raster data. To enable this setting, you need to specify north-south and east-west resolution.', minOccurs = 0, maxOccurs = 1, type = type(0.0), allowedValues = '*')
    self.addLiteralInput(identifier = 'grass_resolution_ew', title = 'Resolution of the mapset in east-west direction in meters or degrees', abstract = 'This parameter defines the east-west resolution of the mapset in meters or degrees, which should be used to process the input and output raster data.  To enable this setting, you need to specify north-south and east-west resolution.', minOccurs = 0, maxOccurs = 1, type = type(0.0), allowedValues = '*')

    # complex outputs
    self.addComplexOutput(identifier = 'output', title = 'Name of the output space time raster dataset', formats = [{'mimeType': 'application/x-grass-strds-tar'}, {'mimeType': 'application/x-grass-strds-tar-gz'}, {'mimeType': 'application/x-grass-strds-tar-bzip'}])

  def execute(self):
    starter = PyWPSGrassModuleStarter()
    starter.fromPyWPS("t.rast.aggregate.ds", self.inputs, self.outputs, self.pywps)

if __name__ == "__main__":
  process = t_rast_aggregate_ds()
  process.execute()
