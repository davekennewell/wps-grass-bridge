# ################################################ #
# This process was generated using GrassXMLtoPyWPS #
# Author: Soeren Gebbert                           #
# Mail: soerengebbert <at> googlemail <dot> com    #
# ################################################ #

from pywps.Process import WPSProcess

from PyWPSGrassModuleStarter import PyWPSGrassModuleStarter

class v_buffer(WPSProcess):

  def __init__(self):
    WPSProcess.__init__(self, identifier = 'v.buffer', title = 'Creates a buffer around vector features of given type.', version = 1, statusSupported = True, storeSupported = True, metadata = [{'type': 'simple', 'title': 'vector'}, {'type': 'simple', 'title': 'buffer'}, {'type': 'simple', 'title': 'geometry'}], abstract = 'http://grass.osgeo.org/grass70/manuals/html70_user/v.buffer.html')

    # Literal and complex inputs
    self.addComplexInput(identifier = 'input', title = 'Or data source for direct OGR access', minOccurs = 1, maxOccurs = 1, formats = [{'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/3.1.1/base/gml.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/xml', 'schema': 'http://schemas.opengis.net/gml/3.1.1/base/gml.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/kml/2.2.0/ogckml22.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/dgn', 'schema': 'None', 'encoding': 'None'}, {'mimeType': 'application/shp', 'schema': 'None', 'encoding': 'None'}, {'mimeType': 'application/x-zipped-shp', 'schema': 'None', 'encoding': 'None'}])
    self.addLiteralInput(identifier = 'layer', title = 'A single vector map can be connected to multiple database tables. This number determines which table to use. When used with direct OGR access this is the layer name.', minOccurs = 1, maxOccurs = 1, type = type("string"), default = "-1")
    self.addLiteralInput(identifier = 'cats', title = 'Example: 1,3,7-9,13', minOccurs = 0, maxOccurs = 1, type = type("string"), allowedValues = '*')
    self.addLiteralInput(identifier = 'where', title = 'Example: income &#60; 1000 and inhab &#62;= 10000', minOccurs = 0, maxOccurs = 1, type = type("string"), allowedValues = '*')
    self.addLiteralInput(identifier = 'type', title = 'Feature type', minOccurs = 0, maxOccurs = 1024, type = type("string"), default = "point,line,area", allowedValues = ['point', 'line', 'boundary', 'centroid', 'area'])
    self.addLiteralInput(identifier = 'distance', title = 'Buffer distance along major axis in map units', minOccurs = 0, maxOccurs = 1, type = type(0.0), allowedValues = '*')
    self.addLiteralInput(identifier = 'minordistance', title = 'Buffer distance along minor axis in map units', minOccurs = 0, maxOccurs = 1, type = type(0.0), allowedValues = '*')
    self.addLiteralInput(identifier = 'angle', title = 'Angle of major axis in degrees', minOccurs = 0, maxOccurs = 1, type = type(0.0), default = 0.0)
    self.addLiteralInput(identifier = 'bufcolumn', title = 'Name of column to use for buffer distances', minOccurs = 0, maxOccurs = 1, type = type("string"), allowedValues = '*')
    self.addLiteralInput(identifier = 'scale', title = 'Scaling factor for attribute column values', minOccurs = 0, maxOccurs = 1, type = type(0.0), default = 1.0)
    self.addLiteralInput(identifier = 'tolerance', title = 'Maximum distance between theoretical arc and polygon segments as multiple of buffer', minOccurs = 0, maxOccurs = 1, type = type(0.0), default = 0.01)
    self.addLiteralInput(identifier = '-s', title = 'Make outside corners straight', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])
    self.addLiteralInput(identifier = '-c', title = 'Dont make caps at the ends of polylines', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])
    self.addLiteralInput(identifier = '-t', title = 'Transfer categories and attributes', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])

    # complex outputs
    self.addComplexOutput(identifier = 'output', title = 'Name for output vector map', formats = [{'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/3.1.1/base/gml.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/xml', 'schema': 'http://schemas.opengis.net/gml/3.1.1/base/gml.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/kml/2.2.0/ogckml22.xsd', 'encoding': 'UTF-8'}])

  def execute(self):
    starter = PyWPSGrassModuleStarter()
    starter.fromPyWPS("v.buffer", self.inputs, self.outputs, self.pywps)

if __name__ == "__main__":
  process = v_buffer()
  process.execute()
