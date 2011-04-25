# ################################################ #
# This process was generated using GrassXMLtoPyWPS #
# Author: Soeren Gebbert                           #
# Mail: soerengebbert <at> googlemail <dot> com    #
# ################################################ #

from pywps.Process import WPSProcess

from PyWPSGrassModuleStarter import PyWPSGrassModuleStarter

class v_mkgrid(WPSProcess):

  def __init__(self):
    WPSProcess.__init__(self, identifier = 'v.mkgrid', title = 'Creates a vector map of a user-defined grid.', version = 1, statusSupported = True, storeSupported = True, metadata = [{'type': 'simple', 'title': 'vector'}, {'type': 'simple', 'title': 'geometry'}], abstract = 'http://grass.osgeo.org/grass70/manuals/html70_user/v.mkgrid.html')

    # Literal and complex inputs
    self.addLiteralInput(identifier = 'grid', title = 'Number of rows and columns in grid', minOccurs = 1, maxOccurs = 1, type = type(0), allowedValues = '*')
    self.addLiteralInput(identifier = 'position', title = 'Where to place the grid', minOccurs = 0, maxOccurs = 1, type = type("string"), default = "region", allowedValues = ['region', 'coor'])
    self.addLiteralInput(identifier = 'coor', title = 'Lower left easting and northing coordinates of map', minOccurs = 0, maxOccurs = 1, type = type(0.0), allowedValues = '*')
    self.addLiteralInput(identifier = 'box', title = 'Width and height of boxes in grid', minOccurs = 0, maxOccurs = 1, type = type(0.0), allowedValues = '*')
    self.addLiteralInput(identifier = 'angle', title = 'Angle of rotation (in degrees counter-clockwise)', minOccurs = 0, maxOccurs = 1, type = type(0.0), default = 0.0)
    self.addLiteralInput(identifier = 'breaks', title = 'Number of horizontal vertex points per grid cell', minOccurs = 0, maxOccurs = 1, type = type(0), default = 3)
    self.addLiteralInput(identifier = '-p', title = 'Create grid of points instead of areas and centroids', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])

    # complex outputs
    self.addComplexOutput(identifier = 'map', title = 'Name for output vector map', formats = [{'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/3.1.1/base/gml.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/xml', 'schema': 'http://schemas.opengis.net/gml/3.1.1/base/gml.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/kml/2.2.0/ogckml22.xsd', 'encoding': 'UTF-8'}])

  def execute(self):
    starter = PyWPSGrassModuleStarter()
    starter.fromPyWPS("v.mkgrid", self.inputs, self.outputs, self.pywps)

if __name__ == "__main__":
  process = v_mkgrid()
  process.execute()
