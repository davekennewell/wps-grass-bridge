# ################################################ #
# This process was generated using GrassXMLtoPyWPS #
# Author: Soeren Gebbert                           #
# Mail: soerengebbert <at> googlemail <dot> com    #
# ################################################ #

from pywps.Process import WPSProcess

from PyWPSGrassModuleStarter import PyWPSGrassModuleStarter

class v_net_centrality(WPSProcess):

  def __init__(self):
    WPSProcess.__init__(self, identifier = 'v.net.centrality', title = 'Computes degree, centrality, betweeness, closeness and eigenvector centrality measures in the network.', version = 1, statusSupported = True, storeSupported = True, metadata = [{'type': 'simple', 'title': 'vector'}, {'type': 'simple', 'title': 'network'}, {'type': 'simple', 'title': 'centrality measures'}], abstract = 'http://grass.osgeo.org/grass70/manuals/html70_user/v.net.centrality.html')

    # Literal and complex inputs
    self.addComplexInput(identifier = 'input', title = 'Data source for direct OGR access', minOccurs = 1, maxOccurs = 1, formats = [{'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/kml/2.2.0/ogckml22.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/dgn', 'schema': 'None', 'encoding': 'None'}, {'mimeType': 'application/shp', 'schema': 'None', 'encoding': 'None'}, {'mimeType': 'application/x-zipped-shp', 'schema': 'None', 'encoding': 'None'}])
    self.addLiteralInput(identifier = 'layer', title = 'A single vector map can be connected to multiple database tables. This number determines which table to use. Layer name for direct OGR access.', minOccurs = 1, maxOccurs = 1, type = type("string"), default = "1")
    self.addLiteralInput(identifier = 'cats', title = 'Example: 1,3,7-9,13', minOccurs = 0, maxOccurs = 1, type = type("string"), allowedValues = '*')
    self.addLiteralInput(identifier = 'where', title = 'Example: income &#60; 1000 and inhab &#62;= 10000', minOccurs = 0, maxOccurs = 1, type = type("string"), allowedValues = '*')
    self.addLiteralInput(identifier = 'afcolumn', title = 'Name of arc forward/both direction(s) cost column', minOccurs = 0, maxOccurs = 1, type = type("string"), allowedValues = '*')
    self.addLiteralInput(identifier = 'abcolumn', title = 'Name of arc backward direction cost column', minOccurs = 0, maxOccurs = 1, type = type("string"), allowedValues = '*')
    self.addLiteralInput(identifier = 'degree', title = 'Name of degree centrality column', minOccurs = 0, maxOccurs = 1, type = type("string"), allowedValues = '*')
    self.addLiteralInput(identifier = 'closeness', title = 'Name of closeness centrality column', minOccurs = 0, maxOccurs = 1, type = type("string"), allowedValues = '*')
    self.addLiteralInput(identifier = 'betweenness', title = 'Name of betweenness centrality column', minOccurs = 0, maxOccurs = 1, type = type("string"), allowedValues = '*')
    self.addLiteralInput(identifier = 'eigenvector', title = 'Name of eigenvector centrality column', minOccurs = 0, maxOccurs = 1, type = type("string"), allowedValues = '*')
    self.addLiteralInput(identifier = 'iterations', title = 'Maximum number of iterations to compute eigenvector centrality', minOccurs = 0, maxOccurs = 1, type = type(0), default = 1000)
    self.addLiteralInput(identifier = 'error', title = 'Cummulative error tolerance for eigenvector centrality', minOccurs = 0, maxOccurs = 1, type = type(0.0), default = 0.1)
    self.addLiteralInput(identifier = '-g', title = 'Use geodesic calculation for longitude-latitude locations', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])
    self.addLiteralInput(identifier = '-a', title = 'Add points on nodes', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])

    # complex outputs
    self.addComplexOutput(identifier = 'output', title = 'Name for output vector map', formats = [{'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/kml/2.2.0/ogckml22.xsd', 'encoding': 'UTF-8'}])

  def execute(self):
    starter = PyWPSGrassModuleStarter()
    starter.fromPyWPS("v.net.centrality", self.inputs, self.outputs, self.pywps)

if __name__ == "__main__":
  process = v_net_centrality()
  process.execute()
