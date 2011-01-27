# ################################################ #
# This process was generated using GrassXMLtoPyWPS #
# Author: Soeren Gebbert                           #
# Mail: soerengebbert <at> googlemail <dot> com    #
# ################################################ #

from pywps.Process import WPSProcess

from PyWPSGrassModuleStarter import PyWPSGrassModuleStarter

class v_net_salesman(WPSProcess):

  def __init__(self):
    WPSProcess.__init__(self, identifier = 'v.net.salesman', title = 'Note that TSP is NP-hard, heuristic algorithm is used by this module and created cycle may be sub optimal', version = 1, statusSupported = True, storeSupported = True, metadata = [{'type': 'simple', 'title': 'vector'}, {'type': 'simple', 'title': 'networking'}], abstract = 'http://grass.osgeo.org/grass70/manuals/html70_user/v.net.salesman.html')

    # Literal and complex inputs
    self.addComplexInput(identifier = 'input', title = 'Data source for OGR access', minOccurs = 1, maxOccurs = 1, formats = [{'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/kml/2.2.0/ogckml22.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/dgn', 'schema': 'None', 'encoding': 'None'}, {'mimeType': 'application/shp', 'schema': 'None', 'encoding': 'None'}, {'mimeType': 'application/x-zipped-shp', 'schema': 'None', 'encoding': 'None'}])
    self.addLiteralInput(identifier = 'type', title = 'Arc type', minOccurs = 0, maxOccurs = 1024, type = type("string"), default = "line,boundary", allowedValues = ['line', 'boundary'])
    self.addLiteralInput(identifier = 'alayer', title = 'Arc layer', minOccurs = 1, maxOccurs = 1, type = type("string"), default = "1")
    self.addLiteralInput(identifier = 'nlayer', title = 'Node layer (used for cities)', minOccurs = 1, maxOccurs = 1, type = type("string"), default = "2")
    self.addLiteralInput(identifier = 'acolumn', title = 'Arcs cost column (for both directions)', minOccurs = 0, maxOccurs = 1, type = type("string"), allowedValues = '*')
    self.addLiteralInput(identifier = 'ccats', title = 'Categories of points (cities) on nodes (layer is specified by nlayer)', minOccurs = 1, maxOccurs = 1, type = type("string"), allowedValues = '*')
    self.addLiteralInput(identifier = '-g', title = 'Use geodesic calculation for longitude-latitude locations', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])

    # complex outputs
    self.addComplexOutput(identifier = 'output', title = 'Name for output vector map', formats = [{'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/kml/2.2.0/ogckml22.xsd', 'encoding': 'UTF-8'}])

  def execute(self):
    starter = PyWPSGrassModuleStarter()
    starter.fromPyWPS("v.net.salesman", self.inputs, self.outputs, self.pywps)

if __name__ == "__main__":
  process = v_net_salesman()
  process.execute()
