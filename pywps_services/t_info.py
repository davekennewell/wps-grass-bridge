# ################################################ #
# This process was generated using GrassXMLtoPyWPS #
# Author: Soeren Gebbert                           #
# Mail: soerengebbert <at> googlemail <dot> com    #
# ################################################ #

from pywps.Process import WPSProcess

from PyWPSGrassModuleStarter import PyWPSGrassModuleStarter

class t_info(WPSProcess):

  def __init__(self):
    WPSProcess.__init__(self, identifier = 't.info', title = 'Lists information about space time datasets and maps.', version = 1, statusSupported = True, storeSupported = True, metadata = [{'type': 'simple', 'title': 'temporal'}, {'type': 'simple', 'title': 'metadata'}], abstract = 'http://grass.osgeo.org/grass70/manuals/html70_user/t.info.html')

    # Literal and complex inputs
    self.addComplexInput(identifier = 'input', title = 'Name of an existing space time dataset or map', minOccurs = 1, maxOccurs = 1, formats = [{'mimeType': 'application/x-grass-strds-tar'}, {'mimeType': 'application/x-grass-strds-tar-gz'}, {'mimeType': 'application/x-grass-strds-tar-bzip'}, {'mimeType': 'application/x-grass-stvds-tar'}, {'mimeType': 'application/x-grass-stvds-tar-gz'}, {'mimeType': 'application/x-grass-stvds-tar-bzip'}])
    self.addLiteralInput(identifier = 'type', title = 'Type of the dataset, default is strds (space time raster dataset)', minOccurs = 0, maxOccurs = 1, type = type("string"), default = "strds", allowedValues = ['strds', 'str3ds', 'stvds', 'rast', 'rast3d', 'vect'])
    self.addLiteralInput(identifier = '-g', title = 'Print information in shell style', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])
    self.addLiteralInput(identifier = '-h', title = 'Print history information in human readable shell style for space time datasets', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])
    self.addLiteralInput(identifier = '-s', title = 'Print information about the temporal DBMI interface and exit', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])

    # complex outputs
    self.addComplexOutput(identifier = 'stdout', title = 'Module output on stdout', abstract = 'The output of the module written to stdout', formats = [{'mimeType': 'text/plain'}])

  def execute(self):
    starter = PyWPSGrassModuleStarter()
    starter.fromPyWPS("t.info", self.inputs, self.outputs, self.pywps)

if __name__ == "__main__":
  process = t_info()
  process.execute()
