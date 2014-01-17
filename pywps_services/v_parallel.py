# ################################################ #
# This process was generated using GrassXMLtoPyWPS #
# Author: Soeren Gebbert                           #
# Mail: soerengebbert <at> googlemail <dot> com    #
# ################################################ #

from pywps.Process import WPSProcess

from PyWPSGrassModuleStarter import PyWPSGrassModuleStarter

class v_parallel(WPSProcess):

  def __init__(self):
    WPSProcess.__init__(self, identifier = 'v.parallel', title = 'Creates parallel line to input vector lines.', version = 1, statusSupported = True, storeSupported = True, metadata = [{'type': 'simple', 'title': 'vector'}, {'type': 'simple', 'title': 'geometry'}], abstract = 'http://grass.osgeo.org/grass70/manuals/html70_user/v.parallel.html')

    # Literal and complex inputs
    self.addComplexInput(identifier = 'input', title = 'Or data source for direct OGR access', minOccurs = 1, maxOccurs = 1, formats = [{'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/3.1.1/base/gml.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/xml', 'schema': 'http://schemas.opengis.net/gml/3.1.1/base/gml.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/kml/2.2.0/ogckml22.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/dgn', 'schema': 'None', 'encoding': 'None'}, {'mimeType': 'application/shp', 'schema': 'None', 'encoding': 'None'}, {'mimeType': 'application/x-zipped-shp', 'schema': 'None', 'encoding': 'None'}])
    self.addLiteralInput(identifier = 'layer', title = 'A single vector map can be connected to multiple database tables. This number determines which table to use. When used with direct OGR access this is the layer name.', minOccurs = 0, maxOccurs = 1, type = type("string"), default = "-1")
    self.addLiteralInput(identifier = 'distance', title = 'Offset along major axis in map units', minOccurs = 1, maxOccurs = 1, type = type(0.0), allowedValues = '*')
    self.addLiteralInput(identifier = 'minordistance', title = 'Offset along minor axis in map units', minOccurs = 0, maxOccurs = 1, type = type(0.0), allowedValues = '*')
    self.addLiteralInput(identifier = 'angle', title = 'Angle of major axis in degrees', minOccurs = 0, maxOccurs = 1, type = type(0.0), default = 0.0)
    self.addLiteralInput(identifier = 'side', title = 'Side', minOccurs = 1, maxOccurs = 1, type = type("string"), default = "right", allowedValues = ['left', 'right', 'both'])
    self.addLiteralInput(identifier = 'tolerance', title = 'Tolerance of arc polylines in map units', minOccurs = 0, maxOccurs = 1, type = type(0.0), allowedValues = '*')
    self.addLiteralInput(identifier = '-r', title = 'Make outside corners round', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])
    self.addLiteralInput(identifier = '-b', title = 'Create buffer-like parallel lines', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])

    # complex outputs
    self.addComplexOutput(identifier = 'output', title = 'Name for output vector map', formats = [{'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/3.1.1/base/gml.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/xml', 'schema': 'http://schemas.opengis.net/gml/3.1.1/base/gml.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/kml/2.2.0/ogckml22.xsd', 'encoding': 'UTF-8'}])

  def execute(self):
    starter = PyWPSGrassModuleStarter()
    starter.fromPyWPS("v.parallel", self.inputs, self.outputs, self.pywps)

if __name__ == "__main__":
  process = v_parallel()
  process.execute()
