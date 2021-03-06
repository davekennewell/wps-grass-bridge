# ################################################ #
# This process was generated using GrassXMLtoPyWPS #
# Author: Soeren Gebbert                           #
# Mail: soerengebbert <at> googlemail <dot> com    #
# ################################################ #

from pywps.Process import WPSProcess

from PyWPSGrassModuleStarter import PyWPSGrassModuleStarter

class v_transform(WPSProcess):

  def __init__(self):
    WPSProcess.__init__(self, identifier = 'v.transform', title = 'Performs an affine transformation (shift, scale and rotate) on vector map.', version = 1, statusSupported = True, storeSupported = True, metadata = [{'type': 'simple', 'title': 'vector'}, {'type': 'simple', 'title': 'transformation'}, {'type': 'simple', 'title': 'GCP'}], abstract = 'http://grass.osgeo.org/grass70/manuals/html70_user/v.transform.html')

    # Literal and complex inputs
    self.addComplexInput(identifier = 'input', title = 'Name of input vector map', abstract = 'Or data source for direct OGR access', minOccurs = 1, maxOccurs = 1, formats = [{'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/3.1.1/base/gml.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/xml', 'schema': 'http://schemas.opengis.net/gml/3.1.1/base/gml.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/kml/2.2.0/ogckml22.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/dgn', 'schema': 'None', 'encoding': 'None'}, {'mimeType': 'application/shp', 'schema': 'None', 'encoding': 'None'}, {'mimeType': 'application/x-zipped-shp', 'schema': 'None', 'encoding': 'None'}])
    self.addLiteralInput(identifier = 'layer', title = 'Layer number or name (-1 for all layers)', abstract = 'A single vector map can be connected to multiple database tables. This number determines which table to use. When used with direct OGR access this is the layer name.', minOccurs = 0, maxOccurs = 1, type = type("string"), default = "-1")
    self.addLiteralInput(identifier = 'xshift', title = 'Shifting value for x coordinates', minOccurs = 0, maxOccurs = 1, type = type(0.0), default = 0.0)
    self.addLiteralInput(identifier = 'yshift', title = 'Shifting value for y coordinates', minOccurs = 0, maxOccurs = 1, type = type(0.0), default = 0.0)
    self.addLiteralInput(identifier = 'zshift', title = 'Shifting value for z coordinates', minOccurs = 0, maxOccurs = 1, type = type(0.0), default = 0.0)
    self.addLiteralInput(identifier = 'xscale', title = 'Scaling factor for x coordinates', minOccurs = 0, maxOccurs = 1, type = type(0.0), default = 1.0)
    self.addLiteralInput(identifier = 'yscale', title = 'Scaling factor for y coordinates', minOccurs = 0, maxOccurs = 1, type = type(0.0), default = 1.0)
    self.addLiteralInput(identifier = 'zscale', title = 'Scaling factor for z coordinates', minOccurs = 0, maxOccurs = 1, type = type(0.0), default = 1.0)
    self.addLiteralInput(identifier = 'zrot', title = 'Rotation around z axis in degrees counterclockwise', minOccurs = 0, maxOccurs = 1, type = type(0.0), default = 0.0)
    self.addLiteralInput(identifier = 'columns', title = 'Name of attribute column(s) used as transformation parameters', abstract = 'Format: parameter:column, e.g. xshift:xs,yshift:ys,zrot:zr', minOccurs = 0, maxOccurs = 1024, type = type("string"), allowedValues = '*')
    self.addLiteralInput(identifier = '-t', title = 'Shift all z values to bottom=0', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])
    self.addLiteralInput(identifier = '-w', title = 'Swap coordinates x, y and then apply other parameters', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])
    self.addLiteralInput(identifier = '-b', title = 'Do not build topology for output', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])

    # complex outputs
    self.addComplexOutput(identifier = 'output', title = 'Name for output vector map', formats = [{'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/3.1.1/base/gml.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/xml', 'schema': 'http://schemas.opengis.net/gml/3.1.1/base/gml.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/kml/2.2.0/ogckml22.xsd', 'encoding': 'UTF-8'}])

  def execute(self):
    starter = PyWPSGrassModuleStarter()
    starter.fromPyWPS("v.transform", self.inputs, self.outputs, self.pywps)

if __name__ == "__main__":
  process = v_transform()
  process.execute()
