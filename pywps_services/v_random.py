# ################################################ #
# This process was generated using GrassXMLtoPyWPS #
# Author: Soeren Gebbert                           #
# Mail: soerengebbert <at> googlemail <dot> com    #
# ################################################ #

from pywps.Process import WPSProcess

from PyWPSGrassModuleStarter import PyWPSGrassModuleStarter

class v_random(WPSProcess):

  def __init__(self):
    WPSProcess.__init__(self, identifier = 'v.random', title = 'Generates randomly 2D/3D vector points map.', version = 1, statusSupported = True, storeSupported = True, metadata = [{'type': 'simple', 'title': 'vector'}, {'type': 'simple', 'title': 'sampling'}, {'type': 'simple', 'title': 'statistics'}, {'type': 'simple', 'title': 'random'}], abstract = 'http://grass.osgeo.org/grass70/manuals/html70_user/v.random.html')

    # Literal and complex inputs
    self.addLiteralInput(identifier = 'n', title = 'Number of points to be created', minOccurs = 1, maxOccurs = 1, type = type(0), allowedValues = '*')
    self.addLiteralInput(identifier = 'zmin', title = 'Minimum z height (needs -z flag or column name)', minOccurs = 0, maxOccurs = 1, type = type(0.0), default = 0.0)
    self.addLiteralInput(identifier = 'zmax', title = 'Maximum z height (needs -z flag or column name)', minOccurs = 0, maxOccurs = 1, type = type(0.0), default = 0.0)
    self.addLiteralInput(identifier = 'seed', title = 'The seed to initialize the random generator. If not set the process id is used.', minOccurs = 0, maxOccurs = 1, type = type(0), allowedValues = '*')
    self.addLiteralInput(identifier = 'column', title = 'Writes z values to column', minOccurs = 0, maxOccurs = 1, type = type("string"), allowedValues = '*')
    self.addLiteralInput(identifier = 'column_type', title = 'Type of column for z values', minOccurs = 0, maxOccurs = 1, type = type("string"), default = "double precision", allowedValues = ['integer', 'double precision'])
    self.addLiteralInput(identifier = '-z', title = 'Create 3D output', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])
    self.addLiteralInput(identifier = '-d', title = 'Use drand48() function instead of rand()', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])
    self.addLiteralInput(identifier = '-b', title = 'Do not build topology', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])

    # complex outputs
    self.addComplexOutput(identifier = 'output', title = 'Name for output vector map', formats = [{'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/3.1.1/base/gml.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/xml', 'schema': 'http://schemas.opengis.net/gml/3.1.1/base/gml.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/kml/2.2.0/ogckml22.xsd', 'encoding': 'UTF-8'}])

  def execute(self):
    starter = PyWPSGrassModuleStarter()
    starter.fromPyWPS("v.random", self.inputs, self.outputs, self.pywps)

if __name__ == "__main__":
  process = v_random()
  process.execute()
