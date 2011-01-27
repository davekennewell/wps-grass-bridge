# ################################################ #
# This process was generated using GrassXMLtoPyWPS #
# Author: Soeren Gebbert                           #
# Mail: soerengebbert <at> googlemail <dot> com    #
# ################################################ #

from pywps.Process import WPSProcess

from PyWPSGrassModuleStarter import PyWPSGrassModuleStarter

class r_shaded_relief(WPSProcess):

  def __init__(self):
    WPSProcess.__init__(self, identifier = 'r.shaded.relief', title = 'Creates shaded relief map from an elevation map (DEM).', version = 1, statusSupported = True, storeSupported = True, metadata = [{'type': 'simple', 'title': 'raster'}], abstract = 'http://grass.osgeo.org/grass70/manuals/html70_user/r.shaded.relief.html')

    # Literal and complex inputs
    self.addComplexInput(identifier = 'input', title = 'Name of input elevation map', minOccurs = 1, maxOccurs = 1, formats = [{'mimeType': 'image/tiff'}, {'mimeType': 'image/geotiff'}, {'mimeType': 'application/geotiff'}, {'mimeType': 'application/x-geotiff'}, {'mimeType': 'image/png'}, {'mimeType': 'image/gif'}, {'mimeType': 'image/jpeg'}, {'mimeType': 'application/x-erdas-hfa'}, {'mimeType': 'application/netcdf'}, {'mimeType': 'application/x-netcdf'}])
    self.addLiteralInput(identifier = 'altitude', title = 'Altitude of the sun in degrees above the horizon', minOccurs = 0, maxOccurs = 1, type = type(0.0), default = 30.0)
    self.addLiteralInput(identifier = 'azimuth', title = 'Azimuth of the sun in degrees to the east of north', minOccurs = 0, maxOccurs = 1, type = type(0.0), default = 270.0)
    self.addLiteralInput(identifier = 'zmult', title = 'Factor for exaggerating relief', minOccurs = 0, maxOccurs = 1, type = type(0.0), default = 1.0)
    self.addLiteralInput(identifier = 'scale', title = 'Scale factor for converting horizontal units to elevation units', minOccurs = 0, maxOccurs = 1, type = type(0.0), default = 1.0)
    self.addLiteralInput(identifier = 'units', title = 'Set scaling factor (applies to lat./long. locations only, none: scale=1)', minOccurs = 0, maxOccurs = 1, type = type("string"), default = "none", allowedValues = ['none', 'meters', 'feet'])
    self.addLiteralInput(identifier = 'grass_resolution_ns', title = 'Resolution of the mapset in north-south direction in meters or degrees', abstract = 'This parameter defines the north-south resolution of the mapset in meter or degrees, which should be used to process the input and output raster data. To enable this setting, you need to specify north-south and east-west resolution.', minOccurs = 0, maxOccurs = 1, type = type(0.0), allowedValues = '*')
    self.addLiteralInput(identifier = 'grass_resolution_ew', title = 'Resolution of the mapset in east-west direction in meters or degrees', abstract = 'This parameter defines the east-west resolution of the mapset in meters or degrees, which should be used to process the input and output raster data.  To enable this setting, you need to specify north-south and east-west resolution.', minOccurs = 0, maxOccurs = 1, type = type(0.0), allowedValues = '*')
    self.addLiteralInput(identifier = 'grass_band_number', title = 'Band to select for processing (default is all bands)', abstract = 'This parameter defines band number of the input raster files which should be processed. As default all bands are processed and used as single and multiple inputs for raster modules.', minOccurs = 0, maxOccurs = 1, type = type(0), allowedValues = '*')

    # complex outputs
    self.addComplexOutput(identifier = 'output', title = 'Name for output shaded relief map', formats = [{'mimeType': 'image/tiff'}, {'mimeType': 'image/geotiff'}, {'mimeType': 'application/geotiff'}, {'mimeType': 'application/x-geotiff'}, {'mimeType': 'application/x-erdas-hfa'}, {'mimeType': 'application/netcdf'}, {'mimeType': 'application/x-netcdf'}])

  def execute(self):
    starter = PyWPSGrassModuleStarter()
    starter.fromPyWPS("r.shaded.relief", self.inputs, self.outputs, self.pywps)

if __name__ == "__main__":
  process = r_shaded_relief()
  process.execute()
