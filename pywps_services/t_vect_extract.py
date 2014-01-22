# ################################################ #
# This process was generated using GrassXMLtoPyWPS #
# Author: Soeren Gebbert                           #
# Mail: soerengebbert <at> googlemail <dot> com    #
# ################################################ #

from pywps.Process import WPSProcess

from PyWPSGrassModuleStarter import PyWPSGrassModuleStarter

class t_vect_extract(WPSProcess):

  def __init__(self):
    WPSProcess.__init__(self, identifier = 't.vect.extract', title = 'Extracts a subset of a space time vector dataset.', version = 1, statusSupported = True, storeSupported = True, metadata = [{'type': 'simple', 'title': 'temporal'}, {'type': 'simple', 'title': 'extract'}], abstract = 'http://grass.osgeo.org/grass70/manuals/html70_user/t.vect.extract.html')

    # Literal and complex inputs
    self.addComplexInput(identifier = 'input', title = 'Name of the input space time vector dataset', minOccurs = 1, maxOccurs = 1, formats = [{'mimeType': 'application/x-grass-stvds-tar'}, {'mimeType': 'application/x-grass-stvds-tar-gz'}, {'mimeType': 'application/x-grass-stvds-tar-bzip'}])
    self.addLiteralInput(identifier = 'where', title = 'WHERE conditions of SQL statement without where keyword used in the temporal GIS framework', abstract = 'Example: start_time &#62; 2001-01-01 12:30:00', minOccurs = 0, maxOccurs = 1, type = type("string"), allowedValues = '*')
    self.addLiteralInput(identifier = 'expression', title = 'WHERE conditions of SQL statement without where keyword', abstract = 'Example: income &#60; 1000 and inhab &#62;= 10000', minOccurs = 0, maxOccurs = 1, type = type("string"), allowedValues = '*')
    self.addLiteralInput(identifier = 'layer', title = 'Layer number or name', abstract = 'Vector features can have category values in different layers. This number determines which layer to use. When used with direct OGR access this is the layer name.', minOccurs = 0, maxOccurs = 1, type = type("string"), default = "1")
    self.addLiteralInput(identifier = 'type', title = 'Feature type', minOccurs = 0, maxOccurs = 1024, type = type("string"), default = "point,line,boundary,centroid,area", allowedValues = ['point', 'line', 'boundary', 'centroid', 'area'])
    self.addLiteralInput(identifier = 'basename', title = 'Base name of the new generated output maps"', abstract = 'A numerical suffix separated by an underscore will be attached to create a unique identifier', minOccurs = 0, maxOccurs = 1, type = type("string"), allowedValues = '*')
    self.addLiteralInput(identifier = 'nprocs', title = 'The number of v.extract processes to run in parallel. Use only if database backend is used which supports concurrent writing', minOccurs = 0, maxOccurs = 1, type = type(0), default = 1)
    self.addLiteralInput(identifier = '-n', title = 'Register empty maps', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])

    # complex outputs
    self.addComplexOutput(identifier = 'output', title = 'Name of the output space time vector dataset', formats = [{'mimeType': 'application/x-grass-stvds-tar'}, {'mimeType': 'application/x-grass-stvds-tar-gz'}, {'mimeType': 'application/x-grass-stvds-tar-bzip'}])

  def execute(self):
    starter = PyWPSGrassModuleStarter()
    starter.fromPyWPS("t.vect.extract", self.inputs, self.outputs, self.pywps)

if __name__ == "__main__":
  process = t_vect_extract()
  process.execute()
