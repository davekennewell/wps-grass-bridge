# ################################################ #
# This process was generated using GrassXMLtoPyWPS #
# Author: Soeren Gebbert                           #
# Mail: soerengebbert <at> googlemail <dot> com    #
# ################################################ #

from pywps.Process import WPSProcess

from PyWPSGrassModuleStarter import PyWPSGrassModuleStarter

class r_surf_fractal(WPSProcess):

  def __init__(self):
    WPSProcess.__init__(self, identifier = 'r.surf.fractal', title = 'Creates a fractal surface of a given fractal dimension.', version = 1, statusSupported = True, storeSupported = True, metadata = [{'type': 'simple', 'title': 'raster'}, {'type': 'simple', 'title': 'surface'}, {'type': 'simple', 'title': 'fractal'}], abstract = 'http://grass.osgeo.org/grass70/manuals/html70_user/r.surf.fractal.html')

    # Literal and complex inputs
    self.addLiteralInput(identifier = 'dimension', title = 'Fractal dimension of surface (2 &#60; D &#60; 3)', minOccurs = 0, maxOccurs = 1, type = type(0.0), default = 2.05)
    self.addLiteralInput(identifier = 'number', title = 'Number of intermediate images to produce', minOccurs = 0, maxOccurs = 1, type = type(0), default = 0)
    self.addLiteralInput(identifier = 'grass_resolution_ns', title = 'Resolution of the mapset in north-south direction in meters or degrees', abstract = 'This parameter defines the north-south resolution of the mapset in meter or degrees, which should be used to process the input and output raster data. To enable this setting, you need to specify north-south and east-west resolution.', minOccurs = 0, maxOccurs = 1, type = type(0.0), allowedValues = '*')
    self.addLiteralInput(identifier = 'grass_resolution_ew', title = 'Resolution of the mapset in east-west direction in meters or degrees', abstract = 'This parameter defines the east-west resolution of the mapset in meters or degrees, which should be used to process the input and output raster data.  To enable this setting, you need to specify north-south and east-west resolution.', minOccurs = 0, maxOccurs = 1, type = type(0.0), allowedValues = '*')

    # complex outputs
    self.addComplexOutput(identifier = 'output', title = 'Name for output raster map', formats = [{'mimeType': 'image/tiff'}, {'mimeType': 'image/geotiff'}, {'mimeType': 'application/geotiff'}, {'mimeType': 'application/x-geotiff'}, {'mimeType': 'application/x-erdas-hfa'}, {'mimeType': 'application/netcdf'}, {'mimeType': 'application/x-netcdf'}])

  def execute(self):
    starter = PyWPSGrassModuleStarter()
    starter.fromPyWPS("r.surf.fractal", self.inputs, self.outputs, self.pywps)

if __name__ == "__main__":
  process = r_surf_fractal()
  process.execute()
