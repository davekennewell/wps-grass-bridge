# ################################################ #
# This process was generated using GrassXMLtoPyWPS #
# Author: Soeren Gebbert                           #
# Mail: soerengebbert <at> googlemail <dot> com    #
# ################################################ #

from pywps.Process import WPSProcess

from PyWPSGrassModuleStarter import PyWPSGrassModuleStarter

class t_rast_accumulate(WPSProcess):

  def __init__(self):
    WPSProcess.__init__(self, identifier = 't.rast.accumulate', title = 'Compute cyclic accumulations of a space time raster dataset', version = 1, statusSupported = True, storeSupported = True, metadata = [{'type': 'simple', 'title': 'temporal'}, {'type': 'simple', 'title': 'accumulation'}], abstract = 'http://grass.osgeo.org/grass70/manuals/html70_user/t.rast.accumulate.html')

    # Literal and complex inputs
    self.addComplexInput(identifier = 'input', title = 'Name of the input space time raster dataset', minOccurs = 1, maxOccurs = 1, formats = [{'mimeType': 'application/x-grass-strds-tar'}, {'mimeType': 'application/x-grass-strds-tar-gz'}, {'mimeType': 'application/x-grass-strds-tar-bzip'}])
    self.addComplexInput(identifier = 'lower', title = 'Input space time raster dataset that defines the lower threshold, values lower this threshold are excluded from accumulation', minOccurs = 0, maxOccurs = 1, formats = [{'mimeType': 'application/x-grass-strds-tar'}, {'mimeType': 'application/x-grass-strds-tar-gz'}, {'mimeType': 'application/x-grass-strds-tar-bzip'}])
    self.addComplexInput(identifier = 'upper', title = 'Input space time raster dataset that defines the upper threshold, values upper this threshold are excluded from accumulation', minOccurs = 0, maxOccurs = 1, formats = [{'mimeType': 'application/x-grass-strds-tar'}, {'mimeType': 'application/x-grass-strds-tar-gz'}, {'mimeType': 'application/x-grass-strds-tar-bzip'}])
    self.addLiteralInput(identifier = 'start', title = 'The temporal starting point to begin the accumulation, eg 2001-01-01', minOccurs = 1, maxOccurs = 1, type = type("string"), allowedValues = '*')
    self.addLiteralInput(identifier = 'stop', title = 'The temporal date to stop the accumulation, eg 2009-01-01', minOccurs = 0, maxOccurs = 1, type = type("string"), allowedValues = '*')
    self.addLiteralInput(identifier = 'cycle', title = 'The temporal cycle to restart the accumulation, eg 12 months', minOccurs = 1, maxOccurs = 1, type = type("string"), allowedValues = '*')
    self.addLiteralInput(identifier = 'offset', title = 'The temporal offset to the begin of the next cycle, eg 6 months', minOccurs = 0, maxOccurs = 1, type = type("string"), allowedValues = '*')
    self.addLiteralInput(identifier = 'granularity', title = 'The granularity for accumulation 1 day', minOccurs = 0, maxOccurs = 1, type = type("string"), default = "1 day")
    self.addLiteralInput(identifier = 'basename', title = 'Base name of the new generated output maps"', abstract = 'A numerical suffix separated by an underscore will be attached to create a unique identifier', minOccurs = 1, maxOccurs = 1, type = type("string"), allowedValues = '*')
    self.addLiteralInput(identifier = 'limits', title = 'Use these limits in case lower and/or upper input  space time raster datasets are not defined', minOccurs = 0, maxOccurs = 2, type = type(0.0), allowedValues = '*')
    self.addLiteralInput(identifier = 'shift', title = 'Scale factor for input space time raster dataset', minOccurs = 0, maxOccurs = 1, type = type(0.0), allowedValues = '*')
    self.addLiteralInput(identifier = 'scale', title = 'Shift factor for input space time raster dataset', minOccurs = 0, maxOccurs = 1, type = type(0.0), allowedValues = '*')
    self.addLiteralInput(identifier = 'method', title = 'This method will be applied to compute the accumulative values from the input maps', minOccurs = 0, maxOccurs = 1, type = type("string"), default = "mean", allowedValues = ['mean', 'gdd', 'bedd', 'huglin'])
    self.addLiteralInput(identifier = '-n', title = 'Register empty maps in the output space time raster dataset, otherwise they will be deleted', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])
    self.addLiteralInput(identifier = '-r', title = 'Reverse time direction in cyclic accumulation', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])
    self.addLiteralInput(identifier = 'grass_resolution_ns', title = 'Resolution of the mapset in north-south direction in meters or degrees', abstract = 'This parameter defines the north-south resolution of the mapset in meter or degrees, which should be used to process the input and output raster data. To enable this setting, you need to specify north-south and east-west resolution.', minOccurs = 0, maxOccurs = 1, type = type(0.0), allowedValues = '*')
    self.addLiteralInput(identifier = 'grass_resolution_ew', title = 'Resolution of the mapset in east-west direction in meters or degrees', abstract = 'This parameter defines the east-west resolution of the mapset in meters or degrees, which should be used to process the input and output raster data.  To enable this setting, you need to specify north-south and east-west resolution.', minOccurs = 0, maxOccurs = 1, type = type(0.0), allowedValues = '*')

    # complex outputs
    self.addComplexOutput(identifier = 'output', title = 'Name of the output space time raster dataset', formats = [{'mimeType': 'application/x-grass-strds-tar'}, {'mimeType': 'application/x-grass-strds-tar-gz'}, {'mimeType': 'application/x-grass-strds-tar-bzip'}])

  def execute(self):
    starter = PyWPSGrassModuleStarter()
    starter.fromPyWPS("t.rast.accumulate", self.inputs, self.outputs, self.pywps)

if __name__ == "__main__":
  process = t_rast_accumulate()
  process.execute()
