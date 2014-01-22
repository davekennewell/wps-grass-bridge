# ################################################ #
# This process was generated using GrassXMLtoPyWPS #
# Author: Soeren Gebbert                           #
# Mail: soerengebbert <at> googlemail <dot> com    #
# ################################################ #

from pywps.Process import WPSProcess

from PyWPSGrassModuleStarter import PyWPSGrassModuleStarter

class t_rast_list(WPSProcess):

  def __init__(self):
    WPSProcess.__init__(self, identifier = 't.rast.list', title = 'Lists registered maps of a space time raster dataset.', version = 1, statusSupported = True, storeSupported = True, metadata = [{'type': 'simple', 'title': 'temporal'}, {'type': 'simple', 'title': 'map management'}, {'type': 'simple', 'title': 'raster'}, {'type': 'simple', 'title': 'list'}], abstract = 'http://grass.osgeo.org/grass70/manuals/html70_user/t.rast.list.html')

    # Literal and complex inputs
    self.addComplexInput(identifier = 'input', title = 'Name of the input space time raster dataset', minOccurs = 1, maxOccurs = 1, formats = [{'mimeType': 'application/x-grass-strds-tar'}, {'mimeType': 'application/x-grass-strds-tar-gz'}, {'mimeType': 'application/x-grass-strds-tar-bzip'}])
    self.addLiteralInput(identifier = 'order', title = 'Order the space time dataset by category', minOccurs = 0, maxOccurs = 1024, type = type("string"), default = "start_time", allowedValues = ['id', 'name', 'creator', 'mapset', 'temporal_type', 'creation_time', 'start_time', 'end_time', 'north', 'south', 'west', 'east', 'nsres', 'ewres', 'cols', 'rows', 'number_of_cells', 'min', 'max'])
    self.addLiteralInput(identifier = 'columns', title = 'Select columns to be printed to stdout', minOccurs = 0, maxOccurs = 1024, type = type("string"), default = "name,mapset,start_time,end_time", allowedValues = ['id', 'name', 'creator', 'mapset', 'temporal_type', 'creation_time', 'start_time', 'end_time', 'north', 'south', 'west', 'east', 'nsres', 'ewres', 'cols', 'rows', 'number_of_cells', 'min', 'max'])
    self.addLiteralInput(identifier = 'where', title = 'WHERE conditions of SQL statement without where keyword used in the temporal GIS framework', abstract = 'Example: start_time &#62; 2001-01-01 12:30:00', minOccurs = 0, maxOccurs = 1, type = type("string"), allowedValues = '*')
    self.addLiteralInput(identifier = 'method', title = 'Method used for data listing', minOccurs = 0, maxOccurs = 1, type = type("string"), default = "cols", allowedValues = ['cols', 'comma', 'delta', 'deltagaps', 'gran'])
    self.addLiteralInput(identifier = 'granule', title = 'The granule to be used for listing. The granule must be specified as string eg.: absolute time "1 months" or relative time "1"', minOccurs = 0, maxOccurs = 1, type = type("string"), allowedValues = '*')
    self.addLiteralInput(identifier = 'separator', title = 'Separator character between the columns, default is tabular "\t"', minOccurs = 0, maxOccurs = 1, type = type("string"), allowedValues = '*')
    self.addLiteralInput(identifier = '-h', title = 'Print column names', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])
    self.addLiteralInput(identifier = 'grass_resolution_ns', title = 'Resolution of the mapset in north-south direction in meters or degrees', abstract = 'This parameter defines the north-south resolution of the mapset in meter or degrees, which should be used to process the input and output raster data. To enable this setting, you need to specify north-south and east-west resolution.', minOccurs = 0, maxOccurs = 1, type = type(0.0), allowedValues = '*')
    self.addLiteralInput(identifier = 'grass_resolution_ew', title = 'Resolution of the mapset in east-west direction in meters or degrees', abstract = 'This parameter defines the east-west resolution of the mapset in meters or degrees, which should be used to process the input and output raster data.  To enable this setting, you need to specify north-south and east-west resolution.', minOccurs = 0, maxOccurs = 1, type = type(0.0), allowedValues = '*')

    # complex outputs
    self.addComplexOutput(identifier = 'stdout', title = 'Module output on stdout', abstract = 'The output of the module written to stdout', formats = [{'mimeType': 'text/plain'}])

  def execute(self):
    starter = PyWPSGrassModuleStarter()
    starter.fromPyWPS("t.rast.list", self.inputs, self.outputs, self.pywps)

if __name__ == "__main__":
  process = t_rast_list()
  process.execute()
