# ################################################ #
# This process was generated using GrassXMLtoPyWPS #
# Author: Soeren Gebbert                           #
# Mail: soerengebbert <at> googlemail <dot> com    #
# ################################################ #

from pywps.Process import WPSProcess

from PyWPSGrassModuleStarter import PyWPSGrassModuleStarter

class v_class(WPSProcess):

  def __init__(self):
    WPSProcess.__init__(self, identifier = 'v.class', title = 'Classifies attribute data, e.g. for thematic mapping', version = 1, statusSupported = True, storeSupported = True, metadata = [{'type': 'simple', 'title': 'vector'}, {'type': 'simple', 'title': 'classification'}, {'type': 'simple', 'title': 'attribute table'}, {'type': 'simple', 'title': 'statistics'}], abstract = 'http://grass.osgeo.org/grass70/manuals/html70_user/v.class.html')

    # Literal and complex inputs
    self.addComplexInput(identifier = 'map', title = 'Or data source for direct OGR access', minOccurs = 1, maxOccurs = 1, formats = [{'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/3.1.1/base/gml.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/xml', 'schema': 'http://schemas.opengis.net/gml/3.1.1/base/gml.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/kml/2.2.0/ogckml22.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/dgn', 'schema': 'None', 'encoding': 'None'}, {'mimeType': 'application/shp', 'schema': 'None', 'encoding': 'None'}, {'mimeType': 'application/x-zipped-shp', 'schema': 'None', 'encoding': 'None'}])
    self.addLiteralInput(identifier = 'layer', title = 'Vector features can have category values in different layers. This number determines which layer to use. When used with direct OGR access this is the layer name.', minOccurs = 1, maxOccurs = 1, type = type("string"), default = "1")
    self.addLiteralInput(identifier = 'column', title = 'Column name or expression', minOccurs = 1, maxOccurs = 1, type = type("string"), allowedValues = '*')
    self.addLiteralInput(identifier = 'where', title = 'Example: income &#60; 1000 and inhab &#62;= 10000', minOccurs = 0, maxOccurs = 1, type = type("string"), allowedValues = '*')
    self.addLiteralInput(identifier = 'algorithm', title = 'Algorithm to use for classification', minOccurs = 1, maxOccurs = 1, type = type("string"), allowedValues = ['int', 'std', 'qua', 'equ', 'dis'])
    self.addLiteralInput(identifier = 'nbclasses', title = 'Number of classes to define', minOccurs = 1, maxOccurs = 1, type = type(0), allowedValues = '*')
    self.addLiteralInput(identifier = '-g', title = 'Print only class breaks (without min and max)', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])

    # complex outputs
    self.addComplexOutput(identifier = 'stdout', title = 'Module output on stdout', abstract = 'The output of the module written to stdout', formats = [{'mimeType': 'text/plain'}])

  def execute(self):
    starter = PyWPSGrassModuleStarter()
    starter.fromPyWPS("v.class", self.inputs, self.outputs, self.pywps)

if __name__ == "__main__":
  process = v_class()
  process.execute()
