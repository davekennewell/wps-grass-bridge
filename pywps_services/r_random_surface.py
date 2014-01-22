# ################################################ #
# This process was generated using GrassXMLtoPyWPS #
# Author: Soeren Gebbert                           #
# Mail: soerengebbert <at> googlemail <dot> com    #
# ################################################ #

from pywps.Process import WPSProcess

from PyWPSGrassModuleStarter import PyWPSGrassModuleStarter

class r_random_surface(WPSProcess):

  def __init__(self):
    WPSProcess.__init__(self, identifier = 'r.random.surface', title = 'Generates random surface(s) with spatial dependence.', version = 1, statusSupported = True, storeSupported = True, metadata = [{'type': 'simple', 'title': 'raster'}, {'type': 'simple', 'title': 'surface'}, {'type': 'simple', 'title': 'random'}], abstract = 'http://grass.osgeo.org/grass70/manuals/html70_user/r.random.surface.html')

    # Literal and complex inputs
    self.addLiteralInput(identifier = 'distance', title = 'Maximum distance of spatial correlation (value &#62;= 0.0)', minOccurs = 0, maxOccurs = 1, type = type(0.0), default = 0.0)
    self.addLiteralInput(identifier = 'exponent', title = 'Distance decay exponent (value &#62; 0.0)', minOccurs = 0, maxOccurs = 1, type = type(0.0), default = 1.0)
    self.addLiteralInput(identifier = 'flat', title = 'Distance filter remains flat before beginning exponent', minOccurs = 0, maxOccurs = 1, type = type(0.0), default = 0.0)
    self.addLiteralInput(identifier = 'seed', title = 'Random seed (SEED_MIN &#62;= value &#62;= SEED_MAX), default [random]', minOccurs = 0, maxOccurs = 1, type = type(0), allowedValues = '*')
    self.addLiteralInput(identifier = 'high', title = 'Maximum cell value of distribution', minOccurs = 0, maxOccurs = 1, type = type(0), default = 255)
    self.addLiteralInput(identifier = '-u', title = 'Uniformly distributed cell values', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])
    self.addLiteralInput(identifier = 'grass_resolution_ns', title = 'Resolution of the mapset in north-south direction in meters or degrees', abstract = 'This parameter defines the north-south resolution of the mapset in meter or degrees, which should be used to process the input and output raster data. To enable this setting, you need to specify north-south and east-west resolution.', minOccurs = 0, maxOccurs = 1, type = type(0.0), allowedValues = '*')
    self.addLiteralInput(identifier = 'grass_resolution_ew', title = 'Resolution of the mapset in east-west direction in meters or degrees', abstract = 'This parameter defines the east-west resolution of the mapset in meters or degrees, which should be used to process the input and output raster data.  To enable this setting, you need to specify north-south and east-west resolution.', minOccurs = 0, maxOccurs = 1, type = type(0.0), allowedValues = '*')

    # complex outputs
    self.addComplexOutput(identifier = 'output', title = 'Name for output raster map(s)', formats = [{'mimeType': 'image/tiff'}, {'mimeType': 'image/geotiff'}, {'mimeType': 'application/geotiff'}, {'mimeType': 'application/x-geotiff'}, {'mimeType': 'application/x-erdas-hfa'}, {'mimeType': 'application/netcdf'}, {'mimeType': 'application/x-netcdf'}])

  def execute(self):
    starter = PyWPSGrassModuleStarter()
    starter.fromPyWPS("r.random.surface", self.inputs, self.outputs, self.pywps)

if __name__ == "__main__":
  process = r_random_surface()
  process.execute()
