# ################################################ #
# This process was generated using GrassXMLtoPyWPS #
# Author: Soeren Gebbert                           #
# Mail: soerengebbert <at> googlemail <dot> com    #
# ################################################ #

from pywps.Process import WPSProcess

from PyWPSGrassModuleStarter import PyWPSGrassModuleStarter

class r_resamp_filter(WPSProcess):

  def __init__(self):
    WPSProcess.__init__(self, identifier = 'r.resamp.filter', title = 'Resamples raster map layers using an analytic kernel.', version = 1, statusSupported = True, storeSupported = True, metadata = [{'type': 'simple', 'title': 'raster'}, {'type': 'simple', 'title': 'resample'}], abstract = 'http://grass.osgeo.org/grass70/manuals/html70_user/r.resamp.filter.html')

    # Literal and complex inputs
    self.addComplexInput(identifier = 'input', title = 'Name of input raster map', minOccurs = 1, maxOccurs = 1, formats = [{'mimeType': 'image/tiff'}, {'mimeType': 'image/geotiff'}, {'mimeType': 'application/geotiff'}, {'mimeType': 'application/x-geotiff'}, {'mimeType': 'image/png'}, {'mimeType': 'image/gif'}, {'mimeType': 'image/jpeg'}, {'mimeType': 'application/x-erdas-hfa'}, {'mimeType': 'application/netcdf'}, {'mimeType': 'application/x-netcdf'}])
    self.addLiteralInput(identifier = 'filter', title = 'Filter kernel(s)', minOccurs = 1, maxOccurs = 1024, type = type("string"), allowedValues = ['box', 'bartlett', 'gauss', 'normal', 'hermite', 'sinc', 'lanczos1', 'lanczos2', 'lanczos3', 'hann', 'hamming', 'blackman'])
    self.addLiteralInput(identifier = 'radius', title = 'Filter radius', minOccurs = 0, maxOccurs = 1024, type = type(0.0), allowedValues = '*')
    self.addLiteralInput(identifier = 'x_radius', title = 'Filter radius (horizontal)', minOccurs = 0, maxOccurs = 1024, type = type(0.0), allowedValues = '*')
    self.addLiteralInput(identifier = 'y_radius', title = 'Filter radius (vertical)', minOccurs = 0, maxOccurs = 1024, type = type(0.0), allowedValues = '*')
    self.addLiteralInput(identifier = '-n', title = 'Propagate NULLs', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])
    self.addLiteralInput(identifier = 'grass_resolution_ns', title = 'Resolution of the mapset in north-south direction in meters or degrees', abstract = 'This parameter defines the north-south resolution of the mapset in meter or degrees, which should be used to process the input and output raster data. To enable this setting, you need to specify north-south and east-west resolution.', minOccurs = 0, maxOccurs = 1, type = type(0.0), allowedValues = '*')
    self.addLiteralInput(identifier = 'grass_resolution_ew', title = 'Resolution of the mapset in east-west direction in meters or degrees', abstract = 'This parameter defines the east-west resolution of the mapset in meters or degrees, which should be used to process the input and output raster data.  To enable this setting, you need to specify north-south and east-west resolution.', minOccurs = 0, maxOccurs = 1, type = type(0.0), allowedValues = '*')
    self.addLiteralInput(identifier = 'grass_band_number', title = 'Band to select for processing (default is all bands)', abstract = 'This parameter defines band number of the input raster files which should be processed. As default all bands are processed and used as single and multiple inputs for raster modules.', minOccurs = 0, maxOccurs = 1, type = type(0), allowedValues = '*')

    # complex outputs
    self.addComplexOutput(identifier = 'output', title = 'Name for output raster map', formats = [{'mimeType': 'image/tiff'}, {'mimeType': 'image/geotiff'}, {'mimeType': 'application/geotiff'}, {'mimeType': 'application/x-geotiff'}, {'mimeType': 'application/x-erdas-hfa'}, {'mimeType': 'application/netcdf'}, {'mimeType': 'application/x-netcdf'}])

  def execute(self):
    starter = PyWPSGrassModuleStarter()
    starter.fromPyWPS("r.resamp.filter", self.inputs, self.outputs, self.pywps)

if __name__ == "__main__":
  process = r_resamp_filter()
  process.execute()
