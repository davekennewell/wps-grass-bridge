# ################################################ #
# This process was generated using GrassXMLtoPyWPS #
# Author: Soeren Gebbert                           #
# Mail: soerengebbert <at> googlemail <dot> com    #
# ################################################ #

from pywps.Process import WPSProcess

from PyWPSGrassModuleStarter import PyWPSGrassModuleStarter

class v_surf_bspline(WPSProcess):

  def __init__(self):
    WPSProcess.__init__(self, identifier = 'v.surf.bspline', title = 'Performs bicubic or bilinear spline interpolation with Tykhonov regularization.', version = 1, statusSupported = True, storeSupported = True, metadata = [{'type': 'simple', 'title': 'vector'}, {'type': 'simple', 'title': 'surface'}, {'type': 'simple', 'title': 'interpolation'}, {'type': 'simple', 'title': 'LIDAR'}], abstract = 'http://grass.osgeo.org/grass70/manuals/html70_user/v.surf.bspline.html')

    # Literal and complex inputs
    self.addComplexInput(identifier = 'input', title = 'Name of input vector point map', abstract = 'Or data source for direct OGR access', minOccurs = 1, maxOccurs = 1, formats = [{'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/3.1.1/base/gml.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/xml', 'schema': 'http://schemas.opengis.net/gml/3.1.1/base/gml.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/kml/2.2.0/ogckml22.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/dgn', 'schema': 'None', 'encoding': 'None'}, {'mimeType': 'application/shp', 'schema': 'None', 'encoding': 'None'}, {'mimeType': 'application/x-zipped-shp', 'schema': 'None', 'encoding': 'None'}])
    self.addLiteralInput(identifier = 'layer', title = 'Layer number or name', abstract = 'Vector features can have category values in different layers. This number determines which layer to use. When used with direct OGR access this is the layer name.', minOccurs = 0, maxOccurs = 1, type = type("string"), default = "1")
    self.addComplexInput(identifier = 'sparse_input', title = 'Name of input vector map with sparse points', abstract = 'Or data source for direct OGR access', minOccurs = 0, maxOccurs = 1, formats = [{'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/3.1.1/base/gml.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/xml', 'schema': 'http://schemas.opengis.net/gml/3.1.1/base/gml.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/kml/2.2.0/ogckml22.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/dgn', 'schema': 'None', 'encoding': 'None'}, {'mimeType': 'application/shp', 'schema': 'None', 'encoding': 'None'}, {'mimeType': 'application/x-zipped-shp', 'schema': 'None', 'encoding': 'None'}])
    self.addComplexInput(identifier = 'mask', title = 'Raster map to use for masking (applies to raster output only)', abstract = 'Only cells that are not NULL and not zero are interpolated', minOccurs = 0, maxOccurs = 1, formats = [{'mimeType': 'image/tiff'}, {'mimeType': 'image/geotiff'}, {'mimeType': 'application/geotiff'}, {'mimeType': 'application/x-geotiff'}, {'mimeType': 'image/png'}, {'mimeType': 'image/gif'}, {'mimeType': 'image/jpeg'}, {'mimeType': 'application/x-erdas-hfa'}, {'mimeType': 'application/netcdf'}, {'mimeType': 'application/x-netcdf'}])
    self.addLiteralInput(identifier = 'sie', title = 'Length of each spline step in the east-west direction', minOccurs = 0, maxOccurs = 1, type = type(0.0), default = 4.0)
    self.addLiteralInput(identifier = 'sin', title = 'Length of each spline step in the north-south direction', minOccurs = 0, maxOccurs = 1, type = type(0.0), default = 4.0)
    self.addLiteralInput(identifier = 'method', title = 'Spline interpolation algorithm', minOccurs = 0, maxOccurs = 1, type = type("string"), default = "linear", allowedValues = ['linear', 'cubic'])
    self.addLiteralInput(identifier = 'lambda_i', title = 'Tykhonov regularization parameter (affects smoothing)', minOccurs = 0, maxOccurs = 1, type = type(0.0), default = 0.01)
    self.addLiteralInput(identifier = 'column', title = 'Name of the attribute column with values to be used for approximation', abstract = 'If not given and input is 3D vector map then z-coordinates are used.', minOccurs = 0, maxOccurs = 1, type = type("string"), allowedValues = '*')
    self.addLiteralInput(identifier = 'solver', title = 'The type of solver which should solve the symmetric linear equation system', minOccurs = 0, maxOccurs = 1, type = type("string"), default = "cholesky", allowedValues = ['cholesky', 'cg'])
    self.addLiteralInput(identifier = 'maxit', title = 'Maximum number of iteration used to solve the linear equation system', minOccurs = 0, maxOccurs = 1, type = type(0), default = 10000)
    self.addLiteralInput(identifier = 'error', title = 'Error break criteria for iterative solver', minOccurs = 0, maxOccurs = 1, type = type(0.0), default = 1e-06)
    self.addLiteralInput(identifier = 'memory', title = 'Maximum memory to be used for raster output (in MB)', minOccurs = 0, maxOccurs = 1, type = type(0), default = 300)
    self.addLiteralInput(identifier = '-c', title = 'Find the best Tykhonov regularizing parameter using a "leave-one-out" cross validation method', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])
    self.addLiteralInput(identifier = '-e', title = 'Estimate point density and distance for the input vector points within the current region extends and quit', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])
    self.addLiteralInput(identifier = 'grass_resolution_ns', title = 'Resolution of the mapset in north-south direction in meters or degrees', abstract = 'This parameter defines the north-south resolution of the mapset in meter or degrees, which should be used to process the input and output raster data. To enable this setting, you need to specify north-south and east-west resolution.', minOccurs = 0, maxOccurs = 1, type = type(0.0), allowedValues = '*')
    self.addLiteralInput(identifier = 'grass_resolution_ew', title = 'Resolution of the mapset in east-west direction in meters or degrees', abstract = 'This parameter defines the east-west resolution of the mapset in meters or degrees, which should be used to process the input and output raster data.  To enable this setting, you need to specify north-south and east-west resolution.', minOccurs = 0, maxOccurs = 1, type = type(0.0), allowedValues = '*')
    self.addLiteralInput(identifier = 'grass_band_number', title = 'Band to select for processing (default is all bands)', abstract = 'This parameter defines band number of the input raster files which should be processed. As default all bands are processed and used as single and multiple inputs for raster modules.', minOccurs = 0, maxOccurs = 1, type = type(0), allowedValues = '*')

    # complex outputs
    self.addComplexOutput(identifier = 'output', title = 'Name for output vector map', formats = [{'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/3.1.1/base/gml.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/xml', 'schema': 'http://schemas.opengis.net/gml/3.1.1/base/gml.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/kml/2.2.0/ogckml22.xsd', 'encoding': 'UTF-8'}])

    self.addComplexOutput(identifier = 'raster_output', title = 'Name for output raster map', formats = [{'mimeType': 'image/tiff'}, {'mimeType': 'image/geotiff'}, {'mimeType': 'application/geotiff'}, {'mimeType': 'application/x-geotiff'}, {'mimeType': 'application/x-erdas-hfa'}, {'mimeType': 'application/netcdf'}, {'mimeType': 'application/x-netcdf'}])

  def execute(self):
    starter = PyWPSGrassModuleStarter()
    starter.fromPyWPS("v.surf.bspline", self.inputs, self.outputs, self.pywps)

if __name__ == "__main__":
  process = v_surf_bspline()
  process.execute()
