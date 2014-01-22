# ################################################ #
# This process was generated using GrassXMLtoPyWPS #
# Author: Soeren Gebbert                           #
# Mail: soerengebbert <at> googlemail <dot> com    #
# ################################################ #

from pywps.Process import WPSProcess

from PyWPSGrassModuleStarter import PyWPSGrassModuleStarter

class v_lidar_edgedetection(WPSProcess):

  def __init__(self):
    WPSProcess.__init__(self, identifier = 'v.lidar.edgedetection', title = 'Detects the objects edges from a LIDAR data set.', version = 1, statusSupported = True, storeSupported = True, metadata = [{'type': 'simple', 'title': 'vector'}, {'type': 'simple', 'title': 'LIDAR'}, {'type': 'simple', 'title': 'edges'}], abstract = 'http://grass.osgeo.org/grass70/manuals/html70_user/v.lidar.edgedetection.html')

    # Literal and complex inputs
    self.addComplexInput(identifier = 'input', title = 'Name of input vector map', abstract = 'Or data source for direct OGR access', minOccurs = 1, maxOccurs = 1, formats = [{'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/3.1.1/base/gml.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/xml', 'schema': 'http://schemas.opengis.net/gml/3.1.1/base/gml.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/kml/2.2.0/ogckml22.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/dgn', 'schema': 'None', 'encoding': 'None'}, {'mimeType': 'application/shp', 'schema': 'None', 'encoding': 'None'}, {'mimeType': 'application/x-zipped-shp', 'schema': 'None', 'encoding': 'None'}])
    self.addLiteralInput(identifier = 'see', title = 'Interpolation spline step value in east direction', minOccurs = 0, maxOccurs = 1, type = type(0.0), default = 4.0)
    self.addLiteralInput(identifier = 'sen', title = 'Interpolation spline step value in north direction', minOccurs = 0, maxOccurs = 1, type = type(0.0), default = 4.0)
    self.addLiteralInput(identifier = 'lambda_g', title = 'Regularization weight in gradient evaluation', minOccurs = 0, maxOccurs = 1, type = type(0.0), default = 0.01)
    self.addLiteralInput(identifier = 'tgh', title = 'High gradient threshold for edge classification', minOccurs = 0, maxOccurs = 1, type = type(0.0), default = 6.0)
    self.addLiteralInput(identifier = 'tgl', title = 'Low gradient threshold for edge classification', minOccurs = 0, maxOccurs = 1, type = type(0.0), default = 3.0)
    self.addLiteralInput(identifier = 'theta_g', title = 'Angle range for same direction detection', minOccurs = 0, maxOccurs = 1, type = type(0.0), default = 0.26)
    self.addLiteralInput(identifier = 'lambda_r', title = 'Regularization weight in residual evaluation', minOccurs = 0, maxOccurs = 1, type = type(0.0), default = 2.0)
    self.addLiteralInput(identifier = '-e', title = 'Estimate point density and distance for the input vector points within the current region extends and quit', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])

    # complex outputs
    self.addComplexOutput(identifier = 'output', title = 'Name for output vector map', formats = [{'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/3.1.1/base/gml.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/xml', 'schema': 'http://schemas.opengis.net/gml/3.1.1/base/gml.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/kml/2.2.0/ogckml22.xsd', 'encoding': 'UTF-8'}])

  def execute(self):
    starter = PyWPSGrassModuleStarter()
    starter.fromPyWPS("v.lidar.edgedetection", self.inputs, self.outputs, self.pywps)

if __name__ == "__main__":
  process = v_lidar_edgedetection()
  process.execute()
