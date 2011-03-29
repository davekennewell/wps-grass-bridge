# ################################################ #
# This process was generated using GrassXMLtoPyWPS #
# Author: Soeren Gebbert                           #
# Mail: soerengebbert <at> googlemail <dot> com    #
# ################################################ #

from pywps.Process import WPSProcess

from PyWPSGrassModuleStarter import PyWPSGrassModuleStarter

class v_net_timetable(WPSProcess):

  def __init__(self):
    WPSProcess.__init__(self, identifier = 'v.net.timetable', title = 'Finds shortest path using timetables.', version = 1, statusSupported = True, storeSupported = True, metadata = [{'type': 'simple', 'title': 'vector'}, {'type': 'simple', 'title': 'network'}, {'type': 'simple', 'title': 'shortest path'}], abstract = 'http://grass.osgeo.org/grass70/manuals/html70_user/v.net.timetable.html')

    # Literal and complex inputs
    self.addComplexInput(identifier = 'input', title = 'Data source for direct OGR access', minOccurs = 1, maxOccurs = 1, formats = [{'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/kml/2.2.0/ogckml22.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/dgn', 'schema': 'None', 'encoding': 'None'}, {'mimeType': 'application/shp', 'schema': 'None', 'encoding': 'None'}, {'mimeType': 'application/x-zipped-shp', 'schema': 'None', 'encoding': 'None'}])
    self.addLiteralInput(identifier = 'layer', title = 'A single vector map can be connected to multiple database tables. This number determines which table to use. Layer name for direct OGR access.', minOccurs = 1, maxOccurs = 1, type = type("string"), default = "1")
    self.addLiteralInput(identifier = 'walk_layer', title = 'A single vector map can be connected to multiple database tables. This number determines which table to use. Layer name for direct OGR access.', minOccurs = 1, maxOccurs = 1, type = type("string"), default = "-1")
    self.addLiteralInput(identifier = 'path_layer', title = 'A single vector map can be connected to multiple database tables. This number determines which table to use. Layer name for direct OGR access.', minOccurs = 1, maxOccurs = 1, type = type("string"), default = "-1")
    self.addLiteralInput(identifier = 'route_id', title = 'Name of column name with route ids', minOccurs = 1, maxOccurs = 1, type = type("string"), default = "route_id")
    self.addLiteralInput(identifier = 'stop_time', title = 'Name of column name with stop timestamps', minOccurs = 1, maxOccurs = 1, type = type("string"), default = "stop_time")
    self.addLiteralInput(identifier = 'to_stop', title = 'Name of column name with stop ids', minOccurs = 1, maxOccurs = 1, type = type("string"), default = "to_stop")
    self.addLiteralInput(identifier = 'walk_length', title = 'Name of column name with walk lengths', minOccurs = 1, maxOccurs = 1, type = type("string"), default = "length")

    # complex outputs
    self.addComplexOutput(identifier = 'output', title = 'Name for output vector map', formats = [{'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/kml/2.2.0/ogckml22.xsd', 'encoding': 'UTF-8'}])

  def execute(self):
    starter = PyWPSGrassModuleStarter()
    starter.fromPyWPS("v.net.timetable", self.inputs, self.outputs, self.pywps)

if __name__ == "__main__":
  process = v_net_timetable()
  process.execute()
