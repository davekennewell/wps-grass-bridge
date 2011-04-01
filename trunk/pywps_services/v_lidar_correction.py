# ################################################ #
# This process was generated using GrassXMLtoPyWPS #
# Author: Soeren Gebbert                           #
# Mail: soerengebbert <at> googlemail <dot> com    #
# ################################################ #

from pywps.Process import WPSProcess

from PyWPSGrassModuleStarter import PyWPSGrassModuleStarter

class v_lidar_correction(WPSProcess):

  def __init__(self):
    WPSProcess.__init__(self, identifier = 'v.lidar.correction', title = 'Correction of the v.lidar.growing output. It is the last of the three algorithms for LIDAR filtering.', version = 1, statusSupported = True, storeSupported = True, metadata = [{'type': 'simple', 'title': 'vector'}, {'type': 'simple', 'title': 'LIDAR'}], abstract = 'http://grass.osgeo.org/grass70/manuals/html70_user/v.lidar.correction.html')

    # Literal and complex inputs
    self.addComplexInput(identifier = 'input', title = 'Input observation vector map name (v.lidar.growing output)', minOccurs = 1, maxOccurs = 1, formats = [{'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/kml/2.2.0/ogckml22.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/dgn', 'schema': 'None', 'encoding': 'None'}, {'mimeType': 'application/shp', 'schema': 'None', 'encoding': 'None'}, {'mimeType': 'application/x-zipped-shp', 'schema': 'None', 'encoding': 'None'}])
    self.addLiteralInput(identifier = 'sce', title = 'Interpolation spline step value in east direction', minOccurs = 0, maxOccurs = 1, type = type(0.0), default = 25.0)
    self.addLiteralInput(identifier = 'scn', title = 'Interpolation spline step value in north direction', minOccurs = 0, maxOccurs = 1, type = type(0.0), default = 25.0)
    self.addLiteralInput(identifier = 'lambda_c', title = 'Regularization weight in reclassification evaluation', minOccurs = 0, maxOccurs = 1, type = type(0.0), default = 1.0)
    self.addLiteralInput(identifier = 'tch', title = 'High threshold for object to terrain reclassification', minOccurs = 0, maxOccurs = 1, type = type(0.0), default = 2.0)
    self.addLiteralInput(identifier = 'tcl', title = 'Low threshold for terrain to object reclassification', minOccurs = 0, maxOccurs = 1, type = type(0.0), default = 1.0)
    self.addLiteralInput(identifier = '-e', title = 'Estimate point density and distance for the input vector points within the current region extends and quit', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])

    # complex outputs
    self.addComplexOutput(identifier = 'output', title = 'Output classified vector map name', formats = [{'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/kml/2.2.0/ogckml22.xsd', 'encoding': 'UTF-8'}])

    self.addComplexOutput(identifier = 'terrain', title = 'Only terrain points output vector map', formats = [{'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/kml/2.2.0/ogckml22.xsd', 'encoding': 'UTF-8'}])

  def execute(self):
    starter = PyWPSGrassModuleStarter()
    starter.fromPyWPS("v.lidar.correction", self.inputs, self.outputs, self.pywps)

if __name__ == "__main__":
  process = v_lidar_correction()
  process.execute()
