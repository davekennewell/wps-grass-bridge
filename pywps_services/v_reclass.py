# ################################################ #
# This process was generated using GrassXMLtoPyWPS #
# Author: Soeren Gebbert                           #
# Mail: soerengebbert <at> googlemail <dot> com    #
# ################################################ #

from pywps.Process import WPSProcess

from PyWPSGrassModuleStarter import PyWPSGrassModuleStarter

class v_reclass(WPSProcess):

  def __init__(self):
    WPSProcess.__init__(self, identifier = 'v.reclass', title = 'Changes vector category values for an existing vector map according to results of SQL queries or a value in attribute table column.', version = 1, statusSupported = True, storeSupported = True, metadata = [{'type': 'simple', 'title': 'vector'}, {'type': 'simple', 'title': 'reclassification'}, {'type': 'simple', 'title': 'attributes'}], abstract = 'http://grass.osgeo.org/grass70/manuals/html70_user/v.reclass.html')

    # Literal and complex inputs
    self.addComplexInput(identifier = 'input', title = 'Name of input vector map', abstract = 'Or data source for direct OGR access', minOccurs = 1, maxOccurs = 1, formats = [{'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/3.1.1/base/gml.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/xml', 'schema': 'http://schemas.opengis.net/gml/3.1.1/base/gml.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/kml/2.2.0/ogckml22.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/dgn', 'schema': 'None', 'encoding': 'None'}, {'mimeType': 'application/shp', 'schema': 'None', 'encoding': 'None'}, {'mimeType': 'application/x-zipped-shp', 'schema': 'None', 'encoding': 'None'}])
    self.addLiteralInput(identifier = 'layer', title = 'Layer number or name', abstract = 'Vector features can have category values in different layers. This number determines which layer to use. When used with direct OGR access this is the layer name.', minOccurs = 0, maxOccurs = 1, type = type("string"), default = "1")
    self.addLiteralInput(identifier = 'type', title = 'Feature type', minOccurs = 0, maxOccurs = 1024, type = type("string"), default = "point,line,boundary,centroid", allowedValues = ['point', 'line', 'boundary', 'centroid'])
    self.addLiteralInput(identifier = 'column', title = 'The name of the column whose values are to be used as new categories', abstract = 'The source for the new key column must be type integer or string', minOccurs = 0, maxOccurs = 1, type = type("string"), allowedValues = '*')
    self.addComplexInput(identifier = 'rules', title = 'Full path to the reclass rule file', minOccurs = 0, maxOccurs = 1, formats = [{'mimeType': 'text/plain'}])

    # complex outputs
    self.addComplexOutput(identifier = 'output', title = 'Name for output vector map', formats = [{'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/3.1.1/base/gml.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/xml', 'schema': 'http://schemas.opengis.net/gml/3.1.1/base/gml.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/kml/2.2.0/ogckml22.xsd', 'encoding': 'UTF-8'}])

  def execute(self):
    starter = PyWPSGrassModuleStarter()
    starter.fromPyWPS("v.reclass", self.inputs, self.outputs, self.pywps)

if __name__ == "__main__":
  process = v_reclass()
  process.execute()
