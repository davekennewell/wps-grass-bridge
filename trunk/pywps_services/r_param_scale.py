# ################################################ #
# This process was generated using GrassXMLtoPyWPS #
# Author: Soeren Gebbert                           #
# Mail: soerengebbert <at> googlemail <dot> com    #
# ################################################ #

from pywps.Process import WPSProcess

from PyWPSGrassModuleStarter import PyWPSGrassModuleStarter

class r_param_scale(WPSProcess):

  def __init__(self):
    WPSProcess.__init__(self, identifier = 'r.param.scale', title = 'Uses a multi-scale approach by taking fitting quadratic parameters to any size window (via least squares).', version = 1, statusSupported = True, storeSupported = True, metadata = [{'type': 'simple', 'title': 'raster'}, {'type': 'simple', 'title': 'geomorphology'}], abstract = 'http://grass.osgeo.org/grass70/manuals/html70_user/r.param.scale.html')

    # Literal and complex inputs
    self.addComplexInput(identifier = 'input', title = 'Name of input raster map', minOccurs = 1, maxOccurs = 1, formats = [{'mimeType': 'image/tiff'}, {'mimeType': 'image/geotiff'}, {'mimeType': 'application/geotiff'}, {'mimeType': 'application/x-geotiff'}, {'mimeType': 'image/png'}, {'mimeType': 'image/gif'}, {'mimeType': 'image/jpeg'}, {'mimeType': 'application/x-erdas-hfa'}, {'mimeType': 'application/netcdf'}, {'mimeType': 'application/x-netcdf'}])
    self.addLiteralInput(identifier = 's_tol', title = 'Slope tolerance that defines a flat surface (degrees)', minOccurs = 0, maxOccurs = 1, type = type(0.0), default = 1.0)
    self.addLiteralInput(identifier = 'c_tol', title = 'Curvature tolerance that defines planar surface', minOccurs = 0, maxOccurs = 1, type = type(0.0), default = 0.0001)
    self.addLiteralInput(identifier = 'size', title = 'Size of processing window (odd number only, max: 69)', minOccurs = 0, maxOccurs = 1, type = type(0), default = 3)
    self.addLiteralInput(identifier = 'param', title = 'Morphometric parameter in size window to calculate', minOccurs = 0, maxOccurs = 1, type = type("string"), default = "elev", allowedValues = ['elev', 'slope', 'aspect', 'profc', 'planc', 'longc', 'crosc', 'minic', 'maxic', 'feature'])
    self.addLiteralInput(identifier = 'exp', title = 'Exponent for distance weighting (0.0-4.0)', minOccurs = 0, maxOccurs = 1, type = type(0.0), default = 0.0)
    self.addLiteralInput(identifier = 'zscale', title = 'Vertical scaling factor', minOccurs = 0, maxOccurs = 1, type = type(0.0), default = 1.0)
    self.addLiteralInput(identifier = '-c', title = 'Constrain model through central window cell', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])
    self.addLiteralInput(identifier = 'grass_resolution_ns', title = 'Resolution of the mapset in north-south direction in meters or degrees', abstract = 'This parameter defines the north-south resolution of the mapset in meter or degrees, which should be used to process the input and output raster data. To enable this setting, you need to specify north-south and east-west resolution.', minOccurs = 0, maxOccurs = 1, type = type(0.0), allowedValues = '*')
    self.addLiteralInput(identifier = 'grass_resolution_ew', title = 'Resolution of the mapset in east-west direction in meters or degrees', abstract = 'This parameter defines the east-west resolution of the mapset in meters or degrees, which should be used to process the input and output raster data.  To enable this setting, you need to specify north-south and east-west resolution.', minOccurs = 0, maxOccurs = 1, type = type(0.0), allowedValues = '*')
    self.addLiteralInput(identifier = 'grass_band_number', title = 'Band to select for processing (default is all bands)', abstract = 'This parameter defines band number of the input raster files which should be processed. As default all bands are processed and used as single and multiple inputs for raster modules.', minOccurs = 0, maxOccurs = 1, type = type(0), allowedValues = '*')

    # complex outputs
    self.addComplexOutput(identifier = 'output', title = 'Output raster layer containing morphometric parameter', formats = [{'mimeType': 'image/tiff'}, {'mimeType': 'image/geotiff'}, {'mimeType': 'application/geotiff'}, {'mimeType': 'application/x-geotiff'}, {'mimeType': 'application/x-erdas-hfa'}, {'mimeType': 'application/netcdf'}, {'mimeType': 'application/x-netcdf'}])

  def execute(self):
    starter = PyWPSGrassModuleStarter()
    starter.fromPyWPS("r.param.scale", self.inputs, self.outputs, self.pywps)

if __name__ == "__main__":
  process = r_param_scale()
  process.execute()
