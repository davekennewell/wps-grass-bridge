# ################################################ #
# This process was generated using GrassXMLtoPyWPS #
# Author: Soeren Gebbert                           #
# Mail: soerengebbert <at> googlemail <dot> com    #
# ################################################ #

from pywps.Process import WPSProcess

from PyWPSGrassModuleStarter import PyWPSGrassModuleStarter

class v_distance(WPSProcess):

  def __init__(self):
    WPSProcess.__init__(self, identifier = 'v.distance', title = 'Finds the nearest element in vector map to for elements in vector map from.', version = 1, statusSupported = True, storeSupported = True, metadata = [{'type': 'simple', 'title': 'vector'}, {'type': 'simple', 'title': 'distance'}, {'type': 'simple', 'title': 'database'}, {'type': 'simple', 'title': 'attribute table'}], abstract = 'http://grass.osgeo.org/grass70/manuals/html70_user/v.distance.html')

    # Literal and complex inputs
    self.addComplexInput(identifier = 'from', title = 'Name of existing vector map (from)', abstract = 'Or data source for direct OGR access', minOccurs = 1, maxOccurs = 1, formats = [{'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/3.1.1/base/gml.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/xml', 'schema': 'http://schemas.opengis.net/gml/3.1.1/base/gml.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/kml/2.2.0/ogckml22.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/dgn', 'schema': 'None', 'encoding': 'None'}, {'mimeType': 'application/shp', 'schema': 'None', 'encoding': 'None'}, {'mimeType': 'application/x-zipped-shp', 'schema': 'None', 'encoding': 'None'}])
    self.addLiteralInput(identifier = 'from_layer', title = 'Layer number or name (from)', abstract = 'Vector features can have category values in different layers. This number determines which layer to use. When used with direct OGR access this is the layer name.', minOccurs = 0, maxOccurs = 1, type = type("string"), default = "1")
    self.addLiteralInput(identifier = 'from_type', title = 'Feature type (from)', abstract = 'Feature type', minOccurs = 0, maxOccurs = 1024, type = type("string"), default = "point,line,area", allowedValues = ['point', 'line', 'boundary', 'centroid', 'area'])
    self.addComplexInput(identifier = 'to', title = 'Name of existing vector map (to)', abstract = 'Or data source for direct OGR access', minOccurs = 1, maxOccurs = 1, formats = [{'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/3.1.1/base/gml.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/xml', 'schema': 'http://schemas.opengis.net/gml/3.1.1/base/gml.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/kml/2.2.0/ogckml22.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/dgn', 'schema': 'None', 'encoding': 'None'}, {'mimeType': 'application/shp', 'schema': 'None', 'encoding': 'None'}, {'mimeType': 'application/x-zipped-shp', 'schema': 'None', 'encoding': 'None'}])
    self.addLiteralInput(identifier = 'to_layer', title = 'Layer number or name (to)', abstract = 'Vector features can have category values in different layers. This number determines which layer to use. When used with direct OGR access this is the layer name.', minOccurs = 0, maxOccurs = 1, type = type("string"), default = "1")
    self.addLiteralInput(identifier = 'to_type', title = 'Feature type (to)', abstract = 'Feature type', minOccurs = 0, maxOccurs = 1024, type = type("string"), default = "point,line,area", allowedValues = ['point', 'line', 'boundary', 'centroid', 'area'])
    self.addLiteralInput(identifier = 'dmax', title = 'Maximum distance or -1 for no limit', minOccurs = 0, maxOccurs = 1, type = type(0.0), default = -1.0)
    self.addLiteralInput(identifier = 'dmin', title = 'Minimum distance or -1 for no limit', minOccurs = 0, maxOccurs = 1, type = type(0.0), default = -1.0)
    self.addLiteralInput(identifier = 'upload', title = 'Values describing the relation between two nearest features', minOccurs = 1, maxOccurs = 1024, type = type("string"), allowedValues = ['cat', 'dist', 'to_x', 'to_y', 'to_along', 'to_angle', 'to_attr'])
    self.addLiteralInput(identifier = 'column', title = 'Column name(s) where values specified by upload option will be uploaded', minOccurs = 1, maxOccurs = 1024, type = type("string"), allowedValues = '*')
    self.addLiteralInput(identifier = 'to_column', title = 'Column name of nearest feature (used with upload=to_attr)', minOccurs = 0, maxOccurs = 1, type = type("string"), allowedValues = '*')
    self.addLiteralInput(identifier = 'table', title = 'Name of table created when the distance to all flag is used', minOccurs = 0, maxOccurs = 1, type = type("string"), allowedValues = '*')
    self.addLiteralInput(identifier = '-p', title = 'First column is always category of from feature called from_cat', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])
    self.addLiteralInput(identifier = '-a', title = 'Output is written to stdout but may be uploaded to a new table created by this module; multiple upload options may be used.', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])

    # complex outputs
    self.addComplexOutput(identifier = 'output', title = 'Name for output vector map containing lines connecting nearest elements', formats = [{'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/3.1.1/base/gml.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/xml', 'schema': 'http://schemas.opengis.net/gml/3.1.1/base/gml.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/kml/2.2.0/ogckml22.xsd', 'encoding': 'UTF-8'}])

  def execute(self):
    starter = PyWPSGrassModuleStarter()
    starter.fromPyWPS("v.distance", self.inputs, self.outputs, self.pywps)

if __name__ == "__main__":
  process = v_distance()
  process.execute()
