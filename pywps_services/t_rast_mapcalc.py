# ################################################ #
# This process was generated using GrassXMLtoPyWPS #
# Author: Soeren Gebbert                           #
# Mail: soerengebbert <at> googlemail <dot> com    #
# ################################################ #

from pywps.Process import WPSProcess

from PyWPSGrassModuleStarter import PyWPSGrassModuleStarter

class t_rast_mapcalc(WPSProcess):

  def __init__(self):
    WPSProcess.__init__(self, identifier = 't.rast.mapcalc', title = 'Perform spatio-temporal mapcalc expressions on temporal sampled maps of space time raster datasets.', version = 1, statusSupported = True, storeSupported = True, metadata = [{'type': 'simple', 'title': 'temporal'}, {'type': 'simple', 'title': 'algebra'}], abstract = 'http://grass.osgeo.org/grass70/manuals/html70_user/t.rast.mapcalc.html')

    # Literal and complex inputs
    self.addComplexInput(identifier = 'inputs', title = 'Name of the input space time raster datasets', minOccurs = 1, maxOccurs = 1024, formats = [{'mimeType': 'application/x-grass-strds-tar'}, {'mimeType': 'application/x-grass-strds-tar-gz'}, {'mimeType': 'application/x-grass-strds-tar-bzip'}])
    self.addLiteralInput(identifier = 'expression', title = 'Spatio-temporal mapcalc expression', minOccurs = 1, maxOccurs = 1, type = type("string"), allowedValues = '*')
    self.addLiteralInput(identifier = 'method', title = 'The method to be used for sampling the input dataset', minOccurs = 0, maxOccurs = 1024, type = type("string"), default = "equal", allowedValues = ['start', 'during', 'overlap', 'contain', 'equal', 'follows', 'precedes'])
    self.addLiteralInput(identifier = 'basename', title = 'Base name of the new generated output maps"', abstract = 'A numerical suffix separated by an underscore will be attached to create a unique identifier', minOccurs = 1, maxOccurs = 1, type = type("string"), allowedValues = '*')
    self.addLiteralInput(identifier = 'nprocs', title = 'Number of r.mapcalc processes to run in parallel', minOccurs = 0, maxOccurs = 1, type = type(0), default = 1)
    self.addLiteralInput(identifier = '-n', title = 'Register Null maps', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])
    self.addLiteralInput(identifier = '-s', title = 'Check spatial overlap', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])
    self.addLiteralInput(identifier = 'grass_resolution_ns', title = 'Resolution of the mapset in north-south direction in meters or degrees', abstract = 'This parameter defines the north-south resolution of the mapset in meter or degrees, which should be used to process the input and output raster data. To enable this setting, you need to specify north-south and east-west resolution.', minOccurs = 0, maxOccurs = 1, type = type(0.0), allowedValues = '*')
    self.addLiteralInput(identifier = 'grass_resolution_ew', title = 'Resolution of the mapset in east-west direction in meters or degrees', abstract = 'This parameter defines the east-west resolution of the mapset in meters or degrees, which should be used to process the input and output raster data.  To enable this setting, you need to specify north-south and east-west resolution.', minOccurs = 0, maxOccurs = 1, type = type(0.0), allowedValues = '*')

    # complex outputs
    self.addComplexOutput(identifier = 'output', title = 'Name of the output space time raster dataset', formats = [{'mimeType': 'application/x-grass-strds-tar'}, {'mimeType': 'application/x-grass-strds-tar-gz'}, {'mimeType': 'application/x-grass-strds-tar-bzip'}])

  def execute(self):
    starter = PyWPSGrassModuleStarter()
    starter.fromPyWPS("t.rast.mapcalc", self.inputs, self.outputs, self.pywps)

if __name__ == "__main__":
  process = t_rast_mapcalc()
  process.execute()
