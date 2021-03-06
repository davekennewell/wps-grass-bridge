# ################################################ #
# This process was generated using GrassXMLtoPyWPS #
# Author: Soeren Gebbert                           #
# Mail: soerengebbert <at> googlemail <dot> com    #
# ################################################ #

from pywps.Process import WPSProcess

from PyWPSGrassModuleStarter import PyWPSGrassModuleStarter

class v_report(WPSProcess):

  def __init__(self):
    WPSProcess.__init__(self, identifier = 'v.report', title = 'Reports geometry statistics for vector maps.', version = 1, statusSupported = True, storeSupported = True, metadata = [{'type': 'simple', 'title': 'vector'}, {'type': 'simple', 'title': 'geometry'}, {'type': 'simple', 'title': 'statistics'}], abstract = 'http://grass.osgeo.org/grass70/manuals/html70_user/v.report.html')

    # Literal and complex inputs
    self.addComplexInput(identifier = 'map', title = 'Name of vector map', abstract = 'Or data source for direct OGR access', minOccurs = 1, maxOccurs = 1, formats = [{'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/3.1.1/base/gml.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/xml', 'schema': 'http://schemas.opengis.net/gml/3.1.1/base/gml.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/kml/2.2.0/ogckml22.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/dgn', 'schema': 'None', 'encoding': 'None'}, {'mimeType': 'application/shp', 'schema': 'None', 'encoding': 'None'}, {'mimeType': 'application/x-zipped-shp', 'schema': 'None', 'encoding': 'None'}])
    self.addLiteralInput(identifier = 'layer', title = 'Layer number or name', abstract = 'Vector features can have category values in different layers. This number determines which layer to use. When used with direct OGR access this is the layer name.', minOccurs = 0, maxOccurs = 1, type = type("string"), default = "1")
    self.addLiteralInput(identifier = 'option', title = 'Value to calculate', minOccurs = 1, maxOccurs = 1, type = type("string"), allowedValues = ['area', 'length', 'coor'])
    self.addLiteralInput(identifier = 'units', title = 'Units', minOccurs = 0, maxOccurs = 1, type = type("string"), allowedValues = ['miles', 'feet', 'meters', 'kilometers', 'acres', 'hectares', 'percent'])
    self.addLiteralInput(identifier = 'sort', title = 'Sort the result', minOccurs = 0, maxOccurs = 1, type = type("string"), allowedValues = ['asc', 'desc'])

    # complex outputs
    self.addComplexOutput(identifier = 'stdout', title = 'Module output on stdout', abstract = 'The output of the module written to stdout', formats = [{'mimeType': 'text/plain'}])

  def execute(self):
    starter = PyWPSGrassModuleStarter()
    starter.fromPyWPS("v.report", self.inputs, self.outputs, self.pywps)

if __name__ == "__main__":
  process = v_report()
  process.execute()
