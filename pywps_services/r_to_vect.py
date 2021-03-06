# ################################################ #
# This process was generated using GrassXMLtoPyWPS #
# Author: Soeren Gebbert                           #
# Mail: soerengebbert <at> googlemail <dot> com    #
# ################################################ #

from pywps.Process import WPSProcess

from PyWPSGrassModuleStarter import PyWPSGrassModuleStarter

class r_to_vect(WPSProcess):

  def __init__(self):
    WPSProcess.__init__(self, identifier = 'r.to.vect', title = 'Converts a raster map into a vector map.', version = 1, statusSupported = True, storeSupported = True, metadata = [{'type': 'simple', 'title': 'raster'}, {'type': 'simple', 'title': 'conversion'}, {'type': 'simple', 'title': 'geometry'}, {'type': 'simple', 'title': 'vectorization'}], abstract = 'http://grass.osgeo.org/grass70/manuals/html70_user/r.to.vect.html')

    # Literal and complex inputs
    self.addComplexInput(identifier = 'input', title = 'Name of input raster map', minOccurs = 1, maxOccurs = 1, formats = [{'mimeType': 'image/tiff'}, {'mimeType': 'image/geotiff'}, {'mimeType': 'application/geotiff'}, {'mimeType': 'application/x-geotiff'}, {'mimeType': 'image/png'}, {'mimeType': 'image/gif'}, {'mimeType': 'image/jpeg'}, {'mimeType': 'application/x-erdas-hfa'}, {'mimeType': 'application/netcdf'}, {'mimeType': 'application/x-netcdf'}])
    self.addLiteralInput(identifier = 'type', title = 'Feature type', minOccurs = 1, maxOccurs = 1, type = type("string"), allowedValues = ['point', 'line', 'area'])
    self.addLiteralInput(identifier = 'column', title = 'Name of attribute column to store value', abstract = 'Name must be SQL compliant', minOccurs = 0, maxOccurs = 1, type = type("string"), default = "value")
    self.addLiteralInput(identifier = '-s', title = 'Smooth corners of area features', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])
    self.addLiteralInput(identifier = '-v', title = 'Use raster values as categories instead of unique sequence (CELL only)', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])
    self.addLiteralInput(identifier = '-z', title = 'Table is not created. Currently supported only for points.', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])
    self.addLiteralInput(identifier = '-b', title = 'Recommended for massive point conversion', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])
    self.addLiteralInput(identifier = '-t', title = 'Do not create attribute table', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])
    self.addLiteralInput(identifier = 'grass_resolution_ns', title = 'Resolution of the mapset in north-south direction in meters or degrees', abstract = 'This parameter defines the north-south resolution of the mapset in meter or degrees, which should be used to process the input and output raster data. To enable this setting, you need to specify north-south and east-west resolution.', minOccurs = 0, maxOccurs = 1, type = type(0.0), allowedValues = '*')
    self.addLiteralInput(identifier = 'grass_resolution_ew', title = 'Resolution of the mapset in east-west direction in meters or degrees', abstract = 'This parameter defines the east-west resolution of the mapset in meters or degrees, which should be used to process the input and output raster data.  To enable this setting, you need to specify north-south and east-west resolution.', minOccurs = 0, maxOccurs = 1, type = type(0.0), allowedValues = '*')
    self.addLiteralInput(identifier = 'grass_band_number', title = 'Band to select for processing (default is all bands)', abstract = 'This parameter defines band number of the input raster files which should be processed. As default all bands are processed and used as single and multiple inputs for raster modules.', minOccurs = 0, maxOccurs = 1, type = type(0), allowedValues = '*')

    # complex outputs
    self.addComplexOutput(identifier = 'output', title = 'Name for output vector map', formats = [{'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/3.1.1/base/gml.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/xml', 'schema': 'http://schemas.opengis.net/gml/3.1.1/base/gml.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/kml/2.2.0/ogckml22.xsd', 'encoding': 'UTF-8'}])

  def execute(self):
    starter = PyWPSGrassModuleStarter()
    starter.fromPyWPS("r.to.vect", self.inputs, self.outputs, self.pywps)

if __name__ == "__main__":
  process = r_to_vect()
  process.execute()
