# ################################################ #
# This process was generated using GrassXMLtoPyWPS #
# Author: Soeren Gebbert                           #
# Mail: soerengebbert <at> googlemail <dot> com    #
# ################################################ #

from pywps.Process import WPSProcess

from PyWPSGrassModuleStarter import PyWPSGrassModuleStarter

class v_overlay(WPSProcess):

  def __init__(self):
    WPSProcess.__init__(self, identifier = 'v.overlay', title = 'Overlays two vector maps.', version = 1, statusSupported = True, storeSupported = True, metadata = [{'type': 'simple', 'title': 'vector'}, {'type': 'simple', 'title': 'geometry'}, {'type': 'simple', 'title': 'spatial query'}], abstract = 'http://grass.osgeo.org/grass70/manuals/html70_user/v.overlay.html')

    # Literal and complex inputs
    self.addComplexInput(identifier = 'ainput', title = 'Name of input vector map (A)', abstract = 'Or data source for direct OGR access', minOccurs = 1, maxOccurs = 1, formats = [{'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/3.1.1/base/gml.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/xml', 'schema': 'http://schemas.opengis.net/gml/3.1.1/base/gml.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/kml/2.2.0/ogckml22.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/dgn', 'schema': 'None', 'encoding': 'None'}, {'mimeType': 'application/shp', 'schema': 'None', 'encoding': 'None'}, {'mimeType': 'application/x-zipped-shp', 'schema': 'None', 'encoding': 'None'}])
    self.addLiteralInput(identifier = 'alayer', title = 'Layer number or name (vector map A)', abstract = 'Vector features can have category values in different layers. This number determines which layer to use. When used with direct OGR access this is the layer name.', minOccurs = 0, maxOccurs = 1, type = type("string"), default = "1")
    self.addLiteralInput(identifier = 'atype', title = 'Feature type (vector map A)', abstract = 'Feature type', minOccurs = 0, maxOccurs = 1024, type = type("string"), default = "area", allowedValues = ['line', 'area'])
    self.addComplexInput(identifier = 'binput', title = 'Name of input vector map (B)', abstract = 'Or data source for direct OGR access', minOccurs = 1, maxOccurs = 1, formats = [{'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/3.1.1/base/gml.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/xml', 'schema': 'http://schemas.opengis.net/gml/3.1.1/base/gml.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/kml/2.2.0/ogckml22.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/dgn', 'schema': 'None', 'encoding': 'None'}, {'mimeType': 'application/shp', 'schema': 'None', 'encoding': 'None'}, {'mimeType': 'application/x-zipped-shp', 'schema': 'None', 'encoding': 'None'}])
    self.addLiteralInput(identifier = 'blayer', title = 'Layer number or name (vector map B)', abstract = 'Vector features can have category values in different layers. This number determines which layer to use. When used with direct OGR access this is the layer name.', minOccurs = 0, maxOccurs = 1, type = type("string"), default = "1")
    self.addLiteralInput(identifier = 'btype', title = 'Feature type (vector map B)', abstract = 'Feature type', minOccurs = 0, maxOccurs = 1024, type = type("string"), default = "area", allowedValues = ['area'])
    self.addLiteralInput(identifier = 'operator', title = 'Operator defines features written to output vector map', abstract = 'Feature is written to output if the result of operation ainput operator binput is true. Input feature is considered to be true, if category of given layer is defined.', minOccurs = 1, maxOccurs = 1, type = type("string"), allowedValues = ['and', 'or', 'not', 'xor'])
    self.addLiteralInput(identifier = 'olayer', title = 'Output layer for new category, ainput and binput', abstract = 'If 0 or not given, the category is not written', minOccurs = 0, maxOccurs = 1024, type = type("string"), default = "1,0,0")
    self.addLiteralInput(identifier = 'snap', title = 'Snapping threshold for boundaries', abstract = 'Disable snapping with snap &#60;= 0', minOccurs = 0, maxOccurs = 1, type = type(0.0), default = 1e-08)
    self.addLiteralInput(identifier = '-t', title = 'Do not create attribute table', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])

    # complex outputs
    self.addComplexOutput(identifier = 'output', title = 'Name for output vector map', formats = [{'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/3.1.1/base/gml.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/xml', 'schema': 'http://schemas.opengis.net/gml/3.1.1/base/gml.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/kml/2.2.0/ogckml22.xsd', 'encoding': 'UTF-8'}])

  def execute(self):
    starter = PyWPSGrassModuleStarter()
    starter.fromPyWPS("v.overlay", self.inputs, self.outputs, self.pywps)

if __name__ == "__main__":
  process = v_overlay()
  process.execute()
