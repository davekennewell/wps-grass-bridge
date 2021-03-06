# ################################################ #
# This process was generated using GrassXMLtoPyWPS #
# Author: Soeren Gebbert                           #
# Mail: soerengebbert <at> googlemail <dot> com    #
# ################################################ #

from pywps.Process import WPSProcess

from PyWPSGrassModuleStarter import PyWPSGrassModuleStarter

class r_stats(WPSProcess):

  def __init__(self):
    WPSProcess.__init__(self, identifier = 'r.stats', title = 'Generates area statistics for raster map.', version = 1, statusSupported = True, storeSupported = True, metadata = [{'type': 'simple', 'title': 'raster'}, {'type': 'simple', 'title': 'statistics'}], abstract = 'http://grass.osgeo.org/grass70/manuals/html70_user/r.stats.html')

    # Literal and complex inputs
    self.addComplexInput(identifier = 'input', title = 'Name of raster map(s) to report on', minOccurs = 1, maxOccurs = 1024, formats = [{'mimeType': 'image/tiff'}, {'mimeType': 'image/geotiff'}, {'mimeType': 'application/geotiff'}, {'mimeType': 'application/x-geotiff'}, {'mimeType': 'image/png'}, {'mimeType': 'image/gif'}, {'mimeType': 'image/jpeg'}, {'mimeType': 'application/x-erdas-hfa'}, {'mimeType': 'application/netcdf'}, {'mimeType': 'application/x-netcdf'}])
    self.addLiteralInput(identifier = 'separator', title = 'Field separator', abstract = 'Special characters: newline, space, comma, tab', minOccurs = 0, maxOccurs = 1, type = type("string"), default = "space")
    self.addLiteralInput(identifier = 'nv', title = 'String representing no data cell value', minOccurs = 0, maxOccurs = 1, type = type("string"), default = "*")
    self.addLiteralInput(identifier = 'nsteps', title = 'Number of floating-point subranges to collect stats from', minOccurs = 0, maxOccurs = 1, type = type(0), default = 255)
    self.addLiteralInput(identifier = 'sort', title = 'Sort output statistics by cell counts', abstract = 'Default: sorted by categories or intervals', minOccurs = 0, maxOccurs = 1, type = type("string"), allowedValues = ['asc', 'desc'])
    self.addLiteralInput(identifier = '-a', title = 'Print area totals in square meters', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])
    self.addLiteralInput(identifier = '-c', title = 'Print cell counts (sortable)', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])
    self.addLiteralInput(identifier = '-p', title = 'Print approximate (total percent may not be 100%) percents', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])
    self.addLiteralInput(identifier = '-l', title = 'Print category labels', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])
    self.addLiteralInput(identifier = '-1', title = 'One cell (range) per line', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])
    self.addLiteralInput(identifier = '-g', title = 'Print grid coordinates (east and north)', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])
    self.addLiteralInput(identifier = '-x', title = 'Print x and y (column and row)', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])
    self.addLiteralInput(identifier = '-A', title = 'Print averaged values instead of intervals (floating-point maps only)', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])
    self.addLiteralInput(identifier = '-r', title = 'Print raw indexes of floating-point ranges (floating-point maps only)', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])
    self.addLiteralInput(identifier = '-n', title = 'Do not report no data value', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])
    self.addLiteralInput(identifier = '-N', title = 'Do not report cells where all maps have no data', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])
    self.addLiteralInput(identifier = '-C', title = 'Report for cats floating-point ranges (floating-point maps only)', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])
    self.addLiteralInput(identifier = '-i', title = 'Read floating-point map as integer (use maps quant rules)', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])
    self.addLiteralInput(identifier = 'grass_resolution_ns', title = 'Resolution of the mapset in north-south direction in meters or degrees', abstract = 'This parameter defines the north-south resolution of the mapset in meter or degrees, which should be used to process the input and output raster data. To enable this setting, you need to specify north-south and east-west resolution.', minOccurs = 0, maxOccurs = 1, type = type(0.0), allowedValues = '*')
    self.addLiteralInput(identifier = 'grass_resolution_ew', title = 'Resolution of the mapset in east-west direction in meters or degrees', abstract = 'This parameter defines the east-west resolution of the mapset in meters or degrees, which should be used to process the input and output raster data.  To enable this setting, you need to specify north-south and east-west resolution.', minOccurs = 0, maxOccurs = 1, type = type(0.0), allowedValues = '*')
    self.addLiteralInput(identifier = 'grass_band_number', title = 'Band to select for processing (default is all bands)', abstract = 'This parameter defines band number of the input raster files which should be processed. As default all bands are processed and used as single and multiple inputs for raster modules.', minOccurs = 0, maxOccurs = 1, type = type(0), allowedValues = '*')

    # complex outputs
    self.addComplexOutput(identifier = 'output', title = 'Name for output file (if omitted or "-" output to stdout)', formats = [{'mimeType': 'text/plain'}])

  def execute(self):
    starter = PyWPSGrassModuleStarter()
    starter.fromPyWPS("r.stats", self.inputs, self.outputs, self.pywps)

if __name__ == "__main__":
  process = r_stats()
  process.execute()
