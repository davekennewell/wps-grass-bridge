# ################################################ #
# This process was generated using GrassXMLtoPyWPS #
# Author: Soeren Gebbert                           #
# Mail: soerengebbert <at> googlemail <dot> com    #
# ################################################ #

from pywps.Process import WPSProcess

from PyWPSGrassModuleStarter import PyWPSGrassModuleStarter

class v_net_distance(WPSProcess):

  def __init__(self):
    WPSProcess.__init__(self, identifier = 'v.net.distance', title = 'Finds the shortest paths from each from point to the nearest to feature and various information about this relation are uploaded to the attribute table.', version = 1, statusSupported = True, storeSupported = True, metadata = [{'type': 'simple', 'title': 'vector'}, {'type': 'simple', 'title': 'network'}, {'type': 'simple', 'title': 'shortest path'}], abstract = 'http://grass.osgeo.org/grass70/manuals/html70_user/v.net.distance.html')

    # Literal and complex inputs
    self.addComplexInput(identifier = 'input', title = 'Or data source for direct OGR access', minOccurs = 1, maxOccurs = 1, formats = [{'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/3.1.1/base/gml.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/xml', 'schema': 'http://schemas.opengis.net/gml/3.1.1/base/gml.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/kml/2.2.0/ogckml22.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/dgn', 'schema': 'None', 'encoding': 'None'}, {'mimeType': 'application/shp', 'schema': 'None', 'encoding': 'None'}, {'mimeType': 'application/x-zipped-shp', 'schema': 'None', 'encoding': 'None'}])
    self.addLiteralInput(identifier = 'alayer', title = 'Vector features can have category values in different layers. This number determines which layer to use. When used with direct OGR access this is the layer name.', minOccurs = 0, maxOccurs = 1, type = type("string"), default = "1")
    self.addLiteralInput(identifier = 'type', title = 'Feature type', minOccurs = 0, maxOccurs = 1024, type = type("string"), default = "line,boundary", allowedValues = ['line', 'boundary'])
    self.addLiteralInput(identifier = 'nlayer', title = 'Vector features can have category values in different layers. This number determines which layer to use. When used with direct OGR access this is the layer name.', minOccurs = 0, maxOccurs = 1, type = type("string"), default = "2")
    self.addLiteralInput(identifier = 'from_layer', title = 'Vector features can have category values in different layers. This number determines which layer to use. When used with direct OGR access this is the layer name.', minOccurs = 0, maxOccurs = 1, type = type("string"), default = "1")
    self.addLiteralInput(identifier = 'from_cats', title = 'Example: 1,3,7-9,13', minOccurs = 0, maxOccurs = 1, type = type("string"), allowedValues = '*')
    self.addLiteralInput(identifier = 'from_where', title = 'Example: income &#60; 1000 and inhab &#62;= 10000', minOccurs = 0, maxOccurs = 1, type = type("string"), allowedValues = '*')
    self.addLiteralInput(identifier = 'to_layer', title = 'To layer number or name', minOccurs = 0, maxOccurs = 1, type = type("string"), default = "1")
    self.addLiteralInput(identifier = 'to_type', title = 'To feature type', minOccurs = 0, maxOccurs = 1024, type = type("string"), default = "point", allowedValues = ['point', 'line', 'boundary'])
    self.addLiteralInput(identifier = 'to_cats', title = 'Example: 1,3,7-9,13', minOccurs = 0, maxOccurs = 1, type = type("string"), allowedValues = '*')
    self.addLiteralInput(identifier = 'to_where', title = 'Example: income &#60; 1000 and inhab &#62;= 10000', minOccurs = 0, maxOccurs = 1, type = type("string"), allowedValues = '*')
    self.addLiteralInput(identifier = 'afcolumn', title = 'Arc forward/both direction(s) cost column (number)', minOccurs = 0, maxOccurs = 1, type = type("string"), allowedValues = '*')
    self.addLiteralInput(identifier = 'abcolumn', title = 'Arc backward direction cost column (number)', minOccurs = 0, maxOccurs = 1, type = type("string"), allowedValues = '*')
    self.addLiteralInput(identifier = 'ncolumn', title = 'Node cost column (number)', minOccurs = 0, maxOccurs = 1, type = type("string"), allowedValues = '*')
    self.addLiteralInput(identifier = '-g', title = 'Use geodesic calculation for longitude-latitude locations', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])

    # complex outputs
    self.addComplexOutput(identifier = 'output', title = 'Name for output vector map', formats = [{'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/3.1.1/base/gml.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/xml', 'schema': 'http://schemas.opengis.net/gml/3.1.1/base/gml.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/kml/2.2.0/ogckml22.xsd', 'encoding': 'UTF-8'}])

  def execute(self):
    starter = PyWPSGrassModuleStarter()
    starter.fromPyWPS("v.net.distance", self.inputs, self.outputs, self.pywps)

if __name__ == "__main__":
  process = v_net_distance()
  process.execute()
