# ################################################ #
# This process was generated using GrassXMLtoPyWPS #
# Author: Soeren Gebbert                           #
# Mail: soerengebbert <at> googlemail <dot> com    #
# ################################################ #

from pywps.Process import WPSProcess

from PyWPSGrassModuleStarter import PyWPSGrassModuleStarter

class r_univar(WPSProcess):

  def __init__(self):
    WPSProcess.__init__(self, identifier = 'r.univar', title = 'Calculates univariate statistics from the non-null cells of a raster map.', version = 1, statusSupported = True, storeSupported = True, metadata = [{'type': 'simple', 'title': 'raster'}, {'type': 'simple', 'title': 'statistics'}, {'type': 'simple', 'title': 'univariate statistics'}, {'type': 'simple', 'title': 'zonal statistics'}], abstract = 'http://grass.osgeo.org/grass70/manuals/html70_user/r.univar.html')

    # Literal and complex inputs
    self.addComplexInput(identifier = 'map', title = 'Name of raster map(s)', minOccurs = 1, maxOccurs = 1024, formats = [{'mimeType': 'image/tiff'}, {'mimeType': 'image/geotiff'}, {'mimeType': 'application/geotiff'}, {'mimeType': 'application/x-geotiff'}, {'mimeType': 'image/png'}, {'mimeType': 'image/gif'}, {'mimeType': 'image/jpeg'}, {'mimeType': 'application/x-erdas-hfa'}, {'mimeType': 'application/netcdf'}, {'mimeType': 'application/x-netcdf'}])
    self.addComplexInput(identifier = 'zones', title = 'Raster map used for zoning, must be of type CELL', minOccurs = 0, maxOccurs = 1, formats = [{'mimeType': 'image/tiff'}, {'mimeType': 'image/geotiff'}, {'mimeType': 'application/geotiff'}, {'mimeType': 'application/x-geotiff'}, {'mimeType': 'image/png'}, {'mimeType': 'image/gif'}, {'mimeType': 'image/jpeg'}, {'mimeType': 'application/x-erdas-hfa'}, {'mimeType': 'application/netcdf'}, {'mimeType': 'application/x-netcdf'}])
    self.addLiteralInput(identifier = 'percentile', title = 'Percentile to calculate (requires extended statistics flag)', minOccurs = 0, maxOccurs = 1024, type = type(0.0), default = 90.0)
    self.addLiteralInput(identifier = 'separator', title = 'Field separator', abstract = 'Special characters: newline, space, comma, tab', minOccurs = 0, maxOccurs = 1, type = type("string"), default = "|")
    self.addLiteralInput(identifier = '-g', title = 'Print the stats in shell script style', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])
    self.addLiteralInput(identifier = '-e', title = 'Calculate extended statistics', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])
    self.addLiteralInput(identifier = '-t', title = 'Table output format instead of standard output format', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])
    self.addLiteralInput(identifier = 'grass_resolution_ns', title = 'Resolution of the mapset in north-south direction in meters or degrees', abstract = 'This parameter defines the north-south resolution of the mapset in meter or degrees, which should be used to process the input and output raster data. To enable this setting, you need to specify north-south and east-west resolution.', minOccurs = 0, maxOccurs = 1, type = type(0.0), allowedValues = '*')
    self.addLiteralInput(identifier = 'grass_resolution_ew', title = 'Resolution of the mapset in east-west direction in meters or degrees', abstract = 'This parameter defines the east-west resolution of the mapset in meters or degrees, which should be used to process the input and output raster data.  To enable this setting, you need to specify north-south and east-west resolution.', minOccurs = 0, maxOccurs = 1, type = type(0.0), allowedValues = '*')
    self.addLiteralInput(identifier = 'grass_band_number', title = 'Band to select for processing (default is all bands)', abstract = 'This parameter defines band number of the input raster files which should be processed. As default all bands are processed and used as single and multiple inputs for raster modules.', minOccurs = 0, maxOccurs = 1, type = type(0), allowedValues = '*')

    # complex outputs
    self.addComplexOutput(identifier = 'output', title = 'Name for output file (if omitted or "-" output to stdout)', formats = [{'mimeType': 'text/plain'}])

  def execute(self):
    starter = PyWPSGrassModuleStarter()
    starter.fromPyWPS("r.univar", self.inputs, self.outputs, self.pywps)

if __name__ == "__main__":
  process = r_univar()
  process.execute()
