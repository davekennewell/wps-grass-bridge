# ################################################ #
# This process was generated using GrassXMLtoPyWPS #
# Author: Soeren Gebbert                           #
# Mail: soerengebbert <at> googlemail <dot> com    #
# ################################################ #

from pywps.Process import WPSProcess

from PyWPSGrassModuleStarter import PyWPSGrassModuleStarter

class v_normal(WPSProcess):

  def __init__(self):
    WPSProcess.__init__(self, identifier = 'v.normal', title = 'Tests for normality for vector points.', version = 1, statusSupported = True, storeSupported = True, metadata = [{'type': 'simple', 'title': 'vector'}, {'type': 'simple', 'title': 'statistics'}, {'type': 'simple', 'title': 'points'}], abstract = 'http://grass.osgeo.org/grass70/manuals/html70_user/v.normal.html')

    # Literal and complex inputs
    self.addComplexInput(identifier = 'map', title = 'Data source for direct OGR access', minOccurs = 1, maxOccurs = 1, formats = [{'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/kml/2.2.0/ogckml22.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/dgn', 'schema': 'None', 'encoding': 'None'}, {'mimeType': 'application/shp', 'schema': 'None', 'encoding': 'None'}, {'mimeType': 'application/x-zipped-shp', 'schema': 'None', 'encoding': 'None'}])
    self.addLiteralInput(identifier = 'layer', title = 'A single vector map can be connected to multiple database tables. This number determines which table to use. Layer name for direct OGR access.', minOccurs = 1, maxOccurs = 1, type = type("string"), default = "1")
    self.addLiteralInput(identifier = 'tests', title = 'E.g. 1,3-8,13', minOccurs = 1, maxOccurs = 1024, type = type("string"), allowedValues = '*')
    self.addLiteralInput(identifier = 'column', title = 'Name of attribute column', minOccurs = 1, maxOccurs = 1, type = type("string"), allowedValues = '*')
    self.addLiteralInput(identifier = '-r', title = 'Use only points in current region', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])
    self.addLiteralInput(identifier = '-l', title = 'Lognormality instead of normality', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])

    # complex outputs
    self.addComplexOutput(identifier = 'stdout', title = 'Module output on stdout', abstract = 'The output of the module written to stdout', formats = [{'mimeType': 'text/plain'}])

  def execute(self):
    starter = PyWPSGrassModuleStarter()
    starter.fromPyWPS("v.normal", self.inputs, self.outputs, self.pywps)

if __name__ == "__main__":
  process = v_normal()
  process.execute()
