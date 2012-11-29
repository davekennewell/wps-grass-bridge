# ################################################ #
# This process was generated using GrassXMLtoPyWPS #
# Author: Soeren Gebbert                           #
# Mail: soerengebbert <at> googlemail <dot> com    #
# ################################################ #

from pywps.Process import WPSProcess

from PyWPSGrassModuleStarter import PyWPSGrassModuleStarter

class t_vect_list(WPSProcess):

  def __init__(self):
    WPSProcess.__init__(self, identifier = 't.vect.list', title = 'Lists registered maps of a space time vector dataset.', version = 1, statusSupported = True, storeSupported = True, metadata = [{'type': 'simple', 'title': 'temporal'}, {'type': 'simple', 'title': 'map management'}, {'type': 'simple', 'title': 'list'}], abstract = 'http://grass.osgeo.org/grass70/manuals/html70_user/t.vect.list.html')

    # Literal and complex inputs
    self.addComplexInput(identifier = 'input', title = 'Name of the input space time vector dataset', minOccurs = 1, maxOccurs = 1, formats = [{'mimeType': 'application/x-grass-stvds-tar'}, {'mimeType': 'application/x-grass-stvds-tar-gz'}, {'mimeType': 'application/x-grass-stvds-tar-bzip'}])
    self.addLiteralInput(identifier = 'order', title = 'Order the space time dataset by category', minOccurs = 0, maxOccurs = 1024, type = type("string"), default = "start_time", allowedValues = ['id', 'name', 'layer', 'creator', 'mapset', 'temporal_type', 'creation_time', 'start_time', 'end_time', 'north', 'south', 'west', 'east', 'points', 'lines', 'boundaries', 'centroids', 'faces', 'kernels', 'primitives', 'nodes', 'areas', 'islands', 'holes', 'volumes'])
    self.addLiteralInput(identifier = 'columns', title = 'Select columns to be printed to stdout', minOccurs = 0, maxOccurs = 1024, type = type("string"), default = "id,name,layer,mapset,start_time,end_time", allowedValues = ['id', 'name', 'layer', 'creator', 'mapset', 'temporal_type', 'creation_time', 'start_time', 'end_time', 'north', 'south', 'west', 'east', 'points', 'lines', 'boundaries', 'centroids', 'faces', 'kernels', 'primitives', 'nodes', 'areas', 'islands', 'holes', 'volumes'])
    self.addLiteralInput(identifier = 'where', title = 'Example: start_time &#62; 2001-01-01 12:30:00', minOccurs = 0, maxOccurs = 1, type = type("string"), allowedValues = '*')
    self.addLiteralInput(identifier = 'method', title = 'Method used for data listing', minOccurs = 0, maxOccurs = 1, type = type("string"), default = "cols", allowedValues = ['cols', 'comma', 'delta', 'deltagaps', 'gran'])
    self.addLiteralInput(identifier = 'fs', title = 'Field separator character between the columns, default is tabular "\t"', minOccurs = 0, maxOccurs = 1, type = type("string"), allowedValues = '*')
    self.addLiteralInput(identifier = '-h', title = 'Print column names', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])

    # complex outputs
    self.addComplexOutput(identifier = 'stdout', title = 'Module output on stdout', abstract = 'The output of the module written to stdout', formats = [{'mimeType': 'text/plain'}])

  def execute(self):
    starter = PyWPSGrassModuleStarter()
    starter.fromPyWPS("t.vect.list", self.inputs, self.outputs, self.pywps)

if __name__ == "__main__":
  process = t_vect_list()
  process.execute()
