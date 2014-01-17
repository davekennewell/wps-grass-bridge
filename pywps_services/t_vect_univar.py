# ################################################ #
# This process was generated using GrassXMLtoPyWPS #
# Author: Soeren Gebbert                           #
# Mail: soerengebbert <at> googlemail <dot> com    #
# ################################################ #

from pywps.Process import WPSProcess

from PyWPSGrassModuleStarter import PyWPSGrassModuleStarter

class t_vect_univar(WPSProcess):

  def __init__(self):
    WPSProcess.__init__(self, identifier = 't.vect.univar', title = 'Calculates univariate statistics of attributes for each registered vector map of a space time vector dataset', version = 1, statusSupported = True, storeSupported = True, metadata = [{'type': 'simple', 'title': 'temporal'}, {'type': 'simple', 'title': 'statistics'}, {'type': 'simple', 'title': 'vector'}], abstract = 'http://grass.osgeo.org/grass70/manuals/html70_user/t.vect.univar.html')

    # Literal and complex inputs
    self.addComplexInput(identifier = 'input', title = 'Name of the input space time vector dataset', minOccurs = 1, maxOccurs = 1, formats = [{'mimeType': 'application/x-grass-stvds-tar'}, {'mimeType': 'application/x-grass-stvds-tar-gz'}, {'mimeType': 'application/x-grass-stvds-tar-bzip'}])
    self.addLiteralInput(identifier = 'layer', title = 'Vector features can have category values in different layers. This number determines which layer to use. When used with direct OGR access this is the layer name.', minOccurs = 0, maxOccurs = 1, type = type("string"), default = "1")
    self.addLiteralInput(identifier = 'column', title = 'Name of attribute column', minOccurs = 1, maxOccurs = 1, type = type("string"), allowedValues = '*')
    self.addLiteralInput(identifier = 'twhere', title = 'Example: start_time &#62; 2001-01-01 12:30:00', minOccurs = 0, maxOccurs = 1, type = type("string"), allowedValues = '*')
    self.addLiteralInput(identifier = 'where', title = 'Example: income &#60; 1000 and inhab &#62;= 10000', minOccurs = 0, maxOccurs = 1, type = type("string"), allowedValues = '*')
    self.addLiteralInput(identifier = 'type', title = 'Feature type', minOccurs = 0, maxOccurs = 1, type = type("string"), default = "point", allowedValues = ['point', 'line', 'boundary', 'centroid', 'area'])
    self.addLiteralInput(identifier = 'separator', title = 'Separator character between the output columns', minOccurs = 0, maxOccurs = 1, type = type("string"), default = "|")
    self.addLiteralInput(identifier = '-e', title = 'Calculate extended statistics', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])
    self.addLiteralInput(identifier = '-h', title = 'Print column names', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])

    # complex outputs
    self.addComplexOutput(identifier = 'stdout', title = 'Module output on stdout', abstract = 'The output of the module written to stdout', formats = [{'mimeType': 'text/plain'}])

  def execute(self):
    starter = PyWPSGrassModuleStarter()
    starter.fromPyWPS("t.vect.univar", self.inputs, self.outputs, self.pywps)

if __name__ == "__main__":
  process = t_vect_univar()
  process.execute()
