# ################################################ #
# This process was generated using GrassXMLtoPyWPS #
# Author: Soeren Gebbert                           #
# Mail: soerengebbert <at> googlemail <dot> com    #
# ################################################ #

from pywps.Process import WPSProcess

from PyWPSGrassModuleStarter import PyWPSGrassModuleStarter

class v_generalize(WPSProcess):

  def __init__(self):
    WPSProcess.__init__(self, identifier = 'v.generalize', title = 'Performs vector based generalization.', version = 1, statusSupported = True, storeSupported = True, metadata = [{'type': 'simple', 'title': 'vector'}, {'type': 'simple', 'title': 'generalization'}, {'type': 'simple', 'title': 'simplification'}, {'type': 'simple', 'title': 'smoothing'}, {'type': 'simple', 'title': 'displacement'}, {'type': 'simple', 'title': 'network generalization'}], abstract = 'http://grass.osgeo.org/grass70/manuals/html70_user/v.generalize.html')

    # Literal and complex inputs
    self.addComplexInput(identifier = 'input', title = 'Or data source for direct OGR access', minOccurs = 1, maxOccurs = 1, formats = [{'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/3.1.1/base/gml.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/xml', 'schema': 'http://schemas.opengis.net/gml/3.1.1/base/gml.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/kml/2.2.0/ogckml22.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/dgn', 'schema': 'None', 'encoding': 'None'}, {'mimeType': 'application/shp', 'schema': 'None', 'encoding': 'None'}, {'mimeType': 'application/x-zipped-shp', 'schema': 'None', 'encoding': 'None'}])
    self.addLiteralInput(identifier = 'layer', title = 'A single vector map can be connected to multiple database tables. This number determines which table to use. When used with direct OGR access this is the layer name.', minOccurs = 1, maxOccurs = 1, type = type("string"), default = "-1")
    self.addLiteralInput(identifier = 'type', title = 'Feature type', minOccurs = 0, maxOccurs = 1024, type = type("string"), default = "line,boundary,area", allowedValues = ['line', 'boundary', 'area'])
    self.addLiteralInput(identifier = 'method', title = 'Generalization algorithm', minOccurs = 1, maxOccurs = 1, type = type("string"), allowedValues = ['douglas', 'douglas_reduction', 'lang', 'reduction', 'reumann', 'boyle', 'sliding_averaging', 'distance_weighting', 'chaiken', 'hermite', 'snakes', 'network', 'displacement'])
    self.addLiteralInput(identifier = 'threshold', title = 'Maximal tolerance value', minOccurs = 1, maxOccurs = 1, type = type(0.0), allowedValues = '*')
    self.addLiteralInput(identifier = 'look_ahead', title = 'Look-ahead parameter', minOccurs = 0, maxOccurs = 1, type = type(0), default = 7)
    self.addLiteralInput(identifier = 'reduction', title = 'Percentage of the points in the output of douglas_reduction algorithm', minOccurs = 0, maxOccurs = 1, type = type(0.0), default = 50.0)
    self.addLiteralInput(identifier = 'slide', title = 'Slide of computed point toward the original point', minOccurs = 0, maxOccurs = 1, type = type(0.0), default = 0.5)
    self.addLiteralInput(identifier = 'angle_thresh', title = 'Minimum angle between two consecutive segments in Hermite method', minOccurs = 0, maxOccurs = 1, type = type(0.0), default = 3.0)
    self.addLiteralInput(identifier = 'degree_thresh', title = 'Degree threshold in network generalization', minOccurs = 0, maxOccurs = 1, type = type(0), default = 0)
    self.addLiteralInput(identifier = 'closeness_thresh', title = 'Closeness threshold in network generalization', minOccurs = 0, maxOccurs = 1, type = type(0.0), default = 0.0)
    self.addLiteralInput(identifier = 'betweeness_thresh', title = 'Betweeness threshold in network generalization', minOccurs = 0, maxOccurs = 1, type = type(0.0), default = 0.0)
    self.addLiteralInput(identifier = 'alpha', title = 'Snakes alpha parameter', minOccurs = 0, maxOccurs = 1, type = type(0.0), default = 1.0)
    self.addLiteralInput(identifier = 'beta', title = 'Snakes beta parameter', minOccurs = 0, maxOccurs = 1, type = type(0.0), default = 1.0)
    self.addLiteralInput(identifier = 'iterations', title = 'Number of iterations', minOccurs = 0, maxOccurs = 1, type = type(0), default = 1)
    self.addLiteralInput(identifier = 'cats', title = 'Example: 1,3,7-9,13', minOccurs = 0, maxOccurs = 1, type = type("string"), allowedValues = '*')
    self.addLiteralInput(identifier = 'where', title = 'Example: income &#60; 1000 and inhab &#62;= 10000', minOccurs = 0, maxOccurs = 1, type = type("string"), allowedValues = '*')
    self.addLiteralInput(identifier = '-c', title = 'Copy attributes', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])

    # complex outputs
    self.addComplexOutput(identifier = 'output', title = 'Name for output vector map', formats = [{'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/3.1.1/base/gml.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/xml', 'schema': 'http://schemas.opengis.net/gml/3.1.1/base/gml.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/kml/2.2.0/ogckml22.xsd', 'encoding': 'UTF-8'}])

  def execute(self):
    starter = PyWPSGrassModuleStarter()
    starter.fromPyWPS("v.generalize", self.inputs, self.outputs, self.pywps)

if __name__ == "__main__":
  process = v_generalize()
  process.execute()
