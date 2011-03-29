# ################################################ #
# This process was generated using GrassXMLtoPyWPS #
# Author: Soeren Gebbert                           #
# Mail: soerengebbert <at> googlemail <dot> com    #
# ################################################ #

from pywps.Process import WPSProcess

from PyWPSGrassModuleStarter import PyWPSGrassModuleStarter

class v_net_path(WPSProcess):

  def __init__(self):
    WPSProcess.__init__(self, identifier = 'v.net.path', title = 'Finds shortest path on vector network.', version = 1, statusSupported = True, storeSupported = True, metadata = [{'type': 'simple', 'title': 'vector'}, {'type': 'simple', 'title': 'networking'}], abstract = 'http://grass.osgeo.org/grass70/manuals/html70_user/v.net.path.html')

    # Literal and complex inputs
    self.addComplexInput(identifier = 'input', title = 'Data source for direct OGR access', minOccurs = 1, maxOccurs = 1, formats = [{'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/kml/2.2.0/ogckml22.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/dgn', 'schema': 'None', 'encoding': 'None'}, {'mimeType': 'application/shp', 'schema': 'None', 'encoding': 'None'}, {'mimeType': 'application/x-zipped-shp', 'schema': 'None', 'encoding': 'None'}])
    self.addLiteralInput(identifier = 'type', title = 'Arc type', minOccurs = 0, maxOccurs = 1024, type = type("string"), default = "line,boundary", allowedValues = ['line', 'boundary'])
    self.addLiteralInput(identifier = 'alayer', title = 'Arc layer', minOccurs = 1, maxOccurs = 1, type = type("string"), default = "1")
    self.addLiteralInput(identifier = 'nlayer', title = 'Node layer', minOccurs = 1, maxOccurs = 1, type = type("string"), default = "2")
    self.addComplexInput(identifier = 'file', title = 'Name of file containing start and end points. If not given, read from stdin', minOccurs = 0, maxOccurs = 1, formats = [{'mimeType': 'text/plain'}])
    self.addLiteralInput(identifier = 'afcolumn', title = 'Arc forward/both direction(s) cost column', minOccurs = 0, maxOccurs = 1, type = type("string"), allowedValues = '*')
    self.addLiteralInput(identifier = 'abcolumn', title = 'Arc backward direction cost column', minOccurs = 0, maxOccurs = 1, type = type("string"), allowedValues = '*')
    self.addLiteralInput(identifier = 'ncolumn', title = 'Node cost column', minOccurs = 0, maxOccurs = 1, type = type("string"), allowedValues = '*')
    self.addLiteralInput(identifier = 'dmax', title = 'If start/end are given as coordinates. If start/end point is outside this threshold, the path is not found and error message is printed. To speed up the process, keep this value as low as possible.', minOccurs = 0, maxOccurs = 1, type = type(0.0), default = 1000.0)
    self.addLiteralInput(identifier = '-g', title = 'Use geodesic calculation for longitude-latitude locations', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])
    self.addLiteralInput(identifier = '-s', title = 'Write output as original input segments, not each path as one line.', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])

    # complex outputs
    self.addComplexOutput(identifier = 'output', title = 'Name for output vector map', formats = [{'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/kml/2.2.0/ogckml22.xsd', 'encoding': 'UTF-8'}])

  def execute(self):
    starter = PyWPSGrassModuleStarter()
    starter.fromPyWPS("v.net.path", self.inputs, self.outputs, self.pywps)

if __name__ == "__main__":
  process = v_net_path()
  process.execute()
