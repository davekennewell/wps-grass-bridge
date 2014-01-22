# ################################################ #
# This process was generated using GrassXMLtoPyWPS #
# Author: Soeren Gebbert                           #
# Mail: soerengebbert <at> googlemail <dot> com    #
# ################################################ #

from pywps.Process import WPSProcess

from PyWPSGrassModuleStarter import PyWPSGrassModuleStarter

class t_rast_accdetect(WPSProcess):

  def __init__(self):
    WPSProcess.__init__(self, identifier = 't.rast.accdetect', title = 'Detect accumulation pattern in temporally accumulated space time raster datasets created by t.rast.accumulate.', version = 1, statusSupported = True, storeSupported = True, metadata = [{'type': 'simple', 'title': 'temporal'}, {'type': 'simple', 'title': 'accumulation'}], abstract = 'http://grass.osgeo.org/grass70/manuals/html70_user/t.rast.accdetect.html')

    # Literal and complex inputs
    self.addComplexInput(identifier = 'input', title = 'Name of the input space time raster dataset', minOccurs = 1, maxOccurs = 1, formats = [{'mimeType': 'application/x-grass-strds-tar'}, {'mimeType': 'application/x-grass-strds-tar-gz'}, {'mimeType': 'application/x-grass-strds-tar-bzip'}])
    self.addComplexInput(identifier = 'minimum', title = 'Input space time raster dataset that specifies the minimum values to detect the accumulation pattern', minOccurs = 0, maxOccurs = 1, formats = [{'mimeType': 'application/x-grass-strds-tar'}, {'mimeType': 'application/x-grass-strds-tar-gz'}, {'mimeType': 'application/x-grass-strds-tar-bzip'}])
    self.addComplexInput(identifier = 'maximum', title = 'Input space time raster dataset that specifies the maximum values to detect the accumulation pattern', minOccurs = 0, maxOccurs = 1, formats = [{'mimeType': 'application/x-grass-strds-tar'}, {'mimeType': 'application/x-grass-strds-tar-gz'}, {'mimeType': 'application/x-grass-strds-tar-bzip'}])
    self.addLiteralInput(identifier = 'start', title = 'The temporal starting point to begin the accumulation, eg 2001-01-01', minOccurs = 1, maxOccurs = 1, type = type("string"), allowedValues = '*')
    self.addLiteralInput(identifier = 'stop', title = 'The temporal date to stop the accumulation, eg 2009-01-01', minOccurs = 0, maxOccurs = 1, type = type("string"), allowedValues = '*')
    self.addLiteralInput(identifier = 'cycle', title = 'The temporal cycle to restart the accumulation, eg 12 months', minOccurs = 1, maxOccurs = 1, type = type("string"), allowedValues = '*')
    self.addLiteralInput(identifier = 'offset', title = 'The temporal offset to the begin of the next cycle, eg 6 months', minOccurs = 0, maxOccurs = 1, type = type("string"), allowedValues = '*')
    self.addLiteralInput(identifier = 'basename', title = 'Base name of the new generated output maps"', abstract = 'A numerical suffix separated by an underscore will be attached to create a unique identifier', minOccurs = 1, maxOccurs = 1, type = type("string"), allowedValues = '*')
    self.addLiteralInput(identifier = 'range', title = 'The minimum and maximum value of the occurrence of accumulated values, these values will be used if the min/max space time raster datasets are not specified', minOccurs = 0, maxOccurs = 2, type = type(0.0), allowedValues = '*')
    self.addLiteralInput(identifier = 'staend', title = 'The user defined values that indicate start, intermediate and end status in the indicator output space time raster dataset', minOccurs = 0, maxOccurs = 3, type = type(0), default = 1,2,3)
    self.addLiteralInput(identifier = '-n', title = 'Register empty maps in the output space time raster datasets, otherwise they will be deleted', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])
    self.addLiteralInput(identifier = '-r', title = 'Reverse time direction in cyclic accumulation', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])
    self.addLiteralInput(identifier = 'grass_resolution_ns', title = 'Resolution of the mapset in north-south direction in meters or degrees', abstract = 'This parameter defines the north-south resolution of the mapset in meter or degrees, which should be used to process the input and output raster data. To enable this setting, you need to specify north-south and east-west resolution.', minOccurs = 0, maxOccurs = 1, type = type(0.0), allowedValues = '*')
    self.addLiteralInput(identifier = 'grass_resolution_ew', title = 'Resolution of the mapset in east-west direction in meters or degrees', abstract = 'This parameter defines the east-west resolution of the mapset in meters or degrees, which should be used to process the input and output raster data.  To enable this setting, you need to specify north-south and east-west resolution.', minOccurs = 0, maxOccurs = 1, type = type(0.0), allowedValues = '*')

    # complex outputs
    self.addComplexOutput(identifier = 'occurrence', title = 'The output space time raster dataset that stores the occurrence of the the accumulation pattern using the provided data range', formats = [{'mimeType': 'application/x-grass-strds-tar'}, {'mimeType': 'application/x-grass-strds-tar-gz'}, {'mimeType': 'application/x-grass-strds-tar-bzip'}])

    self.addComplexOutput(identifier = 'indicator', title = 'The output space time raster dataset that stores the indication of the start, intermediate and end of the specified data range', formats = [{'mimeType': 'application/x-grass-strds-tar'}, {'mimeType': 'application/x-grass-strds-tar-gz'}, {'mimeType': 'application/x-grass-strds-tar-bzip'}])

  def execute(self):
    starter = PyWPSGrassModuleStarter()
    starter.fromPyWPS("t.rast.accdetect", self.inputs, self.outputs, self.pywps)

if __name__ == "__main__":
  process = t_rast_accdetect()
  process.execute()
