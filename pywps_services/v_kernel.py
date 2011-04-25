# ################################################ #
# This process was generated using GrassXMLtoPyWPS #
# Author: Soeren Gebbert                           #
# Mail: soerengebbert <at> googlemail <dot> com    #
# ################################################ #

from pywps.Process import WPSProcess

from PyWPSGrassModuleStarter import PyWPSGrassModuleStarter

class v_kernel(WPSProcess):

  def __init__(self):
    WPSProcess.__init__(self, identifier = 'v.kernel', title = 'Generates a raster density map from vector point data using a moving kernel or optionally generates a vector density map on a vector network.', version = 1, statusSupported = True, storeSupported = True, metadata = [{'type': 'simple', 'title': 'vector'}, {'type': 'simple', 'title': 'kernel density'}], abstract = 'http://grass.osgeo.org/grass70/manuals/html70_user/v.kernel.html')

    # Literal and complex inputs
    self.addComplexInput(identifier = 'input', title = 'Input vector with training points', minOccurs = 1, maxOccurs = 1, formats = [{'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/3.1.1/base/gml.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/xml', 'schema': 'http://schemas.opengis.net/gml/3.1.1/base/gml.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/kml/2.2.0/ogckml22.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/dgn', 'schema': 'None', 'encoding': 'None'}, {'mimeType': 'application/shp', 'schema': 'None', 'encoding': 'None'}, {'mimeType': 'application/x-zipped-shp', 'schema': 'None', 'encoding': 'None'}])
    self.addComplexInput(identifier = 'net', title = 'Input network vector map', minOccurs = 0, maxOccurs = 1, formats = [{'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/3.1.1/base/gml.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/xml', 'schema': 'http://schemas.opengis.net/gml/3.1.1/base/gml.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/kml/2.2.0/ogckml22.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/dgn', 'schema': 'None', 'encoding': 'None'}, {'mimeType': 'application/shp', 'schema': 'None', 'encoding': 'None'}, {'mimeType': 'application/x-zipped-shp', 'schema': 'None', 'encoding': 'None'}])
    self.addLiteralInput(identifier = 'output', title = 'Output raster/vector map', minOccurs = 1, maxOccurs = 1, type = type("string"), allowedValues = '*')
    self.addLiteralInput(identifier = 'stddeviation', title = 'Standard deviation in map units', minOccurs = 1, maxOccurs = 1, type = type(0.0), allowedValues = '*')
    self.addLiteralInput(identifier = 'dsize', title = 'Discretization error in map units', minOccurs = 0, maxOccurs = 1, type = type(0.0), default = 0.0)
    self.addLiteralInput(identifier = 'segmax', title = 'Maximum length of segment on network', minOccurs = 0, maxOccurs = 1, type = type(0.0), default = 100.0)
    self.addLiteralInput(identifier = 'distmax', title = 'Maximum distance from point to network', minOccurs = 0, maxOccurs = 1, type = type(0.0), default = 100.0)
    self.addLiteralInput(identifier = 'mult', title = 'Multiply the density result by this number', minOccurs = 0, maxOccurs = 1, type = type(0.0), default = 1.0)
    self.addLiteralInput(identifier = 'node', title = 'Node method', minOccurs = 1, maxOccurs = 1, type = type("string"), default = "none", allowedValues = ['none', 'split'])
    self.addLiteralInput(identifier = 'kernel', title = 'Kernel function', minOccurs = 1, maxOccurs = 1, type = type("string"), default = "gaussian", allowedValues = ['uniform', 'triangular', 'epanechnikov', 'quartic', 'triweight', 'gaussian', 'cosine'])
    self.addLiteralInput(identifier = '-o', title = 'Try to calculate an optimal standard deviation with stddeviation taken as maximum (experimental)', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])
    self.addLiteralInput(identifier = '-q', title = 'Only calculate optimal standard deviation and exit (no map is written)', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])
    self.addLiteralInput(identifier = '-n', title = 'In network mode, normalize values by sum of density multiplied by length of each segment. Integral over the output map then gives 1.0 * mult', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])
    self.addLiteralInput(identifier = '-m', title = 'In network mode, multiply the result by number of input points.', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])

    # complex outputs
    self.addComplexOutput(identifier = 'stdout', title = 'Module output on stdout', abstract = 'The output of the module written to stdout', formats = [{'mimeType': 'text/plain'}])

  def execute(self):
    starter = PyWPSGrassModuleStarter()
    starter.fromPyWPS("v.kernel", self.inputs, self.outputs, self.pywps)

if __name__ == "__main__":
  process = v_kernel()
  process.execute()
