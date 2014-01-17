# ################################################ #
# This process was generated using GrassXMLtoPyWPS #
# Author: Soeren Gebbert                           #
# Mail: soerengebbert <at> googlemail <dot> com    #
# ################################################ #

from pywps.Process import WPSProcess

from PyWPSGrassModuleStarter import PyWPSGrassModuleStarter

class r_volume(WPSProcess):

  def __init__(self):
    WPSProcess.__init__(self, identifier = 'r.volume', title = 'Optionally produces a GRASS vector points map containing the calculated centroids of these clumps.', version = 1, statusSupported = True, storeSupported = True, metadata = [{'type': 'simple', 'title': 'raster'}, {'type': 'simple', 'title': 'volume'}, {'type': 'simple', 'title': 'clumps'}], abstract = 'http://grass.osgeo.org/grass70/manuals/html70_user/r.volume.html')

    # Literal and complex inputs
    self.addComplexInput(identifier = 'input', title = 'Name of input raster map representing data that will be summed within clumps', minOccurs = 1, maxOccurs = 1, formats = [{'mimeType': 'image/tiff'}, {'mimeType': 'image/geotiff'}, {'mimeType': 'application/geotiff'}, {'mimeType': 'application/x-geotiff'}, {'mimeType': 'image/png'}, {'mimeType': 'image/gif'}, {'mimeType': 'image/jpeg'}, {'mimeType': 'application/x-erdas-hfa'}, {'mimeType': 'application/netcdf'}, {'mimeType': 'application/x-netcdf'}])
    self.addComplexInput(identifier = 'clump', title = 'Preferably the output of r.clump. If no clump map is given than MASK is used.', minOccurs = 0, maxOccurs = 1, formats = [{'mimeType': 'image/tiff'}, {'mimeType': 'image/geotiff'}, {'mimeType': 'application/geotiff'}, {'mimeType': 'application/x-geotiff'}, {'mimeType': 'image/png'}, {'mimeType': 'image/gif'}, {'mimeType': 'image/jpeg'}, {'mimeType': 'application/x-erdas-hfa'}, {'mimeType': 'application/netcdf'}, {'mimeType': 'application/x-netcdf'}])
    self.addLiteralInput(identifier = '-f', title = 'Generate unformatted report (items separated by colon)', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])
    self.addLiteralInput(identifier = 'grass_resolution_ns', title = 'Resolution of the mapset in north-south direction in meters or degrees', abstract = 'This parameter defines the north-south resolution of the mapset in meter or degrees, which should be used to process the input and output raster data. To enable this setting, you need to specify north-south and east-west resolution.', minOccurs = 0, maxOccurs = 1, type = type(0.0), allowedValues = '*')
    self.addLiteralInput(identifier = 'grass_resolution_ew', title = 'Resolution of the mapset in east-west direction in meters or degrees', abstract = 'This parameter defines the east-west resolution of the mapset in meters or degrees, which should be used to process the input and output raster data.  To enable this setting, you need to specify north-south and east-west resolution.', minOccurs = 0, maxOccurs = 1, type = type(0.0), allowedValues = '*')
    self.addLiteralInput(identifier = 'grass_band_number', title = 'Band to select for processing (default is all bands)', abstract = 'This parameter defines band number of the input raster files which should be processed. As default all bands are processed and used as single and multiple inputs for raster modules.', minOccurs = 0, maxOccurs = 1, type = type(0), allowedValues = '*')

    # complex outputs
    self.addComplexOutput(identifier = 'centroids', title = 'Name for output vector points map to contain clump centroids', formats = [{'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/3.1.1/base/gml.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/xml', 'schema': 'http://schemas.opengis.net/gml/3.1.1/base/gml.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/kml/2.2.0/ogckml22.xsd', 'encoding': 'UTF-8'}])

    self.addComplexOutput(identifier = 'output', title = 'If no output file given report is printed to standard output', formats = [{'mimeType': 'text/plain'}])

  def execute(self):
    starter = PyWPSGrassModuleStarter()
    starter.fromPyWPS("r.volume", self.inputs, self.outputs, self.pywps)

if __name__ == "__main__":
  process = r_volume()
  process.execute()
