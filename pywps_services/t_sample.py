# ################################################ #
# This process was generated using GrassXMLtoPyWPS #
# Author: Soeren Gebbert                           #
# Mail: soerengebbert <at> googlemail <dot> com    #
# ################################################ #

from pywps.Process import WPSProcess

from PyWPSGrassModuleStarter import PyWPSGrassModuleStarter

class t_sample(WPSProcess):

  def __init__(self):
    WPSProcess.__init__(self, identifier = 't.sample', title = 'Samples the input space time dataset(s) with a sample space time dataset and print the result to stdout.', version = 1, statusSupported = True, storeSupported = True, metadata = [{'type': 'simple', 'title': 'temporal'}, {'type': 'simple', 'title': 'sample'}], abstract = 'http://grass.osgeo.org/grass70/manuals/html70_user/t.sample.html')

    # Literal and complex inputs
    self.addComplexInput(identifier = 'inputs', title = 'Name of the input space time datasets', minOccurs = 1, maxOccurs = 1024, formats = [{'mimeType': 'application/x-grass-strds-tar'}, {'mimeType': 'application/x-grass-strds-tar-gz'}, {'mimeType': 'application/x-grass-strds-tar-bzip'}, {'mimeType': 'application/x-grass-stvds-tar'}, {'mimeType': 'application/x-grass-stvds-tar-gz'}, {'mimeType': 'application/x-grass-stvds-tar-bzip'}])
    self.addComplexInput(identifier = 'sample', title = 'Name of the sample space time dataset', minOccurs = 1, maxOccurs = 1, formats = [{'mimeType': 'application/x-grass-strds-tar'}, {'mimeType': 'application/x-grass-strds-tar-gz'}, {'mimeType': 'application/x-grass-strds-tar-bzip'}, {'mimeType': 'application/x-grass-stvds-tar'}, {'mimeType': 'application/x-grass-stvds-tar-gz'}, {'mimeType': 'application/x-grass-stvds-tar-bzip'}])
    self.addLiteralInput(identifier = 'intype', title = 'Type of the input space time dataset', minOccurs = 0, maxOccurs = 1, type = type("string"), default = "strds", allowedValues = ['strds', 'stvds', 'str3ds'])
    self.addLiteralInput(identifier = 'samtype', title = 'Type of the sample space time dataset', minOccurs = 0, maxOccurs = 1, type = type("string"), default = "strds", allowedValues = ['strds', 'stvds', 'str3ds'])
    self.addLiteralInput(identifier = 'method', title = 'The method to be used for sampling the input dataset', minOccurs = 0, maxOccurs = 1024, type = type("string"), default = "during,overlap,contain,equal", allowedValues = ['start', 'during', 'overlap', 'contain', 'equal', 'follows', 'precedes'])
    self.addLiteralInput(identifier = 'fs', title = 'Field separator character between the output columns, default is tabular " | ". Do not use "," as this char is reserved to list several map ids in a sample granule', minOccurs = 0, maxOccurs = 1, type = type("string"), allowedValues = '*')
    self.addLiteralInput(identifier = '-c', title = 'Print column names', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])
    self.addLiteralInput(identifier = '-s', title = 'Check spatial overlap to perform spatio-temporal sampling', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])

    # complex outputs
    self.addComplexOutput(identifier = 'stdout', title = 'Module output on stdout', abstract = 'The output of the module written to stdout', formats = [{'mimeType': 'text/plain'}])

  def execute(self):
    starter = PyWPSGrassModuleStarter()
    starter.fromPyWPS("t.sample", self.inputs, self.outputs, self.pywps)

if __name__ == "__main__":
  process = t_sample()
  process.execute()
