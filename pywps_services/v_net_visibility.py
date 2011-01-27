# ################################################ #
# This process was generated using GrassXMLtoPyWPS #
# Author: Soeren Gebbert                           #
# Mail: soerengebbert <at> googlemail <dot> com    #
# ################################################ #

from pywps.Process import WPSProcess

from PyWPSGrassModuleStarter import PyWPSGrassModuleStarter

class v_net_visibility(WPSProcess):

  def __init__(self):
    WPSProcess.__init__(self, identifier = 'v.net.visibility', title = 'Visibility graph construction.', version = 1, statusSupported = True, storeSupported = True, metadata = [{'type': 'simple', 'title': 'vector'}, {'type': 'simple', 'title': 'path'}, {'type': 'simple', 'title': 'visibility'}], abstract = 'http://grass.osgeo.org/grass70/manuals/html70_user/v.net.visibility.html')

    # Literal and complex inputs
    self.addComplexInput(identifier = 'input', title = 'Data source for OGR access', minOccurs = 1, maxOccurs = 1, formats = [{'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/kml/2.2.0/ogckml22.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/dgn', 'schema': 'None', 'encoding': 'None'}, {'mimeType': 'application/shp', 'schema': 'None', 'encoding': 'None'}, {'mimeType': 'application/x-zipped-shp', 'schema': 'None', 'encoding': 'None'}])
    self.addLiteralInput(identifier = 'coordinate', title = 'One or more coordinates', minOccurs = 0, maxOccurs = 1024, type = type("string"), allowedValues = '*')
    self.addLiteralInput(identifier = 'vis', title = 'Add points after computing the vis graph', minOccurs = 0, maxOccurs = 1, type = type("string"), allowedValues = '*')

    # complex outputs
    self.addComplexOutput(identifier = 'output', title = 'Name for output vector map', formats = [{'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/kml/2.2.0/ogckml22.xsd', 'encoding': 'UTF-8'}])

  def execute(self):
    starter = PyWPSGrassModuleStarter()
    starter.fromPyWPS("v.net.visibility", self.inputs, self.outputs, self.pywps)

if __name__ == "__main__":
  process = v_net_visibility()
  process.execute()
