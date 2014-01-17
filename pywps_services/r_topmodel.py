# ################################################ #
# This process was generated using GrassXMLtoPyWPS #
# Author: Soeren Gebbert                           #
# Mail: soerengebbert <at> googlemail <dot> com    #
# ################################################ #

from pywps.Process import WPSProcess

from PyWPSGrassModuleStarter import PyWPSGrassModuleStarter

class r_topmodel(WPSProcess):

  def __init__(self):
    WPSProcess.__init__(self, identifier = 'r.topmodel', title = 'Simulates TOPMODEL which is a physically based hydrologic model.', version = 1, statusSupported = True, storeSupported = True, metadata = [{'type': 'simple', 'title': 'raster'}, {'type': 'simple', 'title': 'hydrology'}], abstract = 'http://grass.osgeo.org/grass70/manuals/html70_user/r.topmodel.html')

    # Literal and complex inputs
    self.addComplexInput(identifier = 'parameters', title = 'Name of TOPMODEL parameters file', minOccurs = 1, maxOccurs = 1, formats = [{'mimeType': 'text/plain'}])
    self.addComplexInput(identifier = 'topidxstats', title = 'Name of topographic index statistics file', minOccurs = 1, maxOccurs = 1, formats = [{'mimeType': 'text/plain'}])
    self.addComplexInput(identifier = 'input', title = 'Name of rainfall and potential evapotranspiration data file', minOccurs = 1, maxOccurs = 1, formats = [{'mimeType': 'text/plain'}])
    self.addLiteralInput(identifier = 'timestep', title = 'Generate output for this time step.', minOccurs = 0, maxOccurs = 1, type = type(0), allowedValues = '*')
    self.addLiteralInput(identifier = 'topidxclass', title = 'Generate output for this topographic index class.', minOccurs = 0, maxOccurs = 1, type = type(0), allowedValues = '*')
    self.addComplexInput(identifier = 'topidx', title = 'Must be clipped to the catchment boundary. Used for generating outtopidxstats.', minOccurs = 0, maxOccurs = 1, formats = [{'mimeType': 'image/tiff'}, {'mimeType': 'image/geotiff'}, {'mimeType': 'application/geotiff'}, {'mimeType': 'application/x-geotiff'}, {'mimeType': 'image/png'}, {'mimeType': 'image/gif'}, {'mimeType': 'image/jpeg'}, {'mimeType': 'application/x-erdas-hfa'}, {'mimeType': 'application/netcdf'}, {'mimeType': 'application/x-netcdf'}])
    self.addLiteralInput(identifier = 'ntopidxclasses', title = 'Used for generating outtopidxstats.', minOccurs = 0, maxOccurs = 1, type = type(0), default = 30)
    self.addLiteralInput(identifier = '-p', title = 'Preprocess only and stop after generating outtopidxstats', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])
    self.addLiteralInput(identifier = 'grass_resolution_ns', title = 'Resolution of the mapset in north-south direction in meters or degrees', abstract = 'This parameter defines the north-south resolution of the mapset in meter or degrees, which should be used to process the input and output raster data. To enable this setting, you need to specify north-south and east-west resolution.', minOccurs = 0, maxOccurs = 1, type = type(0.0), allowedValues = '*')
    self.addLiteralInput(identifier = 'grass_resolution_ew', title = 'Resolution of the mapset in east-west direction in meters or degrees', abstract = 'This parameter defines the east-west resolution of the mapset in meters or degrees, which should be used to process the input and output raster data.  To enable this setting, you need to specify north-south and east-west resolution.', minOccurs = 0, maxOccurs = 1, type = type(0.0), allowedValues = '*')
    self.addLiteralInput(identifier = 'grass_band_number', title = 'Band to select for processing (default is all bands)', abstract = 'This parameter defines band number of the input raster files which should be processed. As default all bands are processed and used as single and multiple inputs for raster modules.', minOccurs = 0, maxOccurs = 1, type = type(0), allowedValues = '*')

    # complex outputs
    self.addComplexOutput(identifier = 'output', title = 'Name for output file', formats = [{'mimeType': 'text/plain'}])

    self.addComplexOutput(identifier = 'outtopidxstats', title = 'Requires topidx and ntopidxclasses.', formats = [{'mimeType': 'text/plain'}])

  def execute(self):
    starter = PyWPSGrassModuleStarter()
    starter.fromPyWPS("r.topmodel", self.inputs, self.outputs, self.pywps)

if __name__ == "__main__":
  process = r_topmodel()
  process.execute()
