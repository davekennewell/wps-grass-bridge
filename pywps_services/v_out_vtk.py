# ################################################ #
# This process was generated using GrassXMLtoPyWPS #
# Author: Soeren Gebbert                           #
# Mail: soerengebbert <at> googlemail <dot> com    #
# ################################################ #

from pywps.Process import WPSProcess

from PyWPSGrassModuleStarter import PyWPSGrassModuleStarter

class v_out_vtk(WPSProcess):

  def __init__(self):
    WPSProcess.__init__(self, identifier = 'v.out.vtk', title = 'Converts a vector map to VTK ASCII output.', version = 1, statusSupported = True, storeSupported = True, metadata = [{'type': 'simple', 'title': 'vector'}, {'type': 'simple', 'title': 'export'}], abstract = 'http://grass.osgeo.org/grass70/manuals/html70_user/v.out.vtk.html')

    # Literal and complex inputs
    self.addComplexInput(identifier = 'input', title = 'Data source for direct OGR access', minOccurs = 1, maxOccurs = 1, formats = [{'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/kml/2.2.0/ogckml22.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/dgn', 'schema': 'None', 'encoding': 'None'}, {'mimeType': 'application/shp', 'schema': 'None', 'encoding': 'None'}, {'mimeType': 'application/x-zipped-shp', 'schema': 'None', 'encoding': 'None'}])
    self.addComplexInput(identifier = 'output', title = 'Path to resulting VTK file', minOccurs = 0, maxOccurs = 1, formats = [{'mimeType': 'text/plain'}])
    self.addLiteralInput(identifier = 'type', title = 'Feature type', minOccurs = 0, maxOccurs = 1024, type = type("string"), default = "point,kernel,centroid,line,boundary,area,face", allowedValues = ['point', 'kernel', 'centroid', 'line', 'boundary', 'area', 'face'])
    self.addLiteralInput(identifier = 'dp', title = 'Number of significant digits (floating point only)', minOccurs = 0, maxOccurs = 1, type = type(0), allowedValues = '*')
    self.addLiteralInput(identifier = 'scale', title = 'Scale factor for elevation', minOccurs = 0, maxOccurs = 1, type = type(0.0), default = 1.0)
    self.addLiteralInput(identifier = 'layer', title = 'Layer number', minOccurs = 0, maxOccurs = 1, type = type(0), default = 1)
    self.addLiteralInput(identifier = '-c', title = 'Correct the coordinates to fit the VTK-OpenGL precision', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])

    # complex outputs
    self.addComplexOutput(identifier = 'stdout', title = 'Module output on stdout', abstract = 'The output of the module written to stdout', formats = [{'mimeType': 'text/plain'}])

  def execute(self):
    starter = PyWPSGrassModuleStarter()
    starter.fromPyWPS("v.out.vtk", self.inputs, self.outputs, self.pywps)

if __name__ == "__main__":
  process = v_out_vtk()
  process.execute()
