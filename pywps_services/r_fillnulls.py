# ################################################ #
# This process was generated using GrassXMLtoPyWPS #
# Author: Soeren Gebbert                           #
# Mail: soerengebbert <at> googlemail <dot> com    #
# ################################################ #

from pywps.Process import WPSProcess

from PyWPSGrassModuleStarter import PyWPSGrassModuleStarter

class r_fillnulls(WPSProcess):

  def __init__(self):
    WPSProcess.__init__(self, identifier = 'r.fillnulls', title = 'Fills no-data areas in raster maps using spline interpolation.', version = 1, statusSupported = True, storeSupported = True, metadata = [{'type': 'simple', 'title': 'raster'}, {'type': 'simple', 'title': 'elevation'}, {'type': 'simple', 'title': 'interpolation'}], abstract = 'http://grass.osgeo.org/grass70/manuals/html70_user/r.fillnulls.html')

    # Literal and complex inputs
    self.addComplexInput(identifier = 'input', title = 'Name of input raster map', minOccurs = 1, maxOccurs = 1, formats = [{'mimeType': 'image/tiff'}, {'mimeType': 'image/geotiff'}, {'mimeType': 'application/geotiff'}, {'mimeType': 'application/x-geotiff'}, {'mimeType': 'image/png'}, {'mimeType': 'image/gif'}, {'mimeType': 'image/jpeg'}, {'mimeType': 'application/x-erdas-hfa'}, {'mimeType': 'application/netcdf'}, {'mimeType': 'application/x-netcdf'}])
    self.addLiteralInput(identifier = 'method', title = 'Interpolation method', minOccurs = 1, maxOccurs = 1, type = type("string"), default = "rst", allowedValues = ['linear', 'cubic', 'rst'])
    self.addLiteralInput(identifier = 'tension', title = 'Spline tension parameter', minOccurs = 0, maxOccurs = 1, type = type(0.0), default = 40.0)
    self.addLiteralInput(identifier = 'smooth', title = 'Spline smoothing parameter', minOccurs = 0, maxOccurs = 1, type = type(0.0), default = 0.1)
    self.addLiteralInput(identifier = 'edge', title = 'Width of hole edge used for interpolation (in cells)', minOccurs = 0, maxOccurs = 1, type = type(0), default = 3)
    self.addLiteralInput(identifier = 'npmin', title = 'Minimum number of points for approximation in a segment (&#62;segmax)', minOccurs = 0, maxOccurs = 1, type = type(0), default = 600)
    self.addLiteralInput(identifier = 'segmax', title = 'Maximum number of points in a segment', minOccurs = 0, maxOccurs = 1, type = type(0), default = 300)
    self.addLiteralInput(identifier = 'grass_resolution_ns', title = 'Resolution of the mapset in north-south direction in meters or degrees', abstract = 'This parameter defines the north-south resolution of the mapset in meter or degrees, which should be used to process the input and output raster data. To enable this setting, you need to specify north-south and east-west resolution.', minOccurs = 0, maxOccurs = 1, type = type(0.0), allowedValues = '*')
    self.addLiteralInput(identifier = 'grass_resolution_ew', title = 'Resolution of the mapset in east-west direction in meters or degrees', abstract = 'This parameter defines the east-west resolution of the mapset in meters or degrees, which should be used to process the input and output raster data.  To enable this setting, you need to specify north-south and east-west resolution.', minOccurs = 0, maxOccurs = 1, type = type(0.0), allowedValues = '*')
    self.addLiteralInput(identifier = 'grass_band_number', title = 'Band to select for processing (default is all bands)', abstract = 'This parameter defines band number of the input raster files which should be processed. As default all bands are processed and used as single and multiple inputs for raster modules.', minOccurs = 0, maxOccurs = 1, type = type(0), allowedValues = '*')

    # complex outputs
    self.addComplexOutput(identifier = 'output', title = 'Name for output raster map', formats = [{'mimeType': 'image/tiff'}, {'mimeType': 'image/geotiff'}, {'mimeType': 'application/geotiff'}, {'mimeType': 'application/x-geotiff'}, {'mimeType': 'application/x-erdas-hfa'}, {'mimeType': 'application/netcdf'}, {'mimeType': 'application/x-netcdf'}])

  def execute(self):
    starter = PyWPSGrassModuleStarter()
    starter.fromPyWPS("r.fillnulls", self.inputs, self.outputs, self.pywps)

if __name__ == "__main__":
  process = r_fillnulls()
  process.execute()
